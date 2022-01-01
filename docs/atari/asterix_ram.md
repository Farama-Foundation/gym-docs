Asterix-ram-v0
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|Asterix-ram-v0|Discrete|(1,)|(0,1,...,8,)|(128,)|[(0,255),...,(0,255)]| |`from gym.envs.atari import environment`|
---

### Description
You are Asterix and can move horizontally (continuously) and vertically (discretely). Two types of objects
move horizontally across the screen: lyres and bowls (presumably filled with the magic potion!). Your goal is to guide 
Asterix in such a way as to avoid lyres and collect as much magic potion as possible.

### Actions
Actions for default flavor:

| Num | Action                 |
|-----|------------------------|
| 0   | NOOP |
| 1   | UP |
| 2   | RIGHT |
| 3   | LEFT |
| 4   | DOWN |
| 5   | UPRIGHT |
| 6   | UPLEFT |
| 7   | DOWNRIGHT |
| 8   | DOWNLEFT |


### Arguments

```
env = gym.make("Asterix-ram-v0")
```

The various ways to configure the environment are described in the article on Atari environments.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|Asterix-ram-v0|1|1|

### Version History

* v0: Initial versions release (1.0.0)
