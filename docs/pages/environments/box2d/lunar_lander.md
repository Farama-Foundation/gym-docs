---
layout: "env"
title: LunarLander-v2
---

|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|LunarLander-v2||| |||| |`from gym.envs.box2d.lunar_lander import LunarLander`|

### Description
This environment is a classic rocket trajectory optimization problem.
According to Pontryagin's maximum principle, it is optimal to fire the engine at full throttle or turn it off. This is the reason why this environment has discreet actions: engine on or off.

The landing pad is always at coordinates (0,0). The coordinates are the first two numbers in the state vector.
Landing outside the landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land
on its first attempt.

To see a heuristic landing, run:
```
python gym/envs/box2d/lunar_lander.py
```
<!-- To play yourself, run: -->
<!-- python examples/agents/keyboard_agent.py LunarLander-v2 -->

![LunarLander Episode Example](./lunar_lander.jpg)

### Action Space
Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine.

### Observation Space

### Rewards
Reward for moving from the top of the screen to the landing pad and zero speed is about 100..140 points.
If the lander moves away from the landing pad it loses reward.
If the lander crashes, it receives an additional -100 points. If it comes to rest, it receives an additional +100 points. Each leg with ground contact is +10 points.
Firing the main engine is -0.3 points each frame. Firing the side engine is -0.03 points each frame. Solved is 200 points.

### Starting State

### Episode Termination
The episode finishes if the lander crashes or comes to rest.

### Arguments

### Version History

### References
