# Defense Notes and Q&A

Title: `Tendon-Driven Mechanisms for Adaptive Robotic Grasping and Handheld Surgical Instruments`

## Part I. Slide-by-Slide Speaking Notes

### Slide 1. Title
- Define the thesis as a mechanism-centered study rather than two unrelated projects.
- State that the two systems are two embodiments of one tendon-driven framework.
- Mention that the focus is on adaptive grasping and surgical manipulation under shared mechanism constraints.

### Slide 2. Motivation
- Emphasize the shared constraints: narrow workspace, fragile or irregular targets, and low distal mass.
- Explain why tendon-driven systems are attractive: lightweight force transmission, remote actuation, and compliant interaction.
- Note that these advantages also bring challenges such as slack and hysteresis.

### Slide 3. Research Gap
- Existing work usually studies surgical tools and adaptive grippers separately.
- Most prior designs are application-driven rather than mechanism-driven.
- The missing piece is a transferable tendon-driven design framework.

### Slide 4. Research Question
- State the core question clearly.
- Frame the problem around adaptive, dexterous, and safe manipulation.
- Repeat the three key constraints: limited space, low distal inertia, and compliant contact.

### Slide 5. Main Contributions
- Contribution one: mechanism-level study of tendon-driven robotic systems.
- Contribution two: Lasso Gripper as the first embodiment.
- Contribution three: extraction of transferable design principles.
- Contribution four: translation to a handheld surgical instrument.

### Slide 6. Thesis Roadmap
- Explain the sequence: problem definition, related work, embodiment one, extracted principles, embodiment two, and conclusions.
- Remind the audience that the logic follows scientific structure, not project calendar order.

### Slide 7. Related Work: Surgical Instruments
- Existing cable-driven laparoscopic instruments improve distal dexterity.
- The main issues are coupling, friction, hysteresis, and added weight.
- Many studies optimize one subsystem, but fewer address the full mechanism tradeoff.

### Slide 8. Related Work: Adaptive Grasping
- Soft and enveloping grippers improve shape adaptability.
- Traditional rigid grippers struggle with fragile, oversized, and uncertain targets.
- This motivates a mechanism with both large capture range and controlled force transmission.

### Slide 9. Common Mechanism Principles
- Introduce the five recurring keywords: tension management, proximal actuation, differential routing, compliant interaction, and low distal inertia.
- Explain that both embodiments are analyzed with this same mechanism vocabulary.

### Slide 10. Embodiment 1: Lasso Gripper Concept
- Explain the inspiration from the lasso and the uurga.
- Stress that the string loop is the primary grasping structure, not just a transmission element.
- Highlight adaptive capture as the central idea.

### Slide 11. Lasso Gripper: Mechanical Design
- Describe the launch and retraction subsystems.
- Mention friction wheels, spool recovery, and controller integration.
- Emphasize the design goals: fast deployment, reliable recovery, and stable tension.

### Slide 12. Lasso Gripper: Grasping Strategy
- Present caging as a geometric perspective rather than a fully implemented autonomy pipeline.
- Clarify that the reported experiments used preplanned robot waypoints.
- Explain that loop tightening was triggered at predefined poses.
- State that this isolates mechanism performance from perception uncertainty.

### Slide 13. Lasso Gripper: Dynamics and Workspace
- Explain why the string loop must be modeled, not just demonstrated.
- Connect loop dynamics to workspace and capture behavior.
- Show that modeling supports both mechanism understanding and future control.

### Slide 14. Lasso Gripper: Experimental Results
- Summarize the four groups of demonstrations: static targets, irregular shapes, oversized targets, and moving targets.
- Emphasize adaptability and tolerance to uncertainty in size, shape, and motion.

### Slide 15. Comparison with Conventional Grippers
- Contrast distributed loop contact with concentrated antipodal contact.
- State that the main advantage appears in delicate, deformable, or shape-variable targets.
- Avoid claiming universal superiority; frame it as task-dependent advantage.

### Slide 16. Mechanism Insights from Lasso Gripper
- Controlled tension improves repeatability.
- Flexible contact improves tolerance to uncertainty.
- Proximal actuation reduces distal complexity.
- Differential routing is transferable beyond loop grasping.
- This slide is the bridge from embodiment one to embodiment two.

### Slide 17. Embodiment 2: Surgical Translation
- Explain that the second part is not a topic change, but a mechanism transfer.
- The goal shifts from adaptive capture to distal dexterity and control fidelity.
- Clinical constraints are stricter in geometry, ergonomics, safety, and repeatability.

