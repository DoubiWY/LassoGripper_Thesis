// ESP32 Dev Module
#include <SCServo.h>
#include <HardwareSerial.h>
#include <FastLED.h>

HardwareSerial SerialServo(1); // UART1
SMS_STS sms_sts;

#define LED_PIN  23     // WS2812 pin
#define S_RXD 18
#define S_TXD 19
#define NUM_LEDS 12      // num of LED
// #define DEBUGINFO

CRGB leds[NUM_LEDS];

const int NUM_SERVO = 8;
int ID[NUM_SERVO]       = {1, 2, 3, 4, 5, 6, 7, 8};
int Pos[NUM_SERVO];
int Speed[NUM_SERVO];
int Load[NUM_SERVO];
int Voltage[NUM_SERVO];
int Temper[NUM_SERVO];
int Move[NUM_SERVO];
int Current[NUM_SERVO];

byte ControlID[4]      = {1,2,3,4};

bool lock_flag = false;
bool unload_flag = false;
const float gripper_open = 5.0;
#define LOCK

uint8_t cmd_buf[8];
int buildSMSWriteCmd(uint8_t id, uint8_t cmd, uint8_t* out_buf) {
    // Serial Protocol: 0 -> unload; 1 -> enable; 128 -> 2048 calibration when in position mode
    out_buf[0] = 0xFF;           // head
    out_buf[1] = 0xFF;           // head
    out_buf[2] = id;             // Servo ID
    out_buf[3] = 0x04;           // Length
    out_buf[4] = 0x03;           // Instructuion
    out_buf[5] = 0x28;           // Reginster
    out_buf[6] = cmd;            // Cmd
    uint8_t check = ~(id + 0x04 + 0x03 + 0x28 + cmd) & 0xFF;
    out_buf[7] = check;
    return 8;
}

void setAllLED(CRGB color) {
    for (int i = 0; i < NUM_LEDS; ++i) leds[i] = color;
    FastLED.show();
}

void setup()
{
    SerialServo.begin(500000, SERIAL_8N1, S_RXD, S_TXD);
    sms_sts.pSerial = &SerialServo;
    Serial.begin(115200);

    delay(1000);

    FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
    FastLED.clear();
    FastLED.show();

    sms_sts.WritePosEx(ID[5-1], 2048, 0, 0);
    sms_sts.WritePosEx(ID[6-1], 2048, 0, 0);
    delay(2000);
}

