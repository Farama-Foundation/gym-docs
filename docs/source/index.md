---
hide-toc: true
---

# Gym documentation

## Gym is a standard API for reinforcement learning, and a diverse collection of reference environments.


```{figure} https://user-images.githubusercontent.com/15806078/153222406-af5ce6f0-4696-4a24-a683-46ad4939170c.gif
   :alt: Lunar Lander
```

**The Gym interface is simple, pythonic, and capable of representing general RL problems:**

```{code-block} python

import gym
env = gym.make("LunarLander-v2")
observation, info = env.reset(seed=42, return_info=True)
for _ in range(1000):
   env.render()
   action = policy(observation)  # User-defined policy function
   observation, reward, done, info = env.step(action)

   if done:
      observation, info = env.reset(return_info=True)
env.close()
``` 

```{toctree}
:hidden:
:caption: User Guide

content/api
content/environment_creation
content/spaces
content/vector_api
content/tutorials
content/wrappers
Github <https://github.com/openai/gym>
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
:caption: Development

Contribute to the Docs <https://github.com/Farama-Foundation/gym-docs>

```
