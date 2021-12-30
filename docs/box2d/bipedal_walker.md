BipedalWalker-v2
---
|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|BipedalWalker-v2||| |||| |`from gym.envs.box2d.bipedal_walker import BipedalWalker`|

---

### Description
Reward is given for moving forward, total 300+ points up to the far end. If the robot falls, it gets -100. Applying motor torque costs a small amount of points, more optimal agent will get better score. State consists of hull angle speed, angular velocity, horizontal speed, vertical speed, position of joints and joints angular speed, legs contact with ground, and 10 lidar rangefinder measurements. There's no coordinates in the state vector.


![BipedalWalker Episode Example](./bipedal_walker.jpg)

### Action Space

### Observation Space

### Rewards

### Starting State

### Episode Termination

### Arguments

### Version History

### References
