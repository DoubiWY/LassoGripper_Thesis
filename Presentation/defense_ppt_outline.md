# Thesis Defense PPT Outline

Title: `Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments`

Each slide below uses compressed bullet text suitable for PowerPoint.

## Slide 1. Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments

Image: `Figures/overview_transparent.png`

Slide bullets:
- Yu Wang
- Supervisor: Prof. Peng Lu
- Department of Mechanical Engineering, HKU

Speaker script:
> Good morning, and thank you for attending my MPhil thesis defense. This thesis is mechanism-centered. Instead of presenting two unrelated devices, I study a common tendon-driven design framework and validate it through two embodiments: a handheld laparoscopic instrument for surgical manipulation, and Lasso Gripper for adaptive grasping.

## Slide 2. Motivation

Image: `Figures/surgical instrument.jpg`

Slide bullets:
- Narrow workspaces
- Fragile, irregular, or moving targets
- Low distal mass is required
- Tendon-driven systems offer compliance and remote actuation

Speaker script:
> Robotic manipulation becomes difficult when the workspace is constrained, when targets are fragile or irregular, and when the distal end must remain lightweight. These requirements appear in both general robotic grasping and minimally invasive surgery. Tendon-driven mechanisms are attractive because they transmit force through lightweight tensile elements and enable proximal actuation.

## Slide 3. Research Gap

Image: `Figures/soft modular.png`

Slide bullets:
- Surgical tools and adaptive grippers are often separate
- Most designs are application-driven
- A transferable tendon-driven framework is still missing

Speaker script:
> Existing literature contains many cable-driven surgical tools and many adaptive grippers, but these topics are usually studied in isolation. As a result, design knowledge remains application-specific. My thesis addresses this gap by extracting mechanism principles that can be transferred across domains.

## Slide 4. Research Question

Image: `Figures/overview.png`

Slide bullets:
- How can tendon-driven mechanisms be systematically designed
- to achieve adaptive, dexterous, and safe manipulation
- under limited space, low distal inertia, and compliant contact?

Speaker script:
> The central question of this thesis is how tendon-driven mechanisms can be systematically designed to achieve adaptive, dexterous, and safe manipulation under constraints of limited space, low distal inertia, and compliant contact. This question defines the whole thesis.

## Slide 5. Main Contributions

Image: `Figures/overview_transparent.png`

Slide bullets:
 - Mechanism-level study of tendon-driven systems
 - Handheld surgical instrument as the first embodiment
 - Transferable design principles extracted
 - Lasso Gripper as the second embodiment

Speaker script:
> The thesis makes four contributions. First, it studies tendon-driven systems at the mechanism level. Second, it develops a handheld surgical instrument as the first embodiment. Third, it extracts transferable design principles. Fourth, it demonstrates those principles in Lasso Gripper as the second embodiment.

## Slide 6. Thesis Roadmap

Image: `Figures/overview_transparent.png`

Slide bullets:
 - Problem definition
 - Related work
 - Surgical translation
 - Extracted mechanism principles
 - Lasso Gripper

Speaker script:
> This slide shows the roadmap of the thesis. I begin with the mechanism problem, then review related work. The first embodiment is the handheld surgical instrument, which is used to discover and validate mechanism principles. These principles are then transferred to the second embodiment, Lasso Gripper.

## Slide 7. Related Work: Surgical Instruments

Image: `Figures/trimmed.png`

Slide bullets:
- Cable-driven instruments improve distal dexterity
- Key issues: coupling, friction, hysteresis, weight
- The tradeoff between dexterity and usability remains open

Speaker script:
> On the surgical side, cable-driven instruments recover distal dexterity while keeping actuators away from the tip. However, this comes with coupling, friction, hysteresis, and practical weight penalties. Many studies optimize one part of the system, but fewer address the overall mechanism tradeoff between dexterity, tension control, and ergonomic usability.

## Slide 8. Related Work: Adaptive Grasping

Image: `Figures/8.png`

Slide bullets:
- Soft and enveloping grippers improve shape adaptation
- Rigid grippers still struggle with fragile or oversized targets
- A mechanism with both capture range and controlled force is needed

Speaker script:
> On the grasping side, soft and enveloping designs improve shape adaptability, but many systems sacrifice reach, force transmission, or controllability. Traditional rigid-finger grippers are less effective for fragile, oversized, or highly variable targets. This motivates a loop-based and tension-driven strategy.

## Slide 9. Common Mechanism Principles

Image: `Figures/overview.png`

Slide bullets:
- Tension management
- Proximal actuation
- Differential routing
- Compliant interaction
- Low distal inertia

Speaker script:
> These five principles unify the thesis. Tension management ensures predictable force transmission. Proximal actuation reduces distal mass. Differential routing enables compact multi-DOF behavior. Compliant interaction improves safety and adaptability.

## Slide 10. Embodiment 2: Lasso Gripper Concept

Image: `Figures/Figure1.png`

Slide bullets:
 - Inspired by the lasso and the uurga
 - Loop-based capture instead of point contact
 - Adaptive capture region for uncertain targets

Speaker script:
> The second embodiment is Lasso Gripper. Its inspiration comes from traditional capture tools such as the lasso and the uurga. The key idea is to use a controllable string loop as the primary grasping structure, so that capture is achieved through tension-driven closure rather than rigid fingertip contact.

## Slide 11. Lasso Gripper: Mechanical Design

Image: `Figures/overall_img.png`

Slide bullets:
- Launch and retraction subsystems
- Friction-wheel-based string propulsion
- Spool mechanism for storage and recovery
- ESP32-based controller integration