void loop()
{
    // Step 1: feedback of 8 servos
    for (int i = 0; i < NUM_SERVO; ++i) {
        sms_sts.FeedBack(ID[i]);
        if(!sms_sts.getLastError()){
            Pos[i]     = sms_sts.ReadPos(-1);
            Speed[i]   = sms_sts.ReadSpeed(-1);
            Load[i]    = sms_sts.ReadLoad(-1);
            Voltage[i] = sms_sts.ReadVoltage(-1);
            Temper[i]  = sms_sts.ReadTemper(-1);
            Move[i]    = sms_sts.ReadMove(-1);
            Current[i] = sms_sts.ReadCurrent(-1);
            if(i == 6)
            {
              Serial.print("ID:"); Serial.print(ID[i]);
              Serial.print(" Pos:"); Serial.println(Pos[i]);
            }
            #ifdef DEBUGINFO
                Serial.print("ID:"); Serial.print(ID[i]);
                Serial.print(" Pos:"); Serial.print(Pos[i]);
                Serial.print(" Speed:"); Serial.print(Speed[i]);
                Serial.print(" Load:"); Serial.print(Load[i]);
                Serial.print(" V:"); Serial.print(Voltage[i]);
                Serial.print(" T:"); Serial.print(Temper[i]);
                Serial.print(" Move:"); Serial.print(Move[i]);
                Serial.print(" Current:"); Serial.println(Current[i]);
            #endif
        } else {
            Serial.print("FeedBack error for ID: "); Serial.println(ID[i]);
            Pos[i] = -1;
            setAllLED(CRGB(255, 0, 0));
            exit(-1);
        }
    }

    // Step 2: hand cmd
    int p5, p6, p7, p8, mid;
    p5 = Pos[4];
    p6 = Pos[5];
    p7 = Pos[6];
    p8 = Pos[7];
    mid = 2048;
    float roll_cmd, pitch_cmd, yaw_cmd, gripper_cmd; // map from hand
    float roll_in, pitch_in, yaw_in;    // trans hand cmd to servo inputs

    roll_cmd  = -(p8 - mid) / 4096.0 * 360.0;
    pitch_cmd =  (p6 - mid) / 4096.0 * 360.0 * 1.5;
    yaw_cmd   = -(p5 - mid) / 4096.0 * 360.0 * 6.0 ;

    gripper_cmd = -(p7 - mid) / 4096.0 * 360.0 * 1.5;

    // Step 3: RPY of the center of gripper
    roll_in  = 65   / 35.0 * roll_cmd;
    pitch_in = 4.5  / 5.5  * pitch_cmd;
    yaw_in   = 5.15 / 5.5  * yaw_cmd + 3.25 / 5.5 * pitch_cmd;

    // Step 4: calculate servo cmd
    int s1_pitch, s2_roll, s3_yaw_right, s4_yaw_left; 
    const int s1_phase = -1, s2_phase = 1, s3_phase = -1, s4_phase = 1;
    const float gripper_range = 30.0;
    s1_pitch     = int(s1_phase * pitch_in / 360.0 * 4096.0 + 2048.0);
    s2_roll      = int(s2_phase * roll_in  / 360.0 * 4096.0 + 2048.0);
    s3_yaw_right = int(s3_phase * (yaw_in - gripper_cmd + gripper_range)  / 360.0 * 4096.0 + 2048.0);
    s4_yaw_left  = int(s4_phase * (yaw_in + gripper_cmd*1.2 - gripper_range)  / 360.0 * 4096.0 + 2048.0);

    // Step 5: Run servo
    #ifdef LOCK
    if(gripper_cmd > gripper_open)
    {
        if(!unload_flag)
        {
            buildSMSWriteCmd(ID[5-1], 0, cmd_buf);
            SerialServo.write(cmd_buf, 8);
            delay(1);
            buildSMSWriteCmd(ID[6-1], 0, cmd_buf);
            SerialServo.write(cmd_buf, 8);
            delay(1);
            unload_flag = true;
        }
        sms_sts.WritePosEx(ID[1-1], s1_pitch,     0, 0);
        sms_sts.WritePosEx(ID[2-1], s2_roll,      0, 0);
        sms_sts.WritePosEx(ID[3-1], s3_yaw_right, 0, 0);
        sms_sts.WritePosEx(ID[4-1], s4_yaw_left,  0, 0);
        lock_flag = false;
    }
    else
    {
        if(!lock_flag)
        {
            buildSMSWriteCmd(ID[5-1], 1, cmd_buf);
            SerialServo.write(cmd_buf, 8);
            delay(1);
            buildSMSWriteCmd(ID[6-1], 1, cmd_buf);
            SerialServo.write(cmd_buf, 8);
            delay(1);
            for(int i = 0; i < 6; i++)
                sms_sts.WritePosEx(ID[i], Pos[i],  0, 0);
            lock_flag = true;
        }
        unload_flag = false;

    }

    #else
    sms_sts.WritePosEx(ID[1-1], s1_pitch,     0, 0);
    sms_sts.WritePosEx(ID[2-1], s2_roll,      0, 0);
    sms_sts.WritePosEx(ID[3-1], s3_yaw_right, 0, 0);
    sms_sts.WritePosEx(ID[4-1], s4_yaw_left,  0, 0);
    #endif
    
    // rate control
    delay(3);
}

// update library link
// https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
