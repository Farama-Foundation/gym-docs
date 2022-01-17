---
layout: env
title: BipedalWalker-v2
action-type: Discrete
agents: "2"
manual-control: "No"
action-shape: "(1,)"
action-values: "[0,17]"
observation-shape: "(210, 160, 3)"
observation-values: "(0,255)"
import: "from gym.envs.box2d.bipedal_walker import BipedalWalker"
---
<!-- TODO: fix the front matter info; its wrong -->

### Description
This is simple 4-joints walker robot environment.
There are two versions:
- Normal, with slightly uneven terrain.
- Hardcore with ladders, stumps, pitfalls.

To solve the game you need to get 300 points in 1600 time steps.
To solve hardcore version you need 300 points in 2000 time steps.

Heuristic is provided for testing, it's also useful to get demonstrations to learn from. To run heuristic:
```
python gym/envs/box2d/bipedal_walker.py
```

![BipedalWalker Episode Example](./bipedal_walker.jpg)

### Action Space

### Observation Space
State consists of hull angle speed, angular velocity, horizontal speed, vertical speed, position of joints and joints angular speed, legs contact with ground, and 10 lidar rangefinder measurements. There's no coordinates in the state vector.

### Rewards
Reward is given for moving forward, total 300+ points up to the far end. If the robot falls, it gets -100. Applying motor torque costs a small amount of points, more optimal agent will get better score.

### Starting State

### Episode Termination

### Arguments

### Version History

### References