Speaker script:
> This slide shows the hardware of Lasso Gripper. The system includes dedicated launch and retraction subsystems. Friction wheels propel the string to form the loop, while a spool handles storage and retraction. Mechanically, the design focuses on fast deployment, reliable recovery, and stable tension.

## Slide 12. Lasso Gripper: Grasping Strategy

Image: `Figures/caging.png`

Slide bullets:
- Point-cloud-based target understanding
- Caging-loop-based placement
- Controlled tightening with feedback

Speaker script:
> Grasping in Lasso Gripper combines mechanism and planning. The system identifies suitable loop placement based on point cloud information and caging principles. After loop positioning, tightening is coordinated with approach motion, while feedback regulates the capture process.

## Slide 13. Lasso Gripper: Dynamics and Workspace

Image: `Figures/stringsim.png`

Slide bullets:
- String-loop dynamics explain deployed behavior
- Workspace is estimated from loop geometry
- Modeling supports design and control

Speaker script:
> To move beyond demonstration, the loop behavior also needs to be understood analytically. This part of the thesis models the string dynamics and estimates the workspace associated with the deployed configuration. The analysis connects geometric behavior, launch conditions, and practical capture capability.

## Slide 14. Lasso Gripper: Experimental Results

Image: `Figures/test1.png`

Slide bullets:
- Static object capture
- Shape-adaptive grasping
- Oversized object handling
- Moving target capture

Speaker script:
> These experiments validate Lasso Gripper across a range of scenarios. It successfully captures animal figures, irregular objects, oversized balloons, and moving targets. Together, these demonstrations show that the loop-based mechanism offers both broad capture tolerance and gentle interaction.

## Slide 15. Comparison with Conventional Grippers

Image: `Figures/compare.png`

Slide bullets:
- Antipodal gripping concentrates stress
- Loop gripping distributes contact force
- Better for delicate and shape-variable targets

Speaker script:
> This comparison highlights why the mechanism matters. A conventional antipodal gripper applies concentrated stress to the target, which is problematic for delicate or highly deformable objects. In contrast, Lasso Gripper distributes contact through the loop.

## Slide 16. Mechanism Insights from Lasso Gripper

Image: `Figures/overview.png`

Slide bullets:
- Controlled tension improves repeatability
- Flexible contact improves tolerance to uncertainty
- Proximal actuation reduces distal complexity
- Differential routing is transferable

Speaker script:
> The key outcome of Lasso Gripper is not only a new end-effector. It also provides transferable mechanism insights. Controlled tension improves repeatability, flexible contact improves tolerance to uncertainty, and proximal actuation with differential routing can be reused beyond grasping.

## Slide 17. Embodiment 1: Surgical Translation

Image: `Figures/surgical instrument.jpg`

Slide bullets:
- Clinical constraints are much stricter
- Need distal dexterity without heavy distal hardware
- Need ergonomic balance and motion fidelity

Speaker script:
> The first embodiment tests the same mechanism framework in a more constrained setting. In minimally invasive surgery, the instrument must be slender, precise, ergonomic, and safe. This makes tendon-driven actuation especially relevant, because it allows actuation to remain proximal while producing multi-DOF motion at the tip.

## Slide 18. Surgical Instrument: Design

Image: `Figures/Motor Arrangement.png`

Slide bullets:
- Compact output actuation and input sensing
- Tension-preserving reel architecture
- Cable routing and tip design
- Quick-swap modular structure

Speaker script:
> This slide summarizes the architecture of the handheld surgical instrument. The design combines proximal actuation, compact motor arrangement, dedicated reel architecture, and precise cable routing. The reel is especially important because it preserves bidirectional tension and reduces slack accumulation.

## Slide 18b. 手术器械：历史版本演化

Image: `Presentation/医疗机械臂/ver1.0.png`  (建议同时在幻灯片中展示 3–4 张缩略图)

Slide bullets:
- v1.0: 拇指摇杆与波轮的4自由度设计，最小化钳头体积
- v2.0: 云台手柄稳定与食指捏合反馈，改进操控人机工程
- v3.3: 自设计PCB与定制钳头、双电机自稳实现精度提升
- v4.1: 恢复俯仰、横滚自由度，采用大扭矩直驱电机

Speaker script:
> 本幻灯片展示手术器械从早期原型到当前版本的关键演化。每一轮迭代都针对早期问题（如张力管理、操控稳定性或体积）做出权衡和改进，最终形成当前的卷盘与紧凑马达布局架构。

## Slide 19. Surgical Instrument: Control and Validation

Image: `Figures/input.png`

Slide bullets:
- Signal filtering plus closed-loop motor feedback
- Improved motion fidelity in a hand-held device
- Same mechanism principles under different constraints

Speaker script:
> The control system combines signal filtering and closed-loop motor feedback to improve motion fidelity in a hand-held setting. At this point, the connection between the two embodiments becomes clear. Lasso Gripper validates adaptive interaction under uncertainty, while the surgical instrument validates dexterity and controllability under clinical constraints.

## Slide 20. Conclusion and Future Work

Image: `Figures/overview_transparent.png`

Slide bullets:
- A transferable tendon-driven framework is established
- Validated in grasping and surgical manipulation
- Future work: adaptive control, modular instruments, multi-loop grasping

Speaker script:
> In conclusion, this thesis shows that tendon-driven mechanisms can be systematically designed as a transferable framework for adaptive grasping, dexterous manipulation, and safe interaction. Lasso Gripper and the handheld surgical instrument are two embodiments of that same idea. Future work will further improve adaptive control, modularity, and loop-based grasping in dynamic environments.
