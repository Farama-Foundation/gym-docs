---
hide-toc: true
firstpage:
lastpage:
---

## Gym is a standard API for reinforcement learning, and a diverse collection of reference environments


```{figure} _static/videos/box2d/lunar_lander_continuous.gif
   :alt: Lunar Lander
   :width: 500
```

**The Gym interface is simple, pythonic, and capable of representing general RL problems:**

```{code-block} python

import gym
env = gym.make("LunarLander-v2")
observation, info = env.reset(seed=42)
for _ in range(1000):
   env.render()
   action = policy(observation)  # User-defined policy function
   observation, reward, done, info = env.step(action)

   if done:
      observation, info = env.reset()
env.close()
``` 

```{toctree}
:hidden:
:caption: Introduction

content/basic_usage
```

```{toctree}
:hidden:
:caption: API

api/core
api/spaces
api/wrappers
api/vector
api/utils
```

```{toctree}
:hidden:
:caption: Environments

environments/atari/index
environments/mujoco/index
environments/toy_text/index
environments/classic_control/index
environments/box2d/index
environments/third_party_environments/index
```

```{toctree}
:hidden:
:caption: Tutorials

content/environment_creation
content/vectorising
```

```{toctree}
:hidden:
:caption: Development

Github <https://github.com/openai/gym>
Contribute to the Docs <https://github.com/Farama-Foundation/gym-docs>

```
