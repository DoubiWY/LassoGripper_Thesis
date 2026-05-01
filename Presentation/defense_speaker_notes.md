Slide 1 — Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments

Speaker script:
Good morning, and thank you for attending my MPhil thesis defense. This thesis is mechanism-centered. Instead of presenting two unrelated devices, I study a common tendon-driven design framework and validate it through two embodiments: a handheld laparoscopic instrument for surgical manipulation, and Lasso Gripper for adaptive grasping.

---
Slide 2 — Motivation

Speaker script:
Robotic manipulation becomes difficult when the workspace is constrained, when targets are fragile or irregular, and when the distal end must remain lightweight. These requirements appear in both general robotic grasping and minimally invasive surgery. Tendon-driven mechanisms are attractive because they transmit force through lightweight tensile elements and enable proximal actuation.

---
Slide 3 — Research Gap

Speaker script:
Existing literature contains many cable-driven surgical tools and many adaptive grippers, but these topics are usually studied in isolation. As a result, design knowledge remains application-specific. My thesis addresses this gap by extracting mechanism principles that can be transferred across domains.

---
Slide 4 — Research Question

Speaker script:
The central question of this thesis is how tendon-driven mechanisms can be systematically designed to achieve adaptive, dexterous, and safe manipulation under constraints of limited space, low distal inertia, and compliant contact. This question defines the whole thesis.

---
Slide 5 — Main Contributions

Speaker script:
The thesis makes four contributions. First, it studies tendon-driven systems at the mechanism level. Second, it develops a handheld surgical instrument as the first embodiment. Third, it extracts transferable design principles. Fourth, it demonstrates those principles in Lasso Gripper as the second embodiment.

---
Slide 6 — Thesis Roadmap

Speaker script:
This slide shows the roadmap of the thesis. I begin with the mechanism problem, then review related work. The first embodiment is the handheld surgical instrument, which is used to discover and validate mechanism principles. These principles are then transferred to the second embodiment, Lasso Gripper.

---
Slide 7 — Related Work: Surgical Instruments

Speaker script:
On the surgical side, cable-driven instruments recover distal dexterity while keeping actuators away from the tip. However, this comes with coupling, friction, hysteresis, and practical weight penalties. Many studies optimize one part of the system, but fewer address the overall mechanism tradeoff between dexterity, tension control, and ergonomic usability.

---
Slide 8 — Related Work: Adaptive Grasping

Speaker script:
On the grasping side, soft and enveloping designs improve shape adaptability, but many systems sacrifice reach, force transmission, or controllability. Traditional rigid-finger grippers are less effective for fragile, oversized, or highly variable targets. This motivates a loop-based and tension-driven strategy.

---
Slide 9 — Common Mechanism Principles

Speaker script:
These five principles unify the thesis. Tension management ensures predictable force transmission. Proximal actuation reduces distal mass. Differential routing enables compact multi-DOF behavior. Compliant interaction improves safety and adaptability.

---
Slide 10 — Embodiment 2: Lasso Gripper Concept

Speaker script:
The second embodiment is Lasso Gripper. Its inspiration comes from traditional capture tools such as the lasso and the uurga. The key idea is to use a controllable string loop as the primary grasping structure, so that capture is achieved through tension-driven closure rather than rigid fingertip contact.

---
Slide 11 — Lasso Gripper: Mechanical Design

Speaker script:
This slide shows the hardware of Lasso Gripper. The system includes dedicated launch and retraction subsystems. Friction wheels propel the string to form the loop, while a spool handles storage and retraction. Mechanically, the design focuses on fast deployment, reliable recovery, and stable tension.

---
Slide 12 — Lasso Gripper: Grasping Strategy

Speaker script:
Grasping in Lasso Gripper combines mechanism and planning. The system identifies suitable loop placement based on point cloud information and caging principles. After loop positioning, tightening is coordinated with approach motion, while feedback regulates the capture process.

---
Slide 13 — Lasso Gripper: Dynamics and Workspace

Speaker script:
To move beyond demonstration, the loop behavior also needs to be understood analytically. This part of the thesis models the string dynamics and estimates the workspace associated with the deployed configuration. The analysis connects geometric behavior, launch conditions, and practical capture capability.

---
Slide 14 — Lasso Gripper: Experimental Results

Speaker script:
These experiments validate Lasso Gripper across a range of scenarios. It successfully captures animal figures, irregular objects, oversized balloons, and moving targets. Together, these demonstrations show that the loop-based mechanism offers both broad capture tolerance and gentle interaction.

---
Slide 15 — Comparison with Conventional Grippers

Speaker script:
This comparison highlights why the mechanism matters. A conventional antipodal gripper applies concentrated stress to the target, which is problematic for delicate or highly deformable objects. In contrast, Lasso Gripper distributes contact through the loop.

---
Slide 16 — Mechanism Insights from Lasso Gripper

Speaker script:
The key outcome of Lasso Gripper is not only a new end-effector. It also provides transferable mechanism insights. Controlled tension improves repeatability, flexible contact improves tolerance to uncertainty, and proximal actuation with differential routing can be reused beyond grasping.

---
Slide 17 — Embodiment 1: Surgical Translation

Speaker script:
The first embodiment tests the same mechanism framework in a more constrained setting. In minimally invasive surgery, the instrument must be slender, precise, ergonomic, and safe. This makes tendon-driven actuation especially relevant, because it allows actuation to remain proximal while producing multi-DOF motion at the tip.

---
Slide 18 — Surgical Instrument: Design

Speaker script:
This slide summarizes the architecture of the handheld surgical instrument. The design combines proximal actuation, compact motor arrangement, dedicated reel architecture, and precise cable routing. The reel is especially important because it preserves bidirectional tension and reduces slack accumulation.

---
Slide 18b — 手术器械：历史版本演化

Speaker script:
本幻灯片展示手术器械从早期原型到当前版本的关键演化。每一轮迭代都针对早期问题（如张力管理、操控稳定性或体积）做出权衡和改进，最终形成当前的卷盘与紧凑马达布局架构。

---
Slide 19 — Surgical Instrument: Control and Validation

Speaker script:
The control system combines signal filtering and closed-loop motor feedback to improve motion fidelity in a hand-held setting. At this point, the connection between the two embodiments becomes clear. Lasso Gripper validates adaptive interaction under uncertainty, while the surgical instrument validates dexterity and controllability under clinical constraints.

---
Slide 20 — Conclusion and Future Work

Speaker script:
In conclusion, this thesis shows that tendon-driven mechanisms can be systematically designed as a transferable framework for adaptive grasping, dexterous manipulation, and safe interaction. Lasso Gripper and the handheld surgical instrument are two embodiments of that same idea. Future work will further improve adaptive control, modularity, and loop-based grasping in dynamic environments.
