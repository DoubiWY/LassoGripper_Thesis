# Reviewer Comments Summary for Supervisor Discussion

## Comment 1: Thesis Narrative, Abstract, and Lasso Gripper Contribution

- **Abstract motivation and clarity**
  - The reviewer felt that the abstract did not clearly explain the research problem, challenges, or purpose of the proposed designs.
  - **Revision made:** The abstract was rewritten to start from the broader problem of tendon-driven manipulation in constrained environments.
  - **Current status:** Addressed.

- **Abstract length**
  - The reviewer felt that the abstract was too long.
  - **Revision made:** The abstract was shortened and reorganized around motivation, two prototype embodiments, scope, and contributions.
  - **Current status:** Addressed.

- **Chapter-level summaries**
  - The reviewer recommended adding one- or two-paragraph summaries for each chapter.
  - **Revision made:** Chapter summaries were added to the main chapters using the `chaptersummary` environment.
  - **Current status:** Addressed.

- **Purpose of the Lasso Gripper chapter**
  - The reviewer questioned why the Lasso Gripper chapter was included and felt that it looked like a conceptual trial without clear results.
  - **Revision made:** The chapter now frames Lasso Gripper as the main mechanism embodiment for studying tendon-driven design rules, including design, actuation, sensing, control sequence, experiments, and mechanism-level insights.
  - **Current status:** Addressed.

- **Connection between Lasso Gripper and the surgical instrument**
  - The reviewer felt that the connection between the two systems was weak.
  - **Revision made:** The introduction, Lasso Gripper chapter, surgical instrument chapter, future work, and conclusions now present both systems as two embodiments of the same tendon-driven mechanism framework.
  - **Current status:** Addressed.

- **Novelty of Lasso Gripper**
  - The reviewer asked what makes the proposed gripper different from existing grippers.
  - **Revision made:** The related work and experimental chapters now emphasize large capture range, distributed contact, tolerance to positional uncertainty, rapid launch/retraction, and suitability for deformable or moving targets.
  - **Current status:** Addressed.

- **Comparison with existing grippers**
  - The reviewer requested at least a qualitative comparison with existing gripper designs.
  - **Revision made:** The thesis now compares Lasso Gripper qualitatively with antipodal grippers and loop/enveloping gripper literature. Chapter 6 includes demonstrations against a Robotiq 2F-140 gripper.
  - **Current status:** Addressed.

- **Writing quality and organization**
  - The reviewer criticized unclear section structure, missing titles, and weak writing.
  - **Revision made:** Chapter structures were reorganized, section titles clarified, and grammar/spelling were revised using American English.
  - **Current status:** Addressed.

- **Figure captions and formatting**
  - The reviewer noted awkward figure captions and formatting.
  - **Revision made:** Several captions were rewritten for clarity and grammar.
  - **Current status:** Partially addressed, because some line breaks are controlled automatically by LaTeX layout.

- **Overall thesis standard**
  - The reviewer felt the submitted version did not sufficiently demonstrate seriousness or research quality.
  - **Revision made:** The thesis now has a clearer unified narrative, explicit scope statements, chapter summaries, related work positioning, FEA, control logic, limitations, and future work.
  - **Current status:** Addressed.

## Comment 2: Surgical Instrument Justification, FEA, and Lasso Gripper Control Logic

- **Technical motivation for the handheld laparoscopic instrument**
  - The reviewer found the motivation reasonable but technically underdeveloped.
  - **Revision made:** The surgical instrument chapter now frames the device around clinical and engineering constraints: low distal mass, ergonomic balance, bidirectional tension transmission, packaging, safety, and tendon-driven dexterity.
  - **Current status:** Addressed.

- **Finite element analysis**
  - The reviewer noted that no FEA was provided for the proposed medical instrument.
  - **Revision made:** A dedicated FEA subsection was added for the jaw and middle base, including material, mesh size, boundary conditions, loading assumptions, maximum von Mises stress, and safety interpretation.
  - **Current status:** Addressed.

- **Motor selection justification**
  - The reviewer noted that the motor selection was not quantitatively justified.
  - **Revision made:** The thesis now reports motor mass, torque, feedback capability, and functional role for the selected Feetech servos.
  - **Current status:** Partially addressed. A full torque budget or actuator-sizing derivation could still be added if required.

- **Relationship between the medical instrument and Lasso Gripper**
  - The reviewer felt that the relationship between the two tendon-driven systems was insufficiently explained.
  - **Revision made:** The thesis now explicitly states that Lasso Gripper provides mechanism-level insights and that the handheld instrument translates those principles into a clinically constrained form factor.
  - **Current status:** Addressed.

- **Transition between the two systems**
  - The reviewer felt that the transition from Lasso Gripper to the surgical instrument was abrupt.
  - **Revision made:** Transition paragraphs were added in the introduction, Lasso Gripper implications section, surgical instrument opening section, and conclusions.
  - **Current status:** Addressed.

- **Experimental setup for Lasso Gripper**
  - The reviewer found the Lasso Gripper experimental setup unclear.
  - **Revision made:** Chapter 6 now includes objectives, setup, experimental procedure, data collection, representative demonstrations, and failure-mode discussion.
  - **Current status:** Addressed.

- **Grasping and release logic**
  - The reviewer asked how the gripper determines when to initiate grasping or release actions.
  - **Revision made:** Chapter 4 now clarifies that the demonstrated system uses a preprogrammed launch, approach, retraction, lift, and release sequence. It does not autonomously recognize objects or trigger grasping from visual feedback.
  - **Current status:** Addressed.

- **Sensing mechanisms**
  - The reviewer stated that internal or external sensing mechanisms were not clearly described.
  - **Revision made:** The revised text explains that tension sensing and motor-state feedback are used for monitoring and safety, while visual/point-cloud information is used for setup and interpretation rather than autonomous online grasp triggering.
  - **Current status:** Addressed.

- **Flowchart for grasping and release**
  - The reviewer requested a diagram or flowchart for the complete grasping/releasing process.
  - **Revision made:** Chapter 4 now includes a flowchart showing the sequence: Idle, Preset, Launch, Approach/Sweep, Retract/Tighten, Lift/Transport, Release, and Recovery.
  - **Current status:** Addressed.

- **Quantitative evaluation**
  - The reviewer noted that success rates, repeatability, and failure cases were not sufficiently reported.
  - **Revision made:** The thesis now explicitly states that the Lasso Gripper experiments are qualitative demonstrations. Representative outcomes and common failure modes are discussed, while large-sample statistics, repeatability studies, and fatigue tests are listed as future work.
  - **Current status:** Addressed with scope clarification.

- **Reason for omitting full statistical metrics**
  - The reviewer requested a rationale for the absence of full quantitative evaluation.
  - **Revision made:** The abstract, Lasso Gripper chapter summary, Chapter 6 data collection section, and discussion now explain the demonstration-focused scope.
  - **Current status:** Addressed.

## Remaining Items to Discuss With Supervisor

- Whether to add a short torque-budget calculation for motor selection.
- Whether the current LaTeX flowchart is sufficient or should be replaced with a more polished figure.
- Whether the qualitative-only experimental scope is acceptable, or if a small table of trial counts should be added.
