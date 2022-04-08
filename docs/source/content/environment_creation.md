---
layout: "contents"
title: Environment Creation
---
# Environment Creation

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
      foo_env.py
      foo_extrahard_env.py
```

## Subclassing gym.Env

We will first write the code for our custom environment in `gym-foo/gym_foo/envs/foo_env.py` - let's call it `FooEnv`. All custom environments should subclass `gym.Env` and override the `step`, `reset`, `render`, `close`  methods like so:

```python
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # TODO
        ...
    def step(self, action):
        # TODO
        ...
    def reset(self):
        # TODO
        ...
    def render(self, mode='human'):
        # TODO
        ...
    def close(self):
        # TODO
        ...
```

We will also create a more difficult version, `FooExtraHardEnv`, in `gym-foo/gym_foo/envs/foo_extrahard_env.py`, following the same template as above: 

```python
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooExtraHardEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # TODO
        ...
    def step(self, action):
        # TODO
        ...
    def reset(self):
        # TODO
        ...
    def render(self, mode='human'):
        # TODO
        ...
    def close(self):
        # TODO
        ...
```

## Registering Envs

In order for the custom environments to be detected by OpenAI gym, they must be registered as follows. We will choose to put this code in `gym-foo/gym_foo/__init__.py`. 

```python
from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_foo.envs:FooEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)
```

After registration, our custom `FooEnv` environment can be created with `env = gym.make('foo-v0')`. 

`gym-foo/gym_foo/envs/__init__.py` should have:

```python
from gym_foo.envs.foo_env import FooEnv
from gym_foo.envs.foo_extrahard_env import FooExtraHardEnv
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
  
After you have installed your package locally with `pip install -e gym-foo`, you can create an instance of the environment with `gym.make('gym_foo:foo-v0')`
