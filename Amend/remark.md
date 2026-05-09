## 关于具体内容

# Lasso Gripper
关于具体实验中，大部分场景都是实验了两次并且成功了两次，但因为在实验前我们已经预设好了相对应的绳圈长度和抓取角度。只有在抓取青椒的时候，因为青椒重量不均匀的缘故，有一次是从绳圈中掉落了出去。
- 牛马雕像是用3d打印机打印的，重量在50g左右；
- 无人机的重量是249g，是大疆的mini3
- 白菜的重量是170g
- 可乐的305g
- 青椒的重量是90g
这些具体的实验截图已经在文中涵盖了，对应的是fig6.1, 6.2, 6.3

# 医疗器械
新的图片已经放在同一文件夹下，并通过命名的方式进行了简要概括。主要添加了3d模型的爆炸图，FEA下关于模型的mesh图，其中包括了fixture和load condition。

关于电机的型号已经在文中有所说明，分别是飞特的sts3032和sts3009，选择这两款电机的原因是基于体积、重量和扭矩的共同考虑。手持的特性决定了整个设备的重量不能过于重，否则使用者在使用过程中会感到疲劳。

cable的型号是采用了复合钨丝的结构，本身是用7*37的结构组成了直径0.5mm的钨丝，即由7股编织而成，每股由37根独立的钨丝编织而成。这样的结构提供了足够的柔韧性的同时破断力也达到了501.7N。

Reel的转动直径与前面tip的转动轴直径相等，都是11m。这样的设计确保了reel和tip的传动比是1:1。另外整个tip横滚的齿轮传动比是35:65，可以更精细的调整转动角度以及确保整个快拆部分的体积不至于过大

总  重：682g，操作钳：143g，手  柄：539g



## 参考文献
# Chen, N., Huang, Q., Sui, S., Zhao, Q., and Lin, J. (December 13, 2025). "Design and Implementation of a Handheld Steerable Surgical Device for Minimally Invasive Surgeries." ASME. J. Med. Devices. February 2026; 20(1): 011006. https://doi.org/10.1115/1.4070276

abstract:Pursuing minimal invasiveness is a trend in the development of modern surgeries as smaller size of incision reduces blood loss and postoperative hospitalization stay. This poses high requirement on surgical devices including endoscopes and instruments because the surgeon is difficult to see the full view of the surgical site via a small port. In addition, slenderness and steerability are also critical to access and perform manipulation in complex anatomies. Therefore, we proposed a handheld steerable surgical device to address the problems, with which the incision could be minimized to 3.2 mm in diameter. It consists of a steerable endoscope formed by cable-driven riveted continuum structure and two dexterous slender instruments using concentric push–pull robot (CPPR) mechanism. In design, analysis on the steerability and stiffness about the endoscope was conducted, and we also modeled the tip tool pose with respect to actuation configuration. Specific pattern of CPPR structure benefits designing slender instruments (1.1 mm in outer diameter), and two CPPR-based dexterous instruments pass through the hollow space of the endoscope to reach the narrow constrained surgical sites. Experiments show the potential of the portable device, and ex vivo tests on a porcine lung and heart demonstrate the overall clinic advantages.

# Nonlinear friction modelling and compensation control of hysteresis phenomena for a pair of tendon-sheath actuated  surgical robots
Abstract: Natural Orifice Transluminal Endoscopic Surgery (NOTES) is a special method that allows surgical operations via natural orifices like mouth, anus, and vagina, without leaving visible scars. The use of flexible tendon-sheath mechanism (TSM) is common in these systems because of its light weight in structure, flexibility, and easy transmission of power. However, nonlinear friction and backlash hysteresis pose many challenges to control of such systems; in addition, they do not provide haptic feedback to assist the surgeon in the operation of the systems. In this paper, we propose a new dynamic friction model and backlash hysteresis nonlinearity for a pair of TSM to deal with these problems. The proposed friction model, unlike current approaches in the literature, is smooth and able to capture the force at near zero velocity when the system is stationary or operates at small motion. This model can be used to estimate the friction force for haptic feedback purpose. To improve the system tracking performances, a backlash hysteresis model will be introduced, which can be used in a feedforward controller scheme. The controller involves a simple computation of the inverse hysteresis model. The proposed models are configuration independent and able to capture the nonlinearities for arbitrary tendon-sheath shapes. A representative experimental setup is used to validate the proposed models and to demonstrate the improvement in position tracking accuracy and the possibility of providing desired force information at the distal end of a pair of TSM slave manipulator for haptic feedback to the surgeons.

