---
layout: "contents"
title: API
---
# API
## Initializing Environments
Initializing environment is very easy in Gym and can be done via: 

```python
import gym
env = gym.make('CartPole-v0')
```

## Interacting with the Environment
This example will run an instance of `CartPole-v0` environment for 1000 timesteps, rendering the environment at each step. You should see a window pop up rendering the classic [cart-pole](https://www.youtube.com/watch?v=J7E6_my3CHk&ab_channel=TylerStreeter) problem

```python
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000): 
	env.render()  # by default `mode="human"`(GUI), you can pass `mode="rbg_array"` to retrieve an image instead
	env.step(env.action_space.sample())  # take a random action 	
env.close()
```

The output should look something like this

![cartpole-no-reset](https://user-images.githubusercontent.com/28860173/129241283-70069f7c-453d-4670-a226-854203bd8a1b.gif)


The commonly used methods are: 

`reset()` resets the environment to its initial state and returns the observation corresponding to the initial state
`step(action)` takes an action as an input and implements that action in the environment. This method returns a set of four values 
`render()` renders the environment
	
- `observation` (**object**) : an environment specific object representation your observation of the environment after the step is taken. Its often aliased as the next state after the action has been taken
- `reward`(**float**) : immediate reward achieved by the previous action. Actual value and range will varies between environments, but the final goal is always to increase your total reward
- `done`(**boolean**): whether it’s time to `reset` the environment again. Most (but not all) tasks are divided up into well-defined episodes, and `done` being `True` indicates the episode has terminated. (For example, perhaps the pole tipped too far, or you lost your last life.)
- `info`(**dict**) : This provides general information helpful for debugging or additional information depending on the environment, such as the raw probabilities behind the environment’s last state change


## Additional Environment API

- `action_space`: this attribute gives the format of valid actions. It is of datatype `Space` provided by Gym. (For ex: If the action space is of type `Discrete` and gives the value `Discrete(2)`, this means there are two valid discrete actions 0 & 1 )
```python
print(env.action_space)
#> Discrete(2)

print(env.observation_space)
#> Box(-3.4028234663852886e+38, 3.4028234663852886e+38, (4,), float32)

```
- `observation_space`: this attribute gives the format of valid observations. It if of datatype `Space` provided by Gym. (For ex: if the observation space is of type `Box` and the shape of the object is `(4,)`, this denotes a valid observation will be an array of 4 numbers). We can check the box bounds as well with attributes

```python
print(env.observation_space.high)
#> array([4.8000002e+00, 3.4028235e+38, 4.1887903e-01, 3.4028235e+38], dtype=float32)

print(env.observation_space.low)
#> array([-4.8000002e+00, -3.4028235e+38, -4.1887903e-01, -3.4028235e+38], dtype=float32)
```
- There are multiple types of Space types inherently available in gym:
	- `Box` describes an n-dimensional continuous space. Its a bounded space where we can define the upper and lower limit which describe the valid values our observations can take.
	- `Discrete` describes a discrete space where { 0, 1, ......., n-1} are the possible values our observation/action can take. Values can be shifted to { a, a+1, ......., a+n-1} using an optional argument.
	- `Dict` represents a dictionary of simple spaces.
	- `Tuple` represents a tuple of simple spaces
	- `MultiBinary` creates a n-shape binary space. Argument n can be a number or a `list` of numbers
	- `MultiDiscrete` consists of a series of `Discrete` action spaces with different number of actions in each element
	```python
	observation_space = Box(low=-1.0, high=2.0, shape=(3,), dtype=np.float32)
	print(observation_space.sample())
	#> [ 1.6952509 -0.4399011 -0.7981693]

	observation_space = Discrete(4)
	print(observation_space.sample())
	#> 1
 
	observation_space = Discrete(5, start=-2)
	print(observation_space.sample())
	#> -2

	observation_space = Dict({"position": Discrete(2), "velocity": Discrete(3)})
	print(observation_space.sample())
	#> OrderedDict([('position', 0), ('velocity', 1)])

	observation_space = Tuple((Discrete(2), Discrete(3)))
	print(observation_space.sample())
	#> (1, 2)

	observation_space = MultiBinary(5)
	print(observation_space.sample())
	#> [1 1 1 0 1]

	observation_space = MultiDiscrete([ 5, 2, 2 ])
	print(observation_space.sample())
	#> [3 0 0]
	```
- `reward_range`:  returns a tuple corresponding to min and max possible rewards. Default range is set to `[-inf,+inf]`. You can set it if you want a narrower range 
- `close()` : Override close in your subclass to perform any necessary cleanup
- `seed()`: Sets the seed for this env's random number generator


### Unwrapping an environment
If you have a wrapped environment, and you want to get the unwrapped environment underneath all the layers of wrappers (so that you can manually call a function or change some underlying aspect of the environment), you can use the `.unwrapped` attribute. If the environment is already a base environment, the `.unwrapped` attribute will just return itself.

```python
base_env = env.unwrapped
```

### Vectorized Environment
Vectorized Environments are a way of stacking multiple independent environments, so that instead of training on one environment, our agent can train on multiple environments at a time. Each `observation` returned from a vectorized environment is a batch of observations for each sub-environment, and `step` is also expected to receive a batch of actions for each sub-environment.

**NOTE:** All sub-environments should share the identical observation and action spaces. A vector of multiple different environments is not supported

Gym Vector API consists of two types of vectorized environments:

- `AsyncVectorEnv` runs multiple environments in parallel. It uses `multiprocessing` processes, and pipes for communication.
- `SyncVectorEnv`runs multiple environments serially

```python
import gym
env = gym.vector.make('CartPole-v1', 3,asynchronous=True)  # Creates an Asynchronous env
env.reset()
#> array([[-0.04456399, 0.04653909, 0.01326909, -0.02099827],
#> [ 0.03073904, 0.00145001, -0.03088818, -0.03131252],
#> [ 0.03468829, 0.01500225, 0.01230312, 0.01825218]],
#> dtype=float32)

```


## Vectorized Environments

*Vectorized environments* are environments that run multiple (independent) sub-environments, either sequentially, or in parallel using [multiprocessing](https://docs.python.org/3/library/multiprocessing.html). Vectorized environments take as input a batch of actions, and return a batch of observations. This is particularly useful, for example, when the policy is defined as a neural network that operates over a batch of observations.

Gym provides two types of vectorized environments:

    - `gym.vector.SyncVectorEnv`, where the sub-environment are executed sequentially.
    - `gym.vector.AsyncVectorEnv`, where the sub-environments are executed in parallel using [multiprocessing](https://docs.python.org/3/library/multiprocessing.html). This creates one process per sub-environment.


Similar to `gym.make`, you can run a vectorized version of a registered environment using the `gym.vector.make` function. This runs multiple copies of the same environment (in parallel, by default).

The following example runs 3 copies of the ``CartPole-v1`` environment in parallel, taking as input a vector of 3 binary actions (one for each sub-environment), and returning an array of 3 observations stacked along the first dimension, with an array of rewards returned by each sub-environment, and an array of booleans indicating if the episode in each sub-environment has ended.

    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)
    >>> envs.reset()
    >>> actions = np.array([1, 0, 1])
    >>> observations, rewards, dones, infos = envs.step(actions)

    >>> observations
    array([[ 0.00122802,  0.16228443,  0.02521779, -0.23700266],
           [ 0.00788269, -0.17490888,  0.03393489,  0.31735462],
           [ 0.04918966,  0.19421194,  0.02938497, -0.29495203]],
          dtype=float32)
    >>> rewards
    array([1., 1., 1.])
    >>> dones
    array([False, False, False])
    >>> infos
    ({}, {}, {})


    The function `gym.vector.make` is meant to be used only in basic cases (e.g. running multiple copies of the same registered environment). For any other use-cases, please use either the `SyncVectorEnv` for sequential execution, or `AsyncVectorEnv` for parallel execution. These use-cases may include:

        - Running multiple instances of the same environment with different parameters (e.g. ``"Pendulum-v0"`` with different values for the gravity).
        - Running multiple instances of an unregistered environment (e.g. a custom environment)
        - Using a wrapper on some (but not all) sub-environments.


### Creating a vectorized environment


To create a vectorized environment that runs multiple sub-environments, you can wrap your sub-environments inside `gym.vector.SyncVectorEnv` (for sequential execution), or `gym.vector.AsyncVectorEnv` (for parallel execution, with [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)). These vectorized environments take as input a list of callable specifying how the sub-environments are created.


    >>> envs = gym.vector.AsyncVectorEnv([
    ...     lambda: gym.make("CartPole-v1"),
    ...     lambda: gym.make("CartPole-v1"),
    ...     lambda: gym.make("CartPole-v1")
    ... ])

Alternatively, to create a vectorized environment of multiple copies of the same registered sub-environment, you can use the function :func:`gym.vector.make`.


    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)  # Equivalent

To enable automatic batching of actions and observations, all the sub-environments must share the same :obj:`action_space` and :obj:`observation_space`. However, all the sub-environments are not required to be exact copies of one another. For example, you can run 2 instances of ``Pendulum-v0`` with different values of the gravity in a vectorized environment with

    

        >>> env = gym.vector.AsyncVectorEnv([
        ...     lambda: gym.make("Pendulum-v0", g=9.81),
        ...     lambda: gym.make("Pendulum-v0", g=1.62)
        ... ])

See also `Observation & Action spaces` for more information about automatic batching.

    When using `AsyncVectorEnv` with either the ``spawn`` or ``forkserver`` start methods, you must wrap your code containing the vectorized environment with ``if __name__ == "__main__":``. See `this documentation <https://docs.python.org/3/library/multiprocessing.html#the-spawn-and-forkserver-start-methods>`_ for more information.

    

        if __name__ == "__main__":
            envs = gym.vector.make("CartPole-v1", num_envs=3, context="spawn")

### Working with vectorized environments


While standard Gym environments take a single action and return a single observation (with a reward, and boolean indicating termination), vectorized environments take a *batch of actions* as input, and return a *batch of observations*, together with an array of rewards and booleans indicating if the episode ended in each sub-environment.



    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)
    >>> envs.reset()
    array([[ 0.00198895, -0.00569421, -0.03170966,  0.00126465],
           [-0.02658334,  0.00755256,  0.04376719, -0.00266695],
           [-0.02898625,  0.04779156,  0.02686412, -0.01298284]],
          dtype=float32)

    >>> actions = np.array([1, 0, 1])
    >>> observations, rewards, dones, infos = envs.step(actions)

    >>> observations
    array([[ 0.00187507,  0.18986781, -0.03168437, -0.301252  ],
           [-0.02643229, -0.18816885,  0.04371385,  0.3034975 ],
           [-0.02803041,  0.24251814,  0.02660446, -0.29707024]],
          dtype=float32)
    >>> rewards
    array([1., 1., 1.])
    >>> dones
    array([False, False, False])
    >>> infos
    ({}, {}, {})

Vectorized environments are compatible with any sub-environment, regardless of the action and observation spaces (e.g. container spaces like `gym.spaces.Dict`, or any arbitrarily nested spaces). In particular, vectorized environments can automatically batch the observations returned by :meth:`VectorEnv.reset` and :meth:`VectorEnv.step` for any standard Gym space (e.g. `gym.spaces.Box`, `gym.spaces.Discrete`, `gym.spaces.Dict`, or any nested structure thereof). Similarly, vectorized environments can take batches of actions from any standard Gym space.



    >>> class DictEnv(gym.Env):
    ...     observation_space = gym.spaces.Dict({
    ...         "position": gym.spaces.Box(-1., 1., (3,), np.float32),
    ...         "velocity": gym.spaces.Box(-1., 1., (2,), np.float32)
    ...     })
    ...     action_space = gym.spaces.Dict({
    ...         "fire": gym.spaces.Discrete(2),
    ...         "jump": gym.spaces.Discrete(2),
    ...         "acceleration": gym.spaces.Box(-1., 1., (2,), np.float32)
    ...     })
    ...
    ...     def reset(self):
    ...         return self.observation_space.sample()
    ...
    ...     def step(self, action):
    ...         observation = self.observation_space.sample()
    ...         return (observation, 0., False, {})

    >>> envs = gym.vector.AsyncVectorEnv([lambda: DictEnv()] * 3)
    >>> envs.observation_space
    Dict(position:Box(-1.0, 1.0, (3, 3), float32), velocity:Box(-1.0, 1.0, (3, 2), float32))
    >>> envs.action_space
    Dict(fire:MultiDiscrete([2 2 2]), jump:MultiDiscrete([2 2 2]), acceleration:Box(-1.0, 1.0, (3, 2), float32))

    >>> envs.reset()
    >>> actions = {
    ...     "fire": np.array([1, 1, 0]),
    ...     "jump": np.array([0, 1, 0]),
    ...     "acceleration": np.random.uniform(-1., 1., size=(3, 2))
    ... }
    >>> observations, rewards, dones, infos = envs.step(actions)
    >>> observations
    {"position": array([[-0.5337036 ,  0.7439302 ,  0.41748118],
                        [ 0.9373266 , -0.5780453 ,  0.8987405 ],
                        [-0.917269  , -0.5888639 ,  0.812942  ]], dtype=float32),
    "velocity": array([[ 0.23626241, -0.0616814 ],
                       [-0.4057572 , -0.4875375 ],
                       [ 0.26341468,  0.72282314]], dtype=float32)}


    The sub-environments inside a vectorized environment automatically call :obj:`reset` at the end of an episode. In the following example, the episode of the 3rd sub-environment ends after 2 steps (the agent fell in a hole), and the sub-environment gets reset (observation ``0``).

    

        >>> envs = gym.vector.make("FrozenLake-v1", num_envs=3, is_slippery=False)
        >>> envs.reset()
        array([0, 0, 0])
        >>> observations, rewards, dones, infos = envs.step(np.array([1, 2, 2]))
        >>> observations, rewards, dones, infos = envs.step(np.array([1, 2, 1]))

        >>> dones
        array([False, False,  True])
        >>> observations
        array([8, 2, 0])

### Observation & Action spaces


Like any Gym environment, vectorized environments contain two properties `VectorEnv.observation_space` and `VectorEnv.action_space` to specify the observation and action spaces of the environment. Since vectorized environments operate on multiple sub-environments, where the observations and actions of sub-environments are batched together, the observation and action spaces are adequately batched as well so that the input actions are valid elements of `VectorEnv.action_space`, and the observations are valid elements of `VectorEnv.observation_space`.



    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)
    >>> envs.observation_space
    Box([[-4.8 ...]], [[4.8 ...]], (3, 4), float32)
    >>> envs.action_space
    MultiDiscrete([2 2 2])


    In order to appropriately batch the observations and actions in vectorized environments, the observation and action spaces of all the sub-environments are required to be identical.

    

        >>> envs = gym.vector.AsyncVectorEnv([
        ...     lambda: gym.make("CartPole-v1"),
        ...     lambda: gym.make("MountainCar-v0")
        ... ])
        RuntimeError: Some environments have an observation space different from `Box([-4.8 ...], [4.8 ...], (4,), float32)`. In order to batch observations, the observation spaces from all environments must be equal.