### Slide 18. Surgical Instrument: Design
- Introduce compact actuation layout, cable routing, reel architecture, and quick-swap mechanism.
- Stress that the reel structure is important for preserving stable tendon tension.
- Emphasize low distal mass and handheld usability.

### Slide 19. Surgical Instrument: Control and Validation
- Explain the sensing, filtering, and closed-loop control structure.
- State that the instrument validates the same tendon-driven principles under tighter constraints.
- Reinforce that the two embodiments test one framework in two operating regimes.

### Slide 20. Conclusion and Future Work
- Conclude that the thesis contributes a transferable tendon-driven mechanism framework.
- State that it is validated in both adaptive grasping and surgical manipulation.
- Mention future work: adaptive calibration, modularity, multi-loop grasping, and more autonomous deployment.

## Part II. Standard Q&A

### Q1. 你的 thesis 到底是两个项目，还是一篇连续工作？
**A**
- 它是一篇连续工作，但连续性在 mechanism level，而不是 product level。
- 两部分共享同一组机制问题：tension management、proximal actuation、differential routing、compliant interaction 和 low distal inertia。
- Lasso Gripper 是第一 embodiment，用于发现和验证这些原则；surgical instrument 是第二 embodiment，用于在更严格约束下转译和验证这些原则。

### Q2. 为什么这两个应用差别这么大，还能放在同一篇 thesis 里？
**A**
- 因为 thesis 的主语不是应用领域，而是 tendon-driven mechanisms。
- 两个系统面对不同任务，但依赖相同机制逻辑。
- 一个验证 adaptive interaction，另一个验证 dexterous distal control。

### Q3. Lasso Gripper 的 novelty 到底是什么？
**A**
- novelty 不只是“有一个绳圈”，而是把 flexible tensile element 从 transmission element 变成 primary grasping structure。
- 通过 controllable launch-and-retraction，实现 adaptive capture 和 distributed contact。
- 再加上 robotic execution、mechanism analysis 和实验验证，构成完整的机制创新。

### Q4. 你为什么不用 success rate 来强调性能？
**A**
- 因为这部分工作的目标是 mechanism validation，而不是完整 autonomous grasping benchmark。
- 实验重点是验证 capture adaptability、distributed contact 和 secure holding capability。
- 如果未来扩展到 perception-driven autonomy，再做更系统的 benchmark 会更合理。

### Q5. caging 那一部分是不是实际用于在线定位和规划？
**A**
- 不是。
- caging 在这篇 thesis 里是 geometric perspective，不是最终实验 pipeline 的 online perception module。
- 实际实验中机械臂沿预设路径点运动，并在预定义姿态触发收紧。

### Q6. 既然没有在线定位，为什么还保留 caging 分析？
**A**
- 因为它仍然提供 loop placement 的几何解释。
- 它为 future autonomous deployment 提供理论框架。
- 问题不在于保留它，而在于必须明确它不是 fully implemented autonomy。

### Q7. 为什么不用 parallel gripper 或 soft gripper，而要做 Lasso Gripper？
**A**
- parallel gripper 在 fragile、oversized、irregular targets 上受 opening width 和集中接触限制。
- soft gripper 有较好适应性，但常牺牲 workspace、speed 或 force transmission。
- Lasso Gripper 试图覆盖两者之间的空白，尤其适合 uncertain、large、or moving targets。

### Q8. surgical instrument 和 Lasso Gripper 的联系最核心的一点是什么？
**A**
- 最核心的是 proximal actuation 加 controlled tendon routing。
- Lasso Gripper 证明了 tension-driven mechanism 可以实现 adaptive interaction。
- surgical instrument 证明相同机制逻辑可以在临床约束下实现 distal dexterity。

### Q9. surgical instrument 的主要工程挑战是什么？
**A**
- 在 handheld form factor 下保持 low distal mass。
- 通过 reel 和 routing 结构维持稳定张力并减少 slack。
- 通过 sensing 和 control 提升 motion fidelity 并抑制扰动。

### Q10. 这篇 thesis 最大的局限是什么？
**A**
- 两个 embodiment 都仍处于 prototype validation 阶段。
- Lasso Gripper 还没有形成完整 autonomy pipeline。
- surgical instrument 也还没有进入更严格的 phantom、ex vivo 或 clinical-style evaluation。

### Q11. 下一步最重要的工作是什么？
**A**
- 对 Lasso Gripper，是 perception-driven loop placement 和 multi-loop extension。
- 对 surgical instrument，是 adaptive calibration、learning-based compensation 和更智能的 modular end-effectors。

