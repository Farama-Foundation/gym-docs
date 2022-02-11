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

<img src="https://gym.openai.com/assets/docs/aeloop-138c89d44114492fd02822303e6b4b07213010bb14ca5856d2d49d6b62d88e53.svg" width=20%/>

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


## Commonly used methods
>### Stepping
> `step(action: ActType) -> Tuple[ObsType, float, bool, dict]`
> 
>Run one timestep of the environment's dynamics. When end of episode is reached, you are responsible for calling `reset()`
to reset this environment's state. Accepts an action and returns a tuple `(observation, reward, done, info)`.
>
>>**Parameters**
>>- `action`(**object**): an action provided by the agent. This will oftentimes be a numpy array, but might also be 
>> an integer (for discrete action spaces) or a more complex object.
> 
>>**Returns**
>>
>> This method returns a tuple `(observation, reward, done, info)`:
>>- `observation` (**object**): agent's observation of the current environment.
>> This may, for instance, be a numpy array containing the positions and velocities of certain objects.
>>- `reward` (**float**) : amount of reward returned after previous action
>>- `done` (**bool**): whether the episode has ended, in which case further `step()` calls will return undefined results.
>> A done signal may be emitted for different reasons: Maybe the task underlying the environment was solved successfully, 
>> a certain timelimit was exceeded, or the physics simulation has entered an invalid state. `info` may contain additional
>> information regarding the reasone for a done signal.
>>- `info` (**dict**): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)

>### Resetting
>`reset(*, seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None,) -> Union[ObsType, tuple[ObsType, dict]]`
>
>Resets the environment to an initial state and returns an initial observation.
>>**Parameters**
>>- `seed`(**int** or **None**): The seed that is used to initialize the environments PRNG. If the environment does not already
>> have a PRNG and `seed=None`(the default option) is passed, a seed will be chosen from some source of entropy (e.g. timestamp 
or /dev/urandom). However, if the environment already has a PRNG and `seed=None` is pased, the PRNG will *not* be reset. 
If you pass an integer, the PRNG will be reset even if it already exists. Usually, you want to pass an integer *right after the environment
has been initialized and then never again*. Please refer to the minimal example above to see this paradigm in action.
>>- `return_info`(**bool**): If true, return additional information along with initial observation. This info should be analogous
to the info returned in `step`
>>- `options`(**dict** or **None**):
>
>>**Returns**
>>
>>This method will return an observation of the initial environment state. If `return_info=True` is passed, the method returns a tuple
>> `(observation, info)`, where `observation` is the actual observation and `info` is some auxiliary information complementing `observation`.
>> The dictionary `info` should be analogous to the `info` returned by `step`. If `return_info=False` is passed, only `observation` is returned.

>### Rendering
> 
>`render(mode: str="human") -> Optional[Union[numpy.ndarray, str]]`
>>**Parameters**
>>- `mode`(**str**): This parameter specifies how the environment is rendered. The set of supported modes varies per environment. (And some
environments do not support rendering at all.) By convention, if mode is:
>>      - "human": render to the current display or terminal and return nothing. Usually for human consumption.
>>      - "rgb_array": Return an numpy.ndarray with shape (x, y, 3), representing RGB values for an x-by-y pixel image, suitable
>>        for turning into a video.
>>      - "ansi": Return a string (str) or StringIO.StringIO containing a
         terminal-style text representation. The text can include newlines
         and ANSI escape sequences (e.g. for colors).
>
>>**Returns**
>>
>>Depending on the `mode`, this method may return a representation of the environment as a **str** or **ndarray**. 
>>It may also return **None** e.g. if `mode="human"`
> 
>Make sure that your class's metadata 'render.modes' key includes  the list of supported modes. It's recommended to call super()
implementations to use the functionality of this method.






## Additional Environment API
- `action_space`: this attribute gives the format of valid actions. It is of datatype `Space` provided by Gym. For example, if the action space is of type `Discrete` and gives the value `Discrete(2)`, this means there are two valid discrete actions: 0 & 1.

```python
print(env.action_space)
#> Discrete(2)

print(env.observation_space)
#> Box(-3.4028234663852886e+38, 3.4028234663852886e+38, (4,), float32)
```

- `observation_space`: this attribute gives the format of valid observations. It is of datatype `Space` provided by Gym. For example, if the observation space is of type `Box` and the shape of the object is `(4,)`, this denotes a valid observation will be an array of 4 numbers. We can check the box bounds as well with attributes.

```python
print(env.observation_space.high)
#> array([4.8000002e+00, 3.4028235e+38, 4.1887903e-01, 3.4028235e+38], dtype=float32)

print(env.observation_space.low)
#> array([-4.8000002e+00, -3.4028235e+38, -4.1887903e-01, -3.4028235e+38], dtype=float32)
```
- `reward_range`: returns a tuple corresponding to min and max possible rewards. Default range is set to `[-inf,+inf]`. You can set it if you want a narrower range .
- `close()`: override close in your subclass to perform any necessary cleanup.
- `seed()`: sets the seed for this environment’s random number generator. This method is being deprecated in favor of passing the keyword argument `seed` to `reset`.
Nonetheless, you will see this method being used heavily in older code.


## Wrappers
If you have a wrapped environment, and you want to get the unwrapped environment underneath all of the layers of wrappers (so that you can manually call a function or change some underlying aspect of the environment), you can use the `.unwrapped` attribute. If the environment is already a base environment, the `.unwrapped` attribute will just return itself.

```python
base_env = env.unwrapped
```