However, sometimes it may be handy to have access to the observation and action spaces of a sub-environment, and not the batched spaces. You can access those with the properties `VectorEnv.single_observation_space` and `VectorEnv.single_action_space` of the vectorized environment.



    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)
    >>> envs.single_observation_space
    Box([-4.8 ...], [4.8 ...], (4,), float32)
    >>> envs.single_action_space
    Discrete(2)

This is convenient, for example, if you instantiate a policy. In the following example, we used `VectorEnv.single_observation_space` and `VectorEnv.single_action_space` to define the weights of a linear policy. Note that thanks to the vectorized environment, you can apply the policy directly to the whole batch of observations with a single call to :obj:`policy`.



    >>> from gym.spaces.utils import flatdim
    >>> from scipy.special import softmax

    >>> def policy(weights, observations):
    ...     logits = np.dot(observations, weights)
    ...     return softmax(logits, axis=1)

    >>> envs = gym.vector.make("CartPole-v1", num_envs=3)
    >>> weights = np.random.randn(
    ...     flatdim(envs.single_observation_space),
    ...     envs.single_action_space.n
    ... )
    >>> observations = envs.reset()
    >>> actions = policy(weights, observations).argmax(axis=1)
    >>> observations, rewards, dones, infos = envs.step(actions)


## Intermediate Usage


