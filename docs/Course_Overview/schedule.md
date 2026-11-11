# 31-session schedule

The classroom sequence consists of **31 two-hour sessions (62 contact hours)**. Plan approximately **62 additional hours for independent project development** alongside instruction. Semester dates, holidays, submission deadlines, and evaluation times are announced in Microsoft Teams.

Project milestones guide work outside class. Sessions 17 and 31 are project evaluations; sessions 27–30 remain instructional sessions.

## M0 — Robotics Fundamentals and ROS 2

| Session | Topic |
|---:|---|
| 1 | Introduction to robotics: DOF, robot classification, joint and Cartesian space, workspace, and constraints |
| 2 | Essential ROS 2: nodes, topics, services, TF, terminal tools, and modifying an existing Python node |

Complete software preparation before session 2 using [resources and preparation](T0_3.md). Extended package and launch-file construction remains reference material.

## M1 — Manipulator Kinematics

| Session | Topic | Project connection |
|---:|---|---|
| 3 | Coordinate frames, rotation matrices, and homogeneous transformations | |
| 4 | Forward kinematics and Denavit–Hartenberg parameters | Project 1 released |
| 5 | Analytical and numerical inverse kinematics | |
| 6 | Geometric Jacobians, differential kinematics, and singularities | |
| 7 | Robot models, URDF, TF, RViz, and physical verification | Design and kinematic model milestone |

## M2 — Robot Dynamics and Control

| Session | Topic | Project connection |
|---:|---|---|
| 8 | Robot dynamics: forces, torques, inertia, and energy | |
| 9 | Manipulator dynamic models: mass matrix, Coriolis/centrifugal terms, and gravity | |
| 10 | Joint feedback control: PID/PD, transient response, and tracking errors | Actuators, feedback, and basic positioning milestone |
| 11 | Model-based control, gravity compensation, feedforward, and disturbances | |
| 12 | Actuator constraints, position/velocity/effort interfaces, and ros2_control | |
| 13 | Experimental controller validation, performance measurements, and limitations | Joint control and IK milestone |

## M3 — Trajectory Planning

| Session | Topic | Project connection |
|---:|---|---|
| 14 | Motion profiles: trapezoidal, triangular, and smooth polynomial trajectories | |
| 15 | Joint-space trajectories, synchronization, velocity, and acceleration constraints | |
| 16 | Cartesian trajectories, inverse kinematics, and Jacobian-based motion | Trajectory execution and experimental evidence milestone |
| 17 | Manipulator project demonstration and evaluation | Project 1 final evaluation |

## M4 — Mobile Robot Kinematics and Control

| Session | Topic | Project connection |
|---:|---|---|
| 18 | Differential-drive, Ackermann, and Mecanum kinematics | Project 2 released |
| 19 | Odometry, state estimation, coordinate transformations, and integration errors | |
| 20 | Path following: heading error, cross-track error, PID, and Pure Pursuit | |
| 21 | Mobile simulation and comparison with physical performance | Chassis, propulsion, steering/wheel control milestone |
| 22 | Navigation architectures, Nav2, planners, controllers, and costmaps | |

## M5 — Perception and Autonomous Navigation

| Session | Topic | Project connection |
|---:|---|---|
| 23 | Computer vision, camera geometry, calibration, OpenCV, and ArUco | |
| 24 | RGB-D sensing, 3D coordinate estimation, point clouds, and transformations | Odometry, path following, and sensor acquisition milestone |
| 25 | LiDAR, LaserScan, occupancy grids, SLAM, and mapping | |
| 26 | Perception, localization, obstacle detection, and autonomous navigation integration | |

## M6 — System Integration and Validation

| Session | Topic | Project connection |
|---:|---|---|
| 27 | Autonomous system architecture, functional requirements, and interfaces | Autonomous behavior and navigation integration milestone |
| 28 | Perception-to-control integration and autonomous behavior | |
| 29 | Experimental validation, repeatability, and performance analysis | Validation and performance measurements milestone |
| 30 | Reliability, fault handling, safety, and verification methodologies | Reliability and submission readiness milestone |

## Final evaluation

| Session | Topic |
|---:|---|
| 31 | Autonomous mobile robot demonstration and individual technical defense |

All teams demonstrate Project 2 on the same date. Evaluation scheduling may extend beyond the normal two-hour period to accommodate the demonstrations and defenses.

## Finding teaching material

Existing references are available for fundamentals, kinematics, trajectories, mobile models, and simulation/navigation. Dedicated dynamics/control, perception, and integration lessons are not yet complete. The instructor will identify the material and activities assigned for each session as those segments are reviewed.

[← Syllabus](T0_1.md) · [Next: Project roadmap →](roadmap.md)
