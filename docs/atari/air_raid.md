AirRaid-ram-v0
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|AirRaid-v0|Discrete|(1,)|(0,1,2,3,4,5,)|(250, 160, 3)|(0,255) in each entry| |`from gym.envs.atari import environment`|
---

### Description
You control a ship that can move sideways. You must protect two buildings (one on the right and one on the left side of the screen) from 
flying saucers that are trying to drop bombs on them.

### Actions
Actions for default flavor:

| Num | Action                 |
|-----|------------------------|
| 0   | NOOP |
| 1   | FIRE |
| 2   | RIGHT |
| 3   | LEFT |
| 4   | RIGHTFIRE |
| 5   | LEFTFIRE |


### Arguments

```
env = gym.make("AirRaid-v0")
```

The various ways to configure the environment are described in the article on Atari environments.
It is possible to specify various flavors of the environment via the keyword arguments `difficulty` and `mode`. 
A flavor is a combination of a game mode and a difficulty setting.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|AirRaid-v0|9|1|

### Version History

* v0: Initial versions release (1.0.0)