### Shared memory


`AsyncVectorEnv` runs each sub-environment inside an individual process. At each call to :meth:`AsyncVectorEnv.reset` or :meth:`AsyncVectorEnv.step`, the observations of all the sub-environments are sent back to the main process. To avoid expensive transfers of data between processes, especially with large observations (e.g. images), `AsyncVectorEnv` uses a shared memory by default (``shared_memory=True``) that processes can write to and read from at minimal cost. This can increase the throughout of the vectorized environment.



    >>> env_fns = [lambda: gym.make("BreakoutNoFrameskip-v4")] * 5

    >>> envs = gym.vector.AsyncVectorEnv(env_fns, shared_memory=False)
    >>> envs.reset()
    >>> %timeit envs.step(envs.action_space.sample())
    2.23 ms ± 136 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    >>> envs = gym.vector.AsyncVectorEnv(env_fns, shared_memory=True)
    >>> envs.reset()
    >>> %timeit envs.step(envs.action_space.sample())
    1.36 ms ± 15.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

### Exception handling


Because sometimes things may not go as planned, the exceptions raised in sub-environments are re-raised in the vectorized environment, even when the sub-environments run in parallel with `AsyncVectorEnv`. This way, you can choose how to handle these exceptions yourself (with ``try ... except``).

    >>> class ErrorEnv(gym.Env):
    ...     observation_space = gym.spaces.Box(-1., 1., (2,), np.float32)
    ...     action_space = gym.spaces.Discrete(2)
    ...
    ...     def reset(self):
    ...         return np.zeros((2,), dtype=np.float32)
    ...
    ...     def step(self, action):
    ...         if action == 1:
    ...             raise ValueError("An error occurred.")
    ...         observation = self.observation_space.sample()
    ...         return (observation, 0., False, {})

    >>> envs = gym.vector.AsyncVectorEnv([lambda: ErrorEnv()] * 3)
    >>> observations = envs.reset()
    >>> observations, rewards, dones, infos = envs.step(np.array([0, 0, 1]))
    ERROR: Received the following error from Worker-2: ValueError: An error occurred.
    ERROR: Shutting down Worker-2.
    ERROR: Raising the last exception back to the main process.
    ValueError: An error occurred.


