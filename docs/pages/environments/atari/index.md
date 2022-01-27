---
layout: env_selection
title: Atari
---

Atari environments are simulated via the Arcade Learning Environment (ALE) [[1]](#1). 
### Action Space
The action space a subset of the following discrete set of legal actions:

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

If you use v0 or v4 and the environment is initialized via `make`, the action space will usually be much smaller since most legal actions don't have
any effect. Thus, the enumeration of the actions will differ. The action space can be expanded to the full 
legal space by passing the keyword argument `full_action_space=True` to `make`.

The reduced action space of an Atari environment may depend on the flavor of the game. You can specify the flavor by providing 
the arguments `difficulty` and `mode` when constructing the environment. This documentation only provides details on the
action spaces of default flavors. 

### Observation Space
The observation issued by an Atari environment may be:
- the RGB image that is displayed to a human player,
- a grayscale version of that image or
- the state of the 128 Bytes of RAM of the console.

### Rewards
The exact reward dynamics depend on the environment and are usually documented in the game's manual. You can
find these manuals on [AtariAge](https://atariage.com/).

### Stochasticity
It was pointed out in [[1]](#1) that Atari games are entirely deterministic. Thus, agents could achieve 
state of the art performance by simply memorizing an optimal sequence of actions while completely ignoring observations from the environment.
To avoid this, ALE implements sticky actions: Instead of always simulating the action passed to the environment, there is a small
probability that the previously executed action is used instead.

On top of this, Gym implements stochastic frame skipping: In each environment step, the action is repeated for a random
number of frames. This behavior may be altered by setting the keyword argument `frameskip` to either a positive integer or 
a tuple of two positive integers. If `frameskip` is an integer, frame skipping is deterministic, and in each step the action is 
repeated `frameskip` many times. Otherwise, if `frameskip` is a tuple, the number of skipped frames is chosen uniformly at 
random between `frameskip[0]` (inclusive) and `frameskip[1]` (exclusive) in each environment step.

### Flavors
Some games allow the user to set a difficulty level and a game mode. Different modes/difficulties may have different
game dynamics and (if a reduced action space is used) different action spaces. We follow the convention of [[2]](#2) and
refer to the combination of difficulty level and game mode as a flavor of a game. The following table from [[2]](#2) shows
the number of available modes and difficulty levels for different Atari games:

|Title|# Modes|# Difficulties|
| ----------- | ----------- | -----------|
|AirRaid|9|1|       # Not mentioned in paper
|Alien|4|4|
|Amidar|1|2|
|Assault|1|1|
|Asterix|1|1|
|Asteroids|32|1|
|Atlantis|4|1|
| BankHeist | 1       | 4              |
| BattleZone | 4       |1|
| BeamRider | 1       | 2              |
| Berzerk | 10      |1|
| Bowling | 1       | 2              |




### Common Arguments
When initializing Atari environments via `gym.make`, you may pass some additional arguments. These work for any 
Atari environment. However, legal values for `mode` and `difficulty` depend on the environment.


`mode`: `int`. Game mode, see [[2]](#2). Legal values are in {0, ..., **# Modes** - 1}.

`difficulty`: `int`. Difficulty of the game, see [[2]](#2).. Legal values are in {0, ..., **# Difficulties** - 1}.
Together with `mode`, this determines the "flavor" of the game.

`obs_type`: `str`. This argument determines what observations are returned by the environment:
- "ram": The 128 Bytes of RAM are returned
- "rgb": An RGB rendering of the game is returned
- "grayscale": A grayscale rendering is returned

`frameskip`: `int` or a tuple of two `int`s. This argument controls stochastic frame skipping, as described in the section on stochasticity.

`repeat_action_probability`: `float`. The probability that an action sticks, as described in the section on stochasticity.

`full_action_space`: `bool`. If set to `True`, the action space consists of all legal actions on the console. Otherwise, the
action space will be reduced to a subset.

`render_mode`: `str`. Specifies the rendering mode:
- "human": We'll interactively display the screen and enable game sounds. This will lock emulation to the ROMs specified FPS
- "rgb_array": we'll return the `rgb` key in step metadata with the current environment RGB frame.
> It is highly recommended to specify `render_mode` during construction instead of calling `env.render()`. 
> This will guarantee proper scaling, audio support, and proper framerates


### Version History and Naming Schemes
All Atari games are available in three versions. They differ in the default settings of the arguments above.
The differences are listed in the following table:

|Version|`frameskip=`|`repeat_action_probability=`|`full_action_space=`|
| ----- | --------- | ------------------------- | ---------|
|v0     |`(2, 5,)`  |`0.25`                     |`False`     |
|v4     |`(2, 5,)`  |`0.0`                      |`False`     |
|v5     |`5`        |`0.25`                     |`True`      |

> Version v5 follows the best practices outlined in [[2]](#2). Thus, it is recommended to transition to v5 and
> customize the environment using the arguments above, if necessary.

For each Atari game, several different configurations are registered in OpenAI Gym. The naming schemes are analgous for
v0 and v4. Let us take a look at all variations of Amidar-v0 that are registered with OpenAI gym:

|Name                          |`obs_type=`|`frameskip=`|`repeat_action_probability=`|`full_action_space=`|
| ---------------------------- | -------- | --------- | ------------------------- | ----------------- |
|Amidar-v0                     |`"rgb"`   |`(2, 5,)`  |`0.25`                     |`False`            |
|AmidarDeterministic-v0        |`"rgb"`   |`4`        |`0.0`                      |`False`            |
|AmidarNoframeskip-v0          |`"rgb"`   |`1`        |`0.25`                     |`False`            |
|Amidar-ram-v0                 |`"ram"`   |`(2, 5,)`  |`0.25`                     |`False`            |
|Amidar-ramDeterministic-v0    |`"ram"`   |`4`        |`0.0`                      |`False`            |
|Amidar-ramNoframeskip-v0      |`"ram"`   |`1`        |`0.25`                     |`False`            |

Things change in v5: The suffixes "Deterministic" and "Noframeskip" are no longer available. Instead, you must specify the
environment configuration via arguments passed to `gym.make`. Moreover, the v5 environments
are in the "ALE" namespace. The suffix "-ram" is still available. Thus, we get the following table:

|Name                          |`obs_type=`|`frameskip=`|`repeat_action_probability=`|`full_action_space=`|
| ---------------------------- | -------- | --------- | ------------------------- | ----------------- |
|ALE/Amidar-v5                 |`"rgb"`   |`5`        |`0.25`                     |`True`             |
|ALE/Amidar-ram-v5             |`"ram"`   |`5`        |`0.25`                     |`True`             |

### References
<a id="1">[1]</a> 
MG Bellemare, Y Naddaf, J Veness, and M Bowling.   
"The arcade learning environment: An evaluation platform for general agents."   
Journal of Artificial Intelligence Research (2012).   

<a id="2">[2]</a> 
Machado et al.  
"Revisiting the Arcade Learning Environment: Evaluation Protocols
and Open Problems for General Agents"  
Journal of Artificial Intelligence Research (2018)  
URL: https://jair.org/index.php/jair/article/view/11182  
