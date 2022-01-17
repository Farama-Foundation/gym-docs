---
layout: "contents"
title: API
---

Advanced Usage
==============

Custom spaces
-------------

Vectorized environments will batch actions and observations if they are
elements from standard Gym spaces, such as
`~gym.spaces.Box`{.interpreted-text role="class"},
`~gym.spaces.Discrete`{.interpreted-text role="class"}, or
`~gym.spaces.Dict`{.interpreted-text role="class"}. If you create your
own environment with a custom action and/or observation space though
(inheriting from `gym.Space`{.interpreted-text role="class"}), the
vectorized environment will not attempt to automatically batch the
actions/observations, and instead it will return the raw tuple of
elements from all sub-environments.

In the following example, we created a new environment
`SMILESEnv`{.interpreted-text role="obj"}, whose observations are
strings representing the
[SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
notation of a molecular structure, with a custom observation space
`SMILES`{.interpreted-text role="obj"}. The observations returned by the
vectorized environment is a tuple of strings.

``` {.}
>>> class SMILES(gym.Space):
...     def __init__(self, symbols):
...         super().__init__()
...         self.symbols = symbols
...
...     def __eq__(self, other):
...         return self.symbols == other.symbols

>>> class SMILESEnv(gym.Env):
...     observation_space = SMILES("][()CO=")
...     action_space = gym.spaces.Discrete(7)
...
...     def reset(self):
...         self._state = "["
...         return self._state
...
...     def step(self, action):
...         self._state += self.observation_space.symbols[action]
...         reward = done = (action == 0)
...         return (self._state, float(reward), done, {})

>>> envs = gym.vector.AsyncVectorEnv(
...     [lambda: SMILESEnv()] * 3,
...     shared_memory=False
... )
>>> envs.reset()
>>> observations, rewards, dones, infos = envs.step(np.array([2, 5, 4]))
>>> observations
('[(', '[O', '[C')
```

::: {.warning}
::: {.title}
Warning
:::

Custom observation & action spaces may inherit from the
`gym.Space`{.interpreted-text role="class"} class. However, most
use-cases should be covered by the existing space classes (e.g.
`~gym.spaces.Box`{.interpreted-text role="class"},
`~gym.spaces.Discrete`{.interpreted-text role="class"}, etc\...), and
container classes (`~gym.spaces.Tuple`{.interpreted-text role="class"} &
`~gym.spaces.Dict`{.interpreted-text role="class"}). Moreover, some
implementations of Reinforcement Learning algorithms might not handle
custom spaces properly. Use custom spaces with care.
:::

::: {.warning}
::: {.title}
Warning
:::

If you use `AsyncVectorEnv`{.interpreted-text role="class"} with a
custom observation space, you must set `shared_memory=False`, since
shared memory and automatic batching is not compatible with custom
spaces. In general if you use custom spaces with
`AsyncVectorEnv`{.interpreted-text role="class"}, the elements of those
spaces must be
[pickleable](https://docs.python.org/3/library/pickle.html).
:::
