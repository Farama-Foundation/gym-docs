---
layout: "contents"
title: API
---
# API
## Initializing Environments
Initializing environments is very easy in Gym and can be done via: 

```python
import gym
env = gym.make('CartPole-v0')
```

## Interacting with the Environment
Gym implements the classic "agent-environment loop":

<img src="AE_loop.svg"/>

The agent performs some actions in the environment (usually by passing some control inputs to the environment, e.g. torque inputs of motors) and observes
how the environment's state changes. One such action-observation exchange is referred to as a *timestep*. 

The goal in RL is to manipulate the environment in some specific way. For instance, we want the agent to navigate a robot
to a specific point in space. If it succeeds in doing this (or makes some progress towards that goal), it will receive a positive reward
alongside the observation for this timestep. The reward may also be negative or 0, if the agent did not yet succeed (or did not make any progress). 
The agent will then be trained to maximize the reward it accumulates over many timesteps.

After some timesteps, the environment may enter a terminal state. For instance, the robot may have crashed! In that case,
we want to reset the environment to a new initial state. The environment issues a done signal to the agent if it enters such a terminal state.
Not all done signals must be triggered by a "catastrophic failure": Sometimes we also want to issue a done signal after
a fixed number of timesteps, or if the agent has succeeded in completing some task in the environment.

Let's see what the agent-environment loop looks like in Gym.
This example will run an instance of `LunarLander-v2` environment for 1000 timesteps, rendering the environment at each step. You should see a window pop up rendering the environment

```python
import gym
env = gym.make("LunarLander-v2")
env.action_space.seed(42)

observation, info = env.reset(seed=42, return_info=True)

for _ in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())

    if done:
        observation, info = env.reset(return_info=True)

env.close()
```

The output should look something like this

