# Handling Time Limits
In using Gym environments with reinforcement learning code, a common problem observed is how time limits are incorrectly handled. The `done` signal received from `env.step` indicates whether an episode has ended. However, this signal does not distinguish between the two different reasons why an episode can end - `termination` and `truncation`. 

### Termination
Termination refers to the episode ending after reaching a terminal state that is defined as part of the environment definition. Examples are - task success, task failure, robot falling down etc. Notably this also includes episode ending in finite-horizon environments due to a time-limit inherent to the environment. Note that to preserve Markov property, a representation of the remaining time must be present in the agent's observation in finite-horizon environments. [(Reference)](https://arxiv.org/abs/1712.00378)


### Truncation
Truncation refers to the episode ending after an externally defined time-limit. This time-limit is not part of the environment definition, and its sole purpose is practicality for the user collecting rollouts of the episode. 

An infinite-horizon environment is an obvious example where this is needed. We cannot wait forever for the episode to complete, so we set a practical time-limit after which we forcibly halt the episode. The last state in this case is not a terminal state since it has a non-zero transition probability of moving to another state as per the environment definition. This is also different from time-limits in finite horizon environments as the agent in this case has no idea about this time-limit. 

### Importance in learning code

Bootstrapping (using one or more estimated values of a variable to update estimates of the same variable) is a key aspect of Reinforcement Learning. A common example of bootstrapping in RL is updating the estimate of the Q-value function, 

```math
Q_{target}(o_t, a_t) = r_t + \gamma . \max_a(Q(o_{t+1}, a_{t+1}))
```
In classical RL, the new `Q` estimate is a weighted average of previous `Q` estimate and `Q_target` while in Deep Q-Learning, the error between `Q_target` and previous `Q` estimate is minimized.

However, at the terminal state, bootstrapping is not done,

```math
Q_{target}(o_t, a_t) = r_t
```

This is where the distinction between termination and truncation becomes important. When an episode ends due to termination we don't bootstrap, when it ends due to truncation, we bootstrap.

While using gym environments, the `done` signal is frequently used to determine whether to bootstrap or not. However this is incorrect since it does not differentiate between termination and truncation.

A simple example for value functions is shown below. This is an illustrative example and not part of any specific algorithm.

```python
# INCORRECT
vf_target = rew + gamma * (1-done)* vf_next_state
```

This is incorrect in the case of episode ending due to a truncation, where bootstrapping needs to happen but it doesn't. 

### Solution

Currently, gym supplies truncation information through the TimeLimit wrapper which adds `TimeLimit.truncated` key to `info` which is returned by `env.step`. The correct way to handle terminations and truncations now would be, 

```python
terminated = done and 'TimeLimit.truncated' not in info

vf_target = rew + gamma*(1-terminated)*vf_next_state
```
