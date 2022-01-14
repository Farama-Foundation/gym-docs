---
layout: "links"
title: CarRacing-v0
---

|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|CarRacing-v0||| |||| |`from gym.envs.box2d.car_racing import CarRacing`|


### Description
Easiest continuous control task to learn from pixels, a top-down racing environment. Discreet control is reasonable in this environment as well, on/off discretisation is fine. State consists of 96x96 pixels. Reward is -0.1 every frame and +1000/N for every track tile visited, where N is the total number of tiles in track. For example, if you have finished in 732 frames, your reward is 1000 - 0.1*732 = 926.8 points. Episode finishes when all tiles are visited. Some indicators shown at the bottom of the window and the state RGB buffer. From left to right: true speed, four ABS sensors, steering wheel position, gyroscope.


![CarRacing Episode Example](./car_racing.jpg)

### Action Space

### Observation Space

### Rewards

### Starting State

### Episode Termination

### Arguments

### Version History

### References