![lunar_lander](https://user-images.githubusercontent.com/15806078/153222406-af5ce6f0-4696-4a24-a683-46ad4939170c.gif)

Every environment specifies the format of valid actions by providing an `env.action_space` attribute. Similarly,
the format of valid observations is specified by `env.observation_space`.
In the example above we sampled random actions via `env.action_space.sample()`. Note that we need to seed the action space separately from the 
environment to ensure reproducible samples.

## Standard methods
### Stepping
`step(self, action: ActType) -> Tuple[ObsType, float, bool, dict]`
 
Run one timestep of the environment's dynamics. When end of episode is reached, you are responsible for calling `reset()`
to reset this environment's state. Accepts an action and returns a tuple `(observation, reward, done, info)`.

**Parameters**
- `action`(**object**): an action provided by the agent. This will oftentimes be a numpy array, but might also be 
 an integer (for discrete action spaces) or a more complex object. This should be am element of the environment's 
action space `self.action_space`.
 
**Returns**

 This method returns a tuple `(observation, reward, done, info)`:
- `observation` (**object**): agent's observation of the current environment. This will be an element of the environment's
observation space, `self.observation_space`. This may, for instance, be a numpy array containing the positions and velocities of certain objects.
- `reward` (**float**) : amount of reward returned after previous action
- `done` (**bool**): whether the episode has ended, in which case further `step()` calls will return undefined results.
A done signal may be emitted for different reasons: Maybe the task underlying the environment was solved successfully, 
a certain timelimit was exceeded, or the physics simulation has entered an invalid state. `info` may contain additional
information regarding the reasone for a done signal.
- `info` (**dict**): contains auxiliary diagnostic information (helpful for debugging, learning, and logging). This might, for instance, 
contain:

    - metrics that describe the agent's performance or
    - state variables that are hidden from observations or
    - information that distinguishes truncation and termination or
    - individual reward terms that are combined to produce the total reward


### Resetting
`reset(self, *, seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None) -> ObsType | tuple[ObsType, dict]`

Resets the environment to an initial state and returns an initial observation.
**Parameters**
- `seed`(**int** or **None**): The seed that is used to initialize the environment's PRNG. If the environment does not already
 have a PRNG and `seed=None`(the default option) is passed, a seed will be chosen from some source of entropy (e.g. timestamp 
or /dev/urandom). However, if the environment already has a PRNG and `seed=None` is pased, the PRNG will *not* be reset. 
If you pass an integer, the PRNG will be reset even if it already exists. Usually, you want to pass an integer *right after the environment
has been initialized and then never again*. Please refer to the minimal example above to see this paradigm in action.
- `return_info`(**bool**): If true, return additional information along with initial observation. This info should be analogous
to the info returned in `step`
- `options`(**dict** or **None**): Additional information to specify how the environment is reset (optional, depending on the specific environment)

**Returns**

This method will return an observation of the initial environment state. If `return_info=True` is passed, the method returns a tuple
 `(observation, info)`, otherwise only `observation` will be returned.
 - `observation` (**object**): Observation of the initial state. This will be an element of `env.observation_space` (usually a numpy array) and is analogous to
the observation returned by `step`.
 - `info` (**dict**): This will *only* be returned if `return_info=True` is passed. It contains auxiliary information complementing `observation`. This dictionary should be analogous to the `info` returned by `step`.

### Rendering

`render(self, mode: str="human") -> Optional[np.ndarray | str]`
**Parameters**
- `mode`(**str**): This parameter specifies how the environment is rendered. The set of supported modes varies per environment 
(and some third-party environments may not support). By convention, if mode is:
      - "human": render to the current display or terminal and return nothing. Usually for human consumption.
      - "rgb_array": Return an np.ndarray with shape (height, width, 3), representing RGB values, suitable
        for turning into a video.
      - "ansi": Return a string (str) or StringIO.StringIO containing a
         terminal-style text representation. The text can include newlines
         and ANSI escape sequences (e.g. for colors).

**Returns**

Depending on the `mode`, this method may return a representation of the environment as a **str** or **ndarray**. 
It may also return **None** e.g. if `mode="human"`

Make sure that your class's metadata 'render.modes' key includes  the list of supported modes. It's recommended to call super()
implementations to use the functionality of this method.






## Additional Environment API
- `action_space`: this attribute gives the format of valid actions. It is of datatype `Space` provided by Gym. For example, if the action space is of type `Discrete` and gives the value `Discrete(2)`, this means there are two valid discrete actions: 0 & 1.
```python
>>> env.action_space
Discrete(2)
>>> env.observation_space
Box(-3.4028234663852886e+38, 3.4028234663852886e+38, (4,), float32)
```

- `observation_space`: this attribute gives the format of valid observations. It is of datatype `Space` provided by Gym. For example, if the observation space is of type `Box` and the shape of the object is `(4,)`, this denotes a valid observation will be an array of 4 numbers. We can check the box bounds as well with attributes.
```python
>>> env.observation_space.high
array([4.8000002e+00, 3.4028235e+38, 4.1887903e-01, 3.4028235e+38], dtype=float32)
>>> env.observation_space.low
array([-4.8000002e+00, -3.4028235e+38, -4.1887903e-01, -3.4028235e+38], dtype=float32)
```
- `reward_range`: returns a tuple corresponding to min and max possible rewards. Default range is set to `[-inf,+inf]`. You can set it if you want a narrower range .
- `close()`: override close in your subclass to perform any necessary cleanup.
- `seed()`: sets the seed for this environment’s random number generator. This method is being deprecated in favor of passing the keyword argument `seed` to `reset`.
Nonetheless, you will see this method being used heavily in older code.


## Spaces
Spaces are usually used to specify the format of valid actions and observations.
Every environment should have the attributes `action_space` and `observation_space`, both of which should be instances
of classes that inherit from `Space`.
There are multiple `Space` types available in Gym:

- `Box`: describes an n-dimensional continuous space. It's a bounded space where we can define the upper and lower limits which describe the valid values our observations can take.
- `Discrete`: describes a discrete space where {0, 1, ..., n-1} are the possible values our observation or action can take. Values can be shifted to {a, a+1, ..., a+n-1} using an optional argument.
- `Dict`: represents a dictionary of simple spaces.
- `Tuple`: represents a tuple of simple spaces.
- `MultiBinary`: creates a n-shape binary space. Argument n can be a number or a `list` of numbers.
- `MultiDiscrete`: consists of a series of `Discrete` action spaces with a different number of actions in each element.

```python
>>> from gym.spaces import Box, Discrete, Dict, Tuple, MultiBinary, MultiDiscrete
>>> 
>>> observation_space = Box(low=-1.0, high=2.0, shape=(3,), dtype=np.float32)
>>> observation_space.sample()
[ 1.6952509 -0.4399011 -0.7981693]
>>>
>>> observation_space = Discrete(4)
>>> observation_space.sample()
1
>>> 
>>> observation_space = Discrete(5, start=-2)
>>> observation_space.sample()
-2
>>> 
>>> observation_space = Dict({"position": Discrete(2), "velocity": Discrete(3)})
>>> observation_space.sample()
OrderedDict([('position', 0), ('velocity', 1)])
>>>
>>> observation_space = Tuple((Discrete(2), Discrete(3)))
>>> observation_space.sample()
(1, 2)
>>>
>>> observation_space = MultiBinary(5)
>>> observation_space.sample()
[1 1 1 0 1]
>>>
>>> observation_space = MultiDiscrete([ 5, 2, 2 ])
>>> observation_space.sample()
[3 0 0]
 ```

## Wrappers
Wrappers are a convenient way to modify an existing environment without having to alter the underlying code directly.
Using wrappers will allow you to avoid a lot of boilerplate code and make your environment more modular. Wrappers can 
also chained to combine their effects. Most environments that are generated via `gym.make` will already be wrapped by default.

In order to wrap an environment, you must first initialize a base environment. Then you can pass this environment along
with (possibly optional) parameters to the wrapper's constructor:
```python
>>> import gym
>>> from gym.wrappers import RescaleAction
>>> base_env = gym.make("BipedalWalker-v3")
>>> base_env.action_space
Box([-1. -1. -1. -1.], [1. 1. 1. 1.], (4,), float32)
>>> wrapped_env = RescaleAction(base_env, min_action=0, max_action=1)
>>> wrapped_env.action_space
Box([0. 0. 0. 0.], [1. 1. 1. 1.], (4,), float32)
```


There are three very common things you might want a wrapper to do:

- Transform actions before applying them to the base environment
- Transform observations that are returned by the base environment
- Transform rewards that are returned by the base environment

Such wrappers can be easily implemented by inheriting from `ActionWrapper`, `ObservationWrapper`, or `RewardWrapper` and implementing the
respective transformation.

However, sometimes you might need to implement a wrapper that does some more complicated modifications (e.g. modify the
reward based on data in `info`). Such wrappers
can be implemented by inheriting from `Wrapper`.
Gym already provides many commonly used wrappers for you. Some examples:

- `TimeLimit`: Issue a done signal if a maximum number of timesteps has been exceeded (or the base environment has issued a done signal).
- `ClipAction`: Clip the action such that it lies in the action space (of type Box).
- `RescaleAction`: Rescale actions to lie in a specified interval
- `TimeAwareObservation`: Add information about the index of timestep to observation. In some cases helpful to ensure that transitions are Markov.

If you have a wrapped environment, and you want to get the unwrapped environment underneath all of the layers of wrappers (so that you can manually call a function or change some underlying aspect of the environment), you can use the `.unwrapped` attribute. If the environment is already a base environment, the `.unwrapped` attribute will just return itself.

```python
>>> wrapped_env
<RescaleAction<TimeLimit<BipedalWalker<BipedalWalker-v3>>>>
>>> wrapped_env.unwrapped
<gym.envs.box2d.bipedal_walker.BipedalWalker object at 0x7f87d70712d0>
```

## Playing within an environment
You can also play the environment using your keyboard using the `play` function in `gym.utils.play`. 
```python
from gym.utils.play import play
play(gym.make('Pong-v0'))
```
This opens a window of the environment and allows you to control the agent using your keyboard.

Playing using the keyboard requires a key-action map. This map should be a `dict: tuple(int) -> int or None`, which maps the keys pressed to action performed.
For example, if pressing the keys `w` and `space` at the same time is supposed to perform action `2`, then the `key_to_action` dict should look like:
```python
{
    # ...
    (ord('w'), ord(' ')): 2,
    # ...
}
```
As a more complete example, let's say we wish to play with `CartPole-v0` using our left and right arrow keys. The code would be as follow:
```python
import gym
import pygame
from gym.utils.play import play
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}
play(gym.make("CartPole-v0"), keys_to_action=mapping)
```
where we obtain the corresponding key ID constants from pygame. If the `key_to_action` argument is not specified, then the default `key_to_action` mapping for that env is used, if provided.

Furthermore, you wish to plot real time statistics as you play, you can use `gym.utils.play.PlayPlot`. Here's some sample code for plotting the reward for last 5 second of gameplay:
```python
def callback(obs_t, obs_tp1, action, rew, done, info):
    return [rew,]
plotter = PlayPlot(callback, 30 * 5, ["reward"])
env = gym.make("Pong-v0")
play(env, callback=plotter.callback)
```