# Modeling and motion compensation of a bidirectional tendon-sheath actuated system for robotic endoscopic surgery
Abstract: Recent study shows that tendon-sheath system (TSS) has great potential in the development of surgical robots for endoscopic surgery. It is able to deliver adequate power in a light-weight and compact package. And the flexibility and compliance of the tendon-sheath system make it capable of adapting to the long and winding path in the flexible endoscope. However, the main difficulties in precise control of such system fall on the nonlinearities of the system behavior and absence of necessary sensory feedback at the surgical end-effectors. Since accurate position control of the tool is a prerequisite for efficacy, safety and intuitive user-experience in robotic surgery, in this paper we propose a system modeling approach for motion compensation. Based on a bidirectional actuated system using two separate tendon-sheaths, motion transmission is firstly characterized. Two types of positional errors due to system backlash and environment loading are defined and modeled. Then a model-based feedforward compensation method is proposed for open-loop control, giving the system abilities to adjust according to changes in the transmission route configuration without any information feedback from the distal end. A dedicated experimental platform emulating a bidirectional TSS robotic system for endoscopic surgery is built for testing. Proposed positional errors are identified and verified. The performance of the proposed motion compensation is evaluated by trajectory tracking under different environment loading conditions. And the results demonstrate that accurate position control can be achieved even if the transmission route configuration is updated.



