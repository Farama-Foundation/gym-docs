Amidar-ram-v0
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|Amidar-ram-v0|Discrete|(1,)|(0,1,...,9,)|(128,)|[(0,255),...,(0,255)]| |`from gym.envs.atari import environment`|
---

### Description
This game is similar to Pac-Man: You are trying to visit all places on a 2-dimensional grid while simultaneously avoiding
your enemies.

### Actions
Actions for default flavor:

| Num | Action                 |
|-----|------------------------|
| 0   | NOOP |
| 1   | FIRE |
| 2   | UP |
| 3   | RIGHT |
| 4   | LEFT |
| 5   | DOWN |
| 6   | UPFIRE |
| 7   | RIGHTFIRE |
| 8   | LEFTFIRE |
| 9   | DOWNFIRE |

### Arguments

```
env = gym.make("Amidar-ram-v0")
```

The various ways to configure the environment are described in the article on Atari environments.
It is possible to specify various flavors of the environment via the keyword arguments `difficulty` and `mode`. 
A flavor is a combination of a game mode and a difficulty setting.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|Amidar-ram-v0|1|2|

### Version History

* v0: Initial versions release (1.0.0)
