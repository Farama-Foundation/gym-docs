Assault-ram-v0
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|Assault-v0|Discrete|(1,)|(0,...,6,)|(250, 160, 3)|(0,255) in each entry| |`from gym.envs.atari import environment`|
---

### Description
You control a vehicle that can move sideways. A big mother ship circles overhead and continually deploys smaller drones.
You must destroy these enemies and dodge their attacks.

### Actions
Actions for default flavor:

| Num | Action                 |
|-----|------------------------|
| 0   | NOOP |
| 1   | FIRE |
| 2   | UP |
| 3   | RIGHT |
| 4   | LEFT |
| 5   | RIGHTFIRE |
| 6   | LEFTFIRE |

### Arguments

```
env = gym.make("Assault-v0")
```

The various ways to configure the environment are described in the article on Atari environments.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|Assault-v0|1|1|

### Version History

* v0: Initial versions release (1.0.0)