@inproceedings{berthet-rayne_rolling-joint_2018,
	location = {Madrid},
	title = {Rolling-Joint Design Optimization for Tendon Driven Snake-Like Surgical Robots},
	url = {https://ieeexplore.ieee.org/document/8593517/},
	doi = {10.1109/iros.2018.8593517},
	abstract = {The use of snake-like robots for surgery is a popular choice for intra-luminal procedures. In practice, the requirements for strength, ﬂexibility and accuracy are difﬁcult to be satisﬁed simultaneously. This paper presents a computational approach for optimizing the design of a snake-like robot using serial rolling-joints and tendons as the base architecture. The method optimizes the design in terms of joint angle range and tendon placement to prevent the tendons and joints from colliding during bending motion. The resulting optimized joints were manufactured using 3D printing. The robot was characterized in terms of workspace, dexterity, precision and manipulation forces. The results show a repeatability as low as 0.9 mm and manipulation forces of up to 5.6 N.},
	eventtitle = {2018 {IEEE}/{RSJ} International Conference on Intelligent Robots and Systems ({IROS})},
	pages = {4964--4971},
	booktitle = {2018 {IEEE}/{RSJ} International Conference on Intelligent Robots and Systems ({IROS})},
	publisher = {{IEEE}},
	author = {Berthet-Rayne, Pierre and Leibrandt, Konrad and Kim, Kiyoung and Seneci, Carlo A. and Shang, Jianzhong and Yang, Guang-Zhong},
	urldate = {2026-05-09},
	date = {2018-10},
	langid = {english},
	file = {PDF:C\:\\Users\\Yu\\Zotero\\storage\\WTN6H4T3\\Berthet-Rayne 等 - 2018 - Rolling-Joint Design Optimization for Tendon Driven Snake-Like Surgical Robots.pdf:application/pdf},
}

@article{park_empirical_2024,
	title = {Empirical modeling of hysteresis in a tendon–sheath mechanism on multi-segmented curves},
	volume = {17},
	rights = {https://www.springernature.com/gp/researchers/text-and-data-mining},
	issn = {1861-2776, 1861-2784},
	url = {https://link.springer.com/10.1007/s11370-024-00542-5},
	doi = {10.1007/s11370-024-00542-5},
	abstract = {Flexible surgical robots can move with increased ﬂexibility compared with conventional laparoscopic surgical robots, enabling surgeries along arbitrary curved paths. Because of these characteristics, ﬂexible surgical robots are used for performing minimally invasive surgeries. The tendon–sheath mechanism ({TSM}) plays a pivotal role as a core component of ﬂexible surgical robots. The {TSM} can transmit displacement through small-diameter pathways along arbitrary trajectories; however, it exhibits nonlinear hysteresis depending on the shape of the curved paths encountered. In this study, the hysteresis changes occurring in the {TSM} when handling multiple-curved paths were investigated using different variable combinations. A hysteresis model for a single-curved path proposed in a previous study was extended to estimate the magnitude of hysteresis in a multiple-curved path. Results showed that the position of the curved path has a signiﬁcant inﬂuence on hysteresis; therefore, the hysteresis model was modiﬁed using an exponential function of the position. By superimposing the model for the hysteresis magnitude in single-curved paths with a nonlinear superposition method, we extended the model to include the hysteresis phenomena in multiple-curved paths. To validate this model, the experimental hysteresis results for a triple-curve path were compared with the model predicted values. The results show that the model proposed in this study can predict the hysteresis in a {TSM} on an arbitrary multiple-curved path and can serve as a basis for designing algorithms to compensate for the hysteresis in real time.},
	pages = {891--900},
	number = {4},
	journaltitle = {Intelligent Service Robotics},
	shortjournal = {Intel Serv Robotics},
	author = {Park, Su Hyeon and Jin, Sangrok},
	urldate = {2026-05-09},
	date = {2024-07},
	langid = {english},
	note = {Publisher: Springer Science and Business Media {LLC}},
	file = {PDF:C\:\\Users\\Yu\\Zotero\\storage\\NLHHEPTS\\Park和Jin - 2024 - Empirical modeling of hysteresis in a tendon–sheath mechanism on multi-segmented curves.pdf:application/pdf},
}

@article{li_novel_2024,
	title = {A Novel Cable-Driven Soft Robot for Surgery},
	volume = {29},
	rights = {https://www.springernature.com/gp/researchers/text-and-data-mining},
	issn = {1007-1172, 1995-8188},
	url = {https://link.springer.com/10.1007/s12204-022-2497-3},
	doi = {10.1007/s12204-022-2497-3},
	abstract = {Robot-assisted laparoscopic radical prostatectomy ({RARP}) is widely used to treat prostate cancer. The rigid instruments primarily used in {RARP} cannot overcome the problem of blind areas in surgery and lead to more trauma such as more incision for the passage of the instrument and additional tissue damage caused by rigid instruments. Soft robots are relatively ﬂexible and theoretically have inﬁnite degrees of freedom which can overcome the problem of the rigid instrument. A soft robot system for single-port transvesical robot-assisted radical prostatectomy ({STvRARP}) is developed in this study. The soft manipulator with 10 mm in diameter and a maximum bending angle of 270◦ has good ﬂexibility and dexterity. The design and mechanical structure of the soft robot are described. The kinematics of the soft manipulator is established and the inverse kinematics is compensated based on the characteristics of the designed soft manipulator. The master-slave control system of soft robot for surgery is built and the feasibility of the designed soft robot is veriﬁed.},
	pages = {60--72},
	number = {1},
	journaltitle = {Journal of Shanghai Jiaotong University (Science)},
	shortjournal = {J. Shanghai Jiaotong Univ. (Sci.)},
	author = {Li, Ru and Chen, Fang and Yu, Wenwei and Igarash, Tatsuo and Shu, Xiongpeng and Xie, Le},
	urldate = {2026-05-09},
	date = {2024-02},
	langid = {english},
	note = {Publisher: Springer Science and Business Media {LLC}},
	file = {PDF:C\:\\Users\\Yu\\Zotero\\storage\\6YFJHFQH\\Li 等 - 2024 - A Novel Cable-Driven Soft Robot for Surgery.pdf:application/pdf},
}

@article{zahraee_toward_2010,
	title = {Toward the Development of a Hand-Held Surgical Robot for Laparoscopy},
	rights = {https://ieeexplore.ieee.org/Xplorehelp/downloads/license-information/{IEEE}.html},
	issn = {1083-4435, 1941-014X},
	url = {http://ieeexplore.ieee.org/document/5523951/},
	doi = {10.1109/tmech.2010.2055577},
	abstract = {Minimally invasive surgery ({MIS}), which typically involves endoscopic camera and laparoscopic instruments may seem to be the ideal surgical procedure for its apparent beneﬁts. However, in comparison to open surgeries, the spatial and mechanical tool limitations posed on surgeons are so high that often {MIS} is foregone for complex cases and even when it is possible, the procedure requires a high dexterity, caliber, and experience from the surgeon. Particularly, suturing procedure through {MIS} is known to be extremely challenging. We are working toward the development of a robotic hand-held surgical device for laparoscopic interventions that enhances the surgeons’ dexterity. The instrument produces two independent {DOFs}, which is sufﬁcient for enabling {MIS} suturing procedure in vivo. The end-effector’s orientation is controlled by an intuitive and ergonomic controller and its position is controlled directly by the surgeon. Different control modes, handles, and end-effector kinematics are primarily evaluated using a virtual reality simulator before choosing the best combination. A proof-of-concept prototype of the device has been developed.},
	journaltitle = {{IEEE}/{ASME} Transactions on Mechatronics},
	shortjournal = {{IEEE}/{ASME} Trans. Mechatron.},
	author = {Zahraee, Ali Hassan and Paik, Jamie Kyujin and Szewczyk, Jerome and Morel, Guillaume},
	urldate = {2026-05-09},
	date = {2010-12},
	langid = {english},
	note = {Publisher: Institute of Electrical and Electronics Engineers ({IEEE})},
	file = {PDF:C\:\\Users\\Yu\\Zotero\\storage\\2EBA2V9X\\Zahraee 等 - 2010 - Toward the Development of a Hand-Held Surgical Robot for Laparoscopy.pdf:application/pdf},
}
