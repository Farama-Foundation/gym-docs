---
layout: "contents"
title: Environment Creation
---
# How to create new environments for Gym

This documentation overviews creating new environments and relevant useful wrappers, utilities and tests included in OpenAI Gym designed for the creation of new environments.

## Example Custom Environment

Here is a simple skeleton of the repository structure for a Python Package containing a custom environment. For a more complete example, please refer to: https://github.com/openai/gym-soccer.

```sh
gym-foo/
  README.md
  setup.py
  gym_foo/
    __init__.py
    envs/
      __init__.py
      grid_world.py
```

## Subclassing gym.Env

We will first write the code for our custom environment in `gym-foo/gym_foo/envs/grid_world.py`. The environment consists of a 2-dimensional grid of fixed size and we call it `GridWorld`
- The agent can move vertically and horizontally in each timestep. 
- The goal is to navigate to a target on the grid.
- Observations consist of the position of the agent and the position of the target. 
- There are 4 actions in our environment, corresponding to "right", "up", "left", "down".
- A done signal is issued as soon as the agent has navigated to the grid cell where the target is located
- Rewards are binary and sparse, meaning that the immediate reward is always zero, unless the agent has reached the target, then it is 1

All custom environments should subclass `gym.Env` and override the `step`, `reset`, `render`, `close`  methods.
Let us look at the implementation of `GridWorld`:

```python
import gym
from gym import spaces
import pygame
import numpy as np


class GridWorld(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    def __init__(self, size=5):
        self.size = size
        self.window_size = 512
        self.observation_space = spaces.Dict({"agent": spaces.MultiDiscrete([size, size]),
                                              "target": spaces.MultiDiscrete([size, size])})
        self.action_space = spaces.Discrete(4)
        self._action_to_direction = {0: np.array([1, 0]),
                                     1: np.array([0, 1]),
                                     2: np.array([-1, 0]),
                                     3: np.array([0, -1])}

        self.window = None
        self.clock = None

    def _get_obs(self):
        return {"agent": self._agent_location,
                "target": self._target_location}

    def _info_from_obs(self, obs):
        return {"distance": np.linalg.norm(obs["agent"] - obs["target"], ord=1)}
    
    def reset(self, seed=None, return_info=False, options=None):
        super().reset(seed=seed)
        self._agent_location = self.np_random.integers(0, self.size, size=2)
        self._target_location = self._agent_location
        while np.array_equal(self._target_location, self._agent_location):
            self._target_location = self.np_random.randint(0, self.size, size=2)

        observation = self._get_obs()
        info = self._info_from_obs(observation)
        return (observation, info) if return_info else observation
        
    def step(self, action):
        direction = self._action_to_direction[action]
        self._agent_location = np.clip(self._agent_location + direction, 0, self.size - 1)
        done = np.array_equal(self._agent_location, self._target_location)
        reward = 1 if done else 0
        observation = self._get_obs()
        info = self._info_from_obs(observation)

        return observation, reward, done, info

    def render(self, mode="human"):
        if self.window is None and mode=="human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and mode=="human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = self.window_size / self.size

        # First we draw the target
        pygame.draw.rect(canvas, (255, 0, 0), pygame.Rect(pix_square_size* self._target_location, (pix_square_size, pix_square_size)))
        # Now we draw the agent
        pygame.draw.circle(canvas, (0, 0, 255), (self._agent_location + 0.5) * pix_square_size, pix_square_size/3)

        # Finally, add some gridlines
        for x in range(self.size + 1):
            pygame.draw.line(canvas, 0, (0, pix_square_size * x), (self.window_size, pix_square_size * x))
            pygame.draw.line(canvas, 0, (pix_square_size * x, 0), (pix_square_size * x, self.window_size))

        if mode == "human":
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close():
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
```


## Registering Envs

In order for the custom environments to be detected by OpenAI gym, they must be registered as follows. We will choose to put this code in `gym-foo/gym_foo/__init__.py`. 

```python
from gym.envs.registration import register

register(
    id='GridWorld-v0',
    entry_point='gym_foo.envs:GridWorld',
)
```

After registration, our custom `FooEnv` environment can be created with `env = gym.make('GridWorld-v0')`. 

`gym-foo/gym_foo/envs/__init__.py` should have:

```python
from gym_foo.envs.grid_world import GridWorld
```

## Creating a Package

The last step is to structure our code as a Python package. This involves configuring `gym-foo/setup.py`. A minimal example of how to do so is as follows: 

```python
from setuptools import setup

setup(name='gym_foo',
    version='0.0.1',
    install_requires=['gym']  # And any other dependencies foo needs
)
```
  
After you have installed your package locally with `pip install -e gym-foo`, you can create an instance of the environment with `gym.make('gym_foo:GridWorld-v0')`