# Advanced Usage


## Custom spaces

Vectorized environments will batch actions and observations if they are elements from standard Gym spaces, such as `gym.spaces.Box`, `gym.spaces.Discrete`, or `gym.spaces.Dict`. If you create your own environment with a custom action and/or observation space though (inheriting from `gym.Space`), the vectorized environment will not attempt to automatically batch the actions/observations, and instead it will return the raw tuple of elements from all sub-environments.

In the following example, we created a new environment `SMILESEnv`, whose observations are strings representing the [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) notation of a molecular structure, with a custom observation space `SMILES`. The observations returned by the vectorized environment is a tuple of strings. 

```

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

Custom observation & action spaces may inherit from the `gym.Space` class. However, most use-cases should be covered by the existing space classes (e.g. `gym.spaces.Box`, `gym.spaces.Discrete`, etc...), and container classes (`gym.spaces.Tuple` & `gym.spaces.Dict`). Moreover, some implementations of Reinforcement Learning algorithms might not handle custom spaces properly. Use custom spaces with care.

If you use `AsyncVectorEnv` with a custom observation space, you must set ``shared_memory=False``, since shared memory and automatic batching is not compatible with custom spaces. In general if you use custom spaces with `AsyncVectorEnv`, the elements of those spaces must be `pickleable`_.
