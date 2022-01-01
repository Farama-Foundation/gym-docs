Alien-ram-v0
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|Alien-ram-v0|Discrete|(1,)|(0,1,...,17,)|(128,)|[(0,255),...,(0,255)]| |`from gym.envs.atari import environment`|
---

### Description
You are stuck in a maze-like space ship with three aliens. You goal is to destroy their eggs that are scattered
all over the ship while simultaneously avoiding the aliens (they are trying to kill you). You have a flamethrower that can help you turn 
them away in tricky situations. Moreover, you can occasionally collect a power-up that gives you the temporary ability to kill aliens.


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
| 6   | UPRIGHT |
| 7   | UPLEFT |
| 8   | DOWNRIGHT |
| 9   | DOWNLEFT |
| 10   | UPFIRE |
| 11   | RIGHTGFIRE |
| 12   | LEFTFIRE |
| 13   | DOWNFIRE |
| 14   | UPRIGHTFIRE |
| 15   | UPLEFTFIRE |
| 16   | DOWNRIGHTFIRE |
| 17   | DOWNLEFTFIRE |

### Arguments

```
env = gym.make("Alien-ram-v0")
```

The various ways to configure the environment are described in the article on Atari environments.
It is possible to specify various flavors of the environment via the keyword arguments `difficulty` and `mode`. 
A flavor is a combination of a game mode and a difficulty setting.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|Alien-ram-v0|4|4|

### Version History

* v0: Initial versions release (1.0.0)