### Q12. 如果老师说两部分还是有点松散，你怎么回应？
**A**
- 我会把讨论重新拉回 mechanism level。
- 我不会强调“做了两个机器人”，而会强调“研究了一套 tendon-driven design framework，并在两类约束条件下验证”。
- 这才是 thesis 的连续性所在。

## Part III. Sharp Q&A

### Q1. 你这篇 thesis 本质上还是两个不相关项目拼在一起，为什么说它是连续工作？
**A**
- 如果按应用场景看，它们确实属于不同任务；但 thesis 的主语不是应用，而是 tendon-driven mechanism。
- 两部分共享同一组机制问题：tension management、proximal actuation、differential routing、compliant interaction 和 low distal inertia。
- Lasso Gripper 用来发现和验证这些原则，surgical instrument 用来在更强约束下转译和验证这些原则，所以连续性是在 mechanism level，而不是 product level。

### Q2. 你是不是事后才把两部分硬解释成一个 framework？
**A**
- 从项目发生顺序上，两个系统确实不是作为同一个产品线开发的。
- 但 thesis 组织遵循的是 scientific logic，而不是 calendar order。
- 评审 thesis 看的是你是否提出统一研究问题并给出可辩护的机制结论，而不是项目时间线是否线性。

### Q3. 为什么 Lasso Gripper 能代表 tendon-driven mechanisms，而不是一个特殊的绳圈玩具？
**A**
- 因为我不是把它当成单一产品，而是把它当成 mechanism study platform。
- 它具体体现了张力维持、柔顺接触、远端低复杂度和 flexible element routing 等普适问题。
- 我提炼的原则并不依赖 loop 这一单一形态。

### Q4. 你的 Lasso Gripper 真正的新意是什么？“用绳子套住东西”并不新。
**A**
- 单纯“用绳子”当然不新。
- 新意在于把 controllable launch-and-retraction、adaptive capture region、tension-regulated closure 和 robotic execution 组合成一个可重复的 tendon-driven grasping mechanism。
- novelty 在 mechanism reconstruction，而不是在传统工具的表面形象。

### Q5. 你的 grasping 部分没有严格 success rate，没有 benchmark，这样结论是不是很弱？
**A**
- 如果 thesis 目标是完整 autonomous grasping benchmark，这个批评成立。
- 但本文的目标是 mechanism validation，而不是 perception-and-benchmark competition。
- 因此我把结论限定在 mechanism feasibility、representative validation 和 transferable design principles 上。

### Q6. 你在 caging 那部分是不是暗示做了 perception-based localization，但实际上没有？
**A**
- 实际上没有在线定位，这一点我会明确承认。
- caging 在这篇 thesis 中是 geometric perspective，不是最终实验 pipeline 的 online perception module。
- 实验中机械臂使用预设路径点，在特定姿态收紧绳圈，这是为了控制变量。

### Q7. 如果 caging 没有真正落地，那这一节是不是应该删掉？
**A**
- 我认为不应该删，但必须严格界定其角色。
- 它不是 implemented autonomy，而是 conceptual placement framework。
- 它的价值在于为 loop placement 提供几何解释，并为 future autonomous deployment 提供理论起点。

### Q8. 既然没有在线定位，为什么不直接手动抓，为什么还要机械臂预设路径？
**A**
- 因为目标不是手工演示，而是 controlled robotic execution。
- 预设路径比完全手动操作更能保证实验一致性。
- 同时又避免把感知误差混进机制评价里。

### Q9. 你的 Lasso Gripper 和 soft gripper 相比，真正优势是什么？
**A**
- soft gripper 在局部贴合上更自然，但 often sacrifices workspace、force transmission 或 deployment speed。
- Lasso Gripper 的优势是把 large capture range、distributed contact 和 tension-based holding 结合起来。
- 它特别适合 oversized、uncertain 或 moving targets。

### Q10. 你的 Lasso Gripper 和 conventional antipodal gripper 比，最大 tradeoff 是什么？
**A**
- 最大 tradeoff 是 precision versus tolerance。
- antipodal grippers 在规则几何和精确 pose control 下更直接、更成熟。
- Lasso Gripper 在 target uncertainty、shape variability 和 gentle contact 上更有优势。

