## Project Overview

This project explores end-to-end reinforcement learning for robotic manipulation using MuJoCo.  
A simulated Fetch robot is trained to grasp and place objects at target locations using continuous control.

The agent is trained using Soft Actor-Critic (SAC) combined with Hindsight Experience Replay (HER) to address sparse reward challenges common in goal-conditioned manipulation tasks.

## Environment
- Simulator: MuJoCo
- Task: FetchPickAndPlace-v4 (Gymnasium Robotics)
- Observation: Robot state + achieved goal + desired goal
- Action Space: 4D continuous control (end-effector + gripper)

## Training
```bash
python -m training.train_rl
