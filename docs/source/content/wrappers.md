---
title: Wrappers
---

# Wrappers

Wrappers are a convenient way to modify an existing environment without having to alter the underlying code directly.
Using wrappers will allow you to avoid a lot of boilerplate code and make your environment more modular. Wrappers can 
also be chained to combine their effects. Most environments that are generated via `gym.make` will already be wrapped by default.

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
You can access the environment underneath the **first** wrapper by using
the `.env` attribute:

```python
>>> wrapped_env
<RescaleAction<TimeLimit<OrderEnforcing<BipedalWalker<BipedalWalker-v3>>>>>
>>> wrapped_env.env
<TimeLimit<OrderEnforcing<BipedalWalker<BipedalWalker-v3>>>>
```

If you want to get to the environment underneath **all** of the layers of wrappers, 
you can use the `.unwrapped` attribute. 
If the environment is already a base environment, the `.unwrapped` attribute will just return itself.

```python
>>> wrapped_env
<RescaleAction<TimeLimit<OrderEnforcing<BipedalWalker<BipedalWalker-v3>>>>>
>>> wrapped_env.unwrapped
<gym.envs.box2d.bipedal_walker.BipedalWalker object at 0x7f87d70712d0>
```

There are three common things you might want a wrapper to do:

- Transform actions before applying them to the base environment
- Transform observations that are returned by the base environment
- Transform rewards that are returned by the base environment

Such wrappers can be easily implemented by inheriting from `ActionWrapper`, `ObservationWrapper`, or `RewardWrapper` and implementing the
respective transformation. If you need a wrapper to do more complicated tasks, you can inherit from the `Wrapper` class directly.

## ActionWrapper
If you would like to apply a function to the action before passing it to the base environment,
you can simply inherit from `ActionWrapper` and overwrite the method `action` to implement that transformation.
The transformation defined in that method must take values in the base environment's action space.
However, its domain might differ from the original action space. In that case, you need to specify the new
action space of the wrapper by setting `self._action_space` in the `__init__` method of your wrapper.

Let's say you have an environment with action space of type `Box`, but you would
only like to use a finite subset of actions. Then, you might want to implement the following wrapper

```python
class DiscreteActions(gym.ActionWrapper):
    def __init__(self, env, disc_to_cont):
        super().__init__(env)
        self.disc_to_cont = disc_to_cont
        self._action_space = Discrete(len(disc_to_cont))
    
    def action(self, act):
        return self.disc_to_cont[act]

if __name__ == "__main__":
    env = gym.make("LunarLanderContinuous-v2")
    wrapped_env = DiscreteActions(env, [np.array([1,0]), np.array([-1,0]),
                                        np.array([0,1]), np.array([0,-1])])
    print(wrapped_env.action_space)         #Discrete(4)
```

Among others, Gym provides the action wrappers `ClipAction` and `RescaleAction`.

## ObservationWrapper
If you would like to apply a function to the observation that is returned by the base environment before passing
it to learning code, you can simply inherit from `ObservationWrapper` and overwrite the method `observation` to 
implement that transformation. The transformation defined in that method must be defined on the base environment's
observation space. However, it may take values in a different space. In that case, you need to specify the new
observation space of the wrapper by setting `self._observation_space` in the `__init__` method of your wrapper.

For example, you might have a 2D navigation task where the environment returns dictionaries as observations with keys `"agent_position"`
and `"target_position"`. A common thing to do might be to throw away some degrees of freedom and only consider
the position of the target relative to the agent, i.e. `observation["target_position"] - observation["agent_position"]`. 
For this, you could implement an observation wrapper like this:

```python
class RelativePosition(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self._observation_space = Box(shape=(2,), low=-np.inf, high=np.inf)
    
    def observation(self, obs):
        return obs["target_position"] - obs["agent_position"]
```

Among others, Gym provides the observation wrapper `TimeAwareObservation`, which adds information about the index of the timestep 
to the observation.