### Q11. 你为什么认为从 Lasso Gripper 能自然走到 laparoscopic instrument？这不是跳得太远了吗？
**A**
- 如果从 application 看，这是跨域；如果从 mechanism 看，这个跳转是合理的。
- 两者都依赖 tensile element routing、proximal actuation、tension preservation 和 low distal inertia。
- Lasso Gripper 强调 adaptive interaction，surgical instrument 强调 dexterous distal control，它们是同一机制族的两个实例。

### Q12. surgical instrument 这一部分更像工程设计堆砌，机制创新在哪里？
**A**
- 这部分的价值不在于单个零件新，而在于 mechanism translation。
- 我把在 Lasso Gripper 中提炼出的 tendon-driven principles 转化成手持式 surgical device 的结构与控制架构。
- 它验证的是这些原则在严格医疗约束下是否仍成立。

### Q13. 你的 surgical instrument 没有临床实验，也没有 ex vivo 或 in vivo 验证，凭什么说它对 surgery 有意义？
**A**
- 我不会把它表述成 clinical readiness，而是 mechanism-level feasibility for surgical manipulation。
- 它的意义在于证明 tendon-driven architecture 可以在 handheld form factor 下实现 distal dexterity、tension-preserving transmission 和 controlled operation。
- 临床相关验证显然是下一阶段工作，不属于这篇 thesis 的完成范围。

### Q14. 你如何证明 surgical instrument 的设计原则真的来自 Lasso Gripper，而不是事后总结？
**A**
- 我能证明的不是历史因果，而是逻辑 transferability。
- 我不是声称每个零件都直接从 Lasso 进化而来，而是论证两者共享的设计原则是可转移的。
- thesis 的有效性依赖的是 mechanism argument 是否自洽，而不是项目历史是否线性演化。

### Q15. 如果去掉 surgical instrument，这篇 thesis 还成立吗？
**A**
- 作为一篇关于 Lasso Gripper 的 thesis，它仍然可以成立。
- 但会失去 transferable framework 这个更强的论点。
- surgical instrument 的价值在于证明这些 tendon-driven principles 可以跨任务迁移。

### Q16. 如果去掉 Lasso Gripper，只保留 surgical instrument，这篇 thesis 会更聚焦吗？
**A**
- 会更聚焦于 medical device engineering，但会失去 mechanism discovery 这一层。
- Lasso Gripper 把 tendon-driven interaction 中最核心、最容易观察的机制问题放到了更开放、更可分析的系统里。
- 这使后面的 surgical translation 不只是工程拼装。

### Q17. 你一直强调 transferable framework，那你的 framework 到底是什么，不要只给关键词。
**A**
- 可以具体概括成四步。
- 第一步，明确 task constraint 和 desired interaction mode。
- 第二步，设计 tendon routing and actuation topology to preserve controllable tension。
- 第三步，用 proximal actuation and low distal complexity 满足 inertia and packaging constraints。
- 第四步，用 task-specific contact geometry，例如 loop capture 或 distal articulation，去实现目标功能。

### Q18. 你的实验大多是 demonstration，缺乏 statistical rigor，这会不会影响 thesis 说服力？
**A**
- 会影响我能声称的强度，所以我不会把结论说得比证据更大。
- 我把结论限定在 mechanism feasibility、representative validation 和 transferable design principles 上。
- 对 prototype-stage mechanism thesis，这个证据层级是可以辩护的，但更系统的 statistics 会进一步增强说服力。

### Q19. 你的最大技术风险在哪里？
**A**
- 对 Lasso Gripper，最大风险是 perception and deployment uncertainty 一旦进入 closed-loop autonomy，性能可能与 controlled trials 不同。
- 对 surgical instrument，最大风险是 cable stretch、hysteresis 和 long-term repeatability 可能限制精度。
- 两部分未来都需要更强的 calibration and closed-loop compensation。

### Q20. 如果评审认为你的 thesis 不够“深”，你怎么回应？
**A**
- 我会把“深度”重新界定到 mechanism abstraction 上，而不是某一个 benchmark 指标。
- 本文的深度不在于把某个单项性能做到极限，而在于从两个不同系统中抽象出统一的 tendon-driven design logic，并证明它可以跨任务迁移。
- 这是一篇 mechanism-oriented integrative thesis，而不是单一系统 benchmark thesis。

### Q21. 如果让你重做这篇 thesis，你最会补哪一块？
**A**
- 第一，给 Lasso Gripper 增加 perception-driven loop placement 和更系统的 quantitative benchmark。
- 第二，给 surgical instrument 增加更严格的 task-based validation，例如 phantom or ex vivo style evaluation。
- 这样可以把目前的 mechanism thesis 向更完整的 system thesis 再推进一步。
