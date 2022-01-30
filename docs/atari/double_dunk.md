 ALE/DoubleDunk-v5
---
|Title|Action Type|Action Shape|Action Values|Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------| ----------- | -----------| ----------- | -----------|
|ALE/DoubleDunk-v5|Discrete|(1,)|(0,1,...,17)|(250, 160, 3)|(0,255) in each entry| |`from gym.envs.atari import environment`|
---

### Description
You are playing a 2v2 game of basketball. At the start of each possession, you select between a set
of different plays and then execute them to either score or prevent your rivals from scoring. The
game lasts a set amount of time or until one of the teams reaches a certain score

Detailed documentation can be found on [the AtariAge page](https://atariage.com/manual_html_page.php?SoftwareLabelID=153).

### Actions
By default, all actions that can be performed on an Atari 2600 are available in this environment.
However, if you use v0 or v4 or specify `full_action_space=False` during initialization, only a reduced
number of actions (those that are meaningful in this game) are available. The reduced action space may depend
on the flavor of the environment (the combination of `mode` and `difficulty`). The reduced action space for the default 
flavor looks like this:

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

### Observations
By default, the environment returns the RGB image that is displayed to human players as an observation. However, it is
possible to observe
- The 128 Bytes of RAM of the console
- A grayscale image

instead. The respective observation spaces are
- `Box([0 ... 0], [255 ... 255], (128,), uint8)`
- `Box([[0 ... 0]
 ...
 [0  ... 0]], [[255 ... 255]
 ...
 [255  ... 255]], (250, 160), uint8)
`

respectively. The general article on Atari environments outlines different ways to instantiate corresponding environments
via `gym.make`.

### Rewards
Scores follow the rules of basketball. You can get either 3 points, 2 points foul line) gqdepending
from where you shoot. After a defensive foul, a successful shot from the foul line gives you 1
point.

### Arguments

```
env = gym.make("ALE/DoubleDunk-v5")
```

The various ways to configure the environment are described in detail in the article on Atari environments.

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|DoubleDunk|16|1|

You may use the suffix "-ram" to switch to the RAM observation space. In v0 and v4, the suffixes "Deterministic" and "Noframeskip" 
are available. These are no longer supported in v5. In order to obtain equivalent behavior, pass keyword arguments to `gym.make` as outlined in 
the general article on Atari environments.
The versions v0 and v4 are not contained in the "ALE" namespace. I.e. they are instantiated via `gym.make("DoubleDunk-v0")`.

### Version History
A thorough discussion of the intricate differences between the versions and configurations can be found in the
general article on Atari environments. 

* v5: Stickiness was added back and stochastic frameskipping was removed. The entire action space is used by default. The environments are now in the "ALE" namespace.
* v4: Stickiness of actions was removed
* v0: Initial versions release (1.0.0)