## RewardWrapper
If you would like to apply a function to the reward that is returned by the base environment before passing
it to learning code, you can simply inherit from `RewardWrapper` and overwrite the method `reward` to 
implement that transformation. This transformation might change the reward range; to specify the reward range of 
your wrapper, you can simply define `self._reward_range` in `__init__`.

Let us look at an example: Sometimes (especially when we do not have control over the reward because it is intrinsic), we want to clip the reward
to a range to gain some numerical stability. To do that, we could, for instance, implement the following wrapper:

```python
class ClipReward(gym.RewardWrapper):
    def __init__(self, env, min_reward, max_reward):
        super().__init__(env)
        self.min_reward = min_reward
        self.max_reward = max_reward
        self._reward_range = (min_reward, max_reward)
    
    def reward(self, reward):
        return np.clip(reward, self.min_reward, self.max_reward)
```

## AutoResetWrapper

Some users may want a wrapper which will automatically reset its wrapped environment when its wrapped environment reaches the done state. An advantage of this environment is that it will never produce undefined behavior as standard gym environments do when stepping beyond the done state. 

When calling step causes self.env.step() to return done,
self.env.reset() is called,
and the return format of self.step() is as follows:

```python
new_obs, terminal_reward, terminal_done, info
```

new_obs is the first observation after calling self.env.reset(),

terminal_reward is the reward after calling self.env.step(),
prior to calling self.env.reset()

terminal_done is always True

info is a dict containing all the keys from the info dict returned by
the call to self.env.reset(), with an additional key "terminal_observation"
containing the observation returned by the last call to self.env.step()
and "terminal_info" containing the info dict returned by the last call
to self.env.step().

If done is not true when self.env.step() is called, self.step() returns

```python
obs, reward, done, info
```
as normal.


The AutoResetWrapper is not applied by default when calling gym.make(), but can be applied by setting the optional autoreset argument to True:

```python
    env = gym.make("CartPole-v1", autoreset=True)
```

The AutoResetWrapper can also be applied using its constructor:
```python
    env = gym.make("CartPole-v1")
    env = AutoResetWrapper(env)
```


### Warning
When using the  AutoResetWrapper to collect rollouts, note
that the when self.env.step() returns done, a
new observation from after calling self.env.reset() is returned
by self.step() alongside the terminal reward and done state from the
previous episode . If you need the terminal state from the previous
episode, you need to retrieve it via the the "terminal_observation" key
in the info dict. Make sure you know what you're doing if you
use this wrapper!



## General Wrappers

Sometimes you might need to implement a wrapper that does some more complicated modifications (e.g. modify the
reward based on data in `info` or change the rendering behavior). 
Such wrappers can be implemented by inheriting from `Wrapper`. 

- You can set a new action or observation space by defining `self._action_space` or `self._observation_space` in `__init__`, respectively
- You can set new metadata and reward range by defining `self._metadata` and `self._reward_range` in `__init__`, respectively
- You can override `step`, `render`, `close` etc. If you do this, you can access the environment that was passed
to your wrapper (which *still* might be wrapped in some other wrapper) by accessing the attribute `self.env`.

Let's also take a look at an example for this case. Most MuJoCo environments return a reward that consists
of different terms: For instance, there might be a term that rewards the agent for completing the task and one term that
penalizes large actions (i.e. energy usage). Usually, you can pass weight parameters for those terms during
initialization of the environment. However, *Reacher* does not allow you to do this! Nevertheless, all individual terms
of the reward are returned in `info`, so let us build a wrapper for Reacher that allows us to weight those terms:

```python
class ReacherRewardWrapper(gym.Wrapper):
    def __init__(self, env, reward_dist_weight, reward_ctrl_weight):
        super().__init__(env)
        self.reward_dist_weight = reward_dist_weight
        self.reward_ctrl_weight = reward_ctrl_weight

    def step(self, action):
        obs, _, done, info = self.env.step(action)
        reward = self.reward_dist_weight*info["reward_dist"] + self.reward_ctrl_weight*info["reward_ctrl"]
        return obs, reward, done, info
```

```{note}
It is *not* sufficient to use a `RewardWrapper` in this case!
```