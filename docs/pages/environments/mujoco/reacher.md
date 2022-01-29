Reacher
---
|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|Reacher-v2|Continuous|(2,)|[-1,1], [-1,1]| Box |(11,)|[(-inf,inf), (-inf,inf), (-inf, inf), (-inf,inf), (-inf,inf), (-inf,inf), (-inf, inf), (-inf,inf), (-inf,inf), (-inf,inf), (-inf, inf)]| |`from gym.envs.mujoco import reacher`|
---

### Description



### Action Space
The agent take a 2-element vector for actions.
The action space is a continuous `(action, action)` all in `[-1, 1]`, where `action` represents the numerical torques applied at the hinge joints.

| Num | Action                    | Control Min | Control Max | Name (in corresponding XML file) | Joint | Unit |
|-------|----------------------|---------------|----------------|---------------------------------------|-------|------|
| 0   | Torque applied at the first hinge (connecting the link to the point of fixture) | -1 | 1 | joint0  | hinge | torque (N m) |
| 1   |  Torque applied at the second hinge (connecting the two links)   | -1 | 1 | joint1     | hinge | torque (N m) |

### Observation Space

The state space consists of positional values of different body parts of the hopper, followed by the velocities of those individual parts (their derivatives) with all the positions ordered before all the velocities.

The observation is a `ndarray` with shape `(11,)` where the elements correspond to the following:

| Num | Observation           | Min                  | Max                | Name (in corresponding XML file) | Joint| Unit |
|-----|-----------------------|----------------------|--------------------|----------------------|--------------------|--------------------|
| 0       | cosine of the angle of the first arm                                       | -Inf                 | Inf                | cos(joint0) | hinge | unitless |
| 1        | cosine of the angle of the second arm                                       | -Inf                 | Inf                | cos(joint1) | hinge | unitless |
| 2       | cosine of the angle of the first arm                                       | -Inf                 | Inf                | cos(joint0) | hinge | unitless |
| 3       | cosine of the angle of the second arm                                       | -Inf                 | Inf                | cos(joint1) | hinge | unitless |
| 4       |  x-coorddinate of the target                                      | -Inf                 | Inf                | target_x | slide | position (m) |
| 5       |  y-coorddinate of the target                                      | -Inf                 | Inf                | target_y | slide | position (m) |
| 6       | angular velocity of the first arm                                     | -Inf                 | Inf                | joint0 | hinge | angular velocity (rad/s) |
| 7       | angular velocity of the second arm                                     | -Inf                 | Inf                | joint1 | hinge | angular velocity (rad/s) |
| 8      | x-value of position_fingertip - position_target                                     | -Inf                 | Inf                | NA | slide | position (m) |
| 9      | y-value of position_fingertip - position_target                                     | -Inf                 | Inf                | NA | slide | position (m) |
| 10      | z-value of position_fingertip - position_target (0 since reacher is 2d and z is same for both)     | -Inf                 | Inf                | NA | slide | position (m) |


Most Gym environments just return the positions and velocity of the joints in the `.xml` file as the state of the environment. However, in reacher the state is created by combining only certain elements of the position and velocity, and performing some function transformations on them. If one is to read the `.xml` for reacher then they will find 4 joints:
| Num | Observation           | Min                  | Max                | Name (in corresponding XML file) | Joint| Unit |
|-----|-----------------------|----------------------|--------------------|----------------------|--------------------|--------------------|
| 0       | angle of the first arm                                       | -Inf                 | Inf                | joint0 | hinge | angle (rad |
| 1       | angle of the second arm                                       | -Inf                 | Inf                | joint1 | hinge | angle (rad |
| 2       | x-coordinate of the target                                       | -Inf                 | Inf                | target_x | slide | position (m) |
| 3       | y-coordinate of the target                                       | -Inf                 | Inf                | target_y | slide | position (m) |


### Rewards
The reward consists of two parts:
- *reward_distance*: This reward is a measure of how far the *fingertip* of the reacher (the unattached end) is from the target, with a more negative value assigned for when the reacher *fingertip* is further away from the target. It is ccalculated as the negative of vector norm of (position of the fingertip - position of target), or *-norm("fingertip" - "target")*.
- *reward_control*: A negative reward for penalising the walker if it takes actions that are too large. It is measured as *- **x** sum(action<sup>2</sup>)* (unlike otther enviroonments,  where *coefficient* is a parameter set for the control, the vavlue here is static and fixed to 1. It can be tweakedd by using a default class).

The total reward returned is ***reward*** *=* *reward_distance + reward_control*

### Starting State
All observations start in state (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) with a noise added for stochasticity. A uniform noise in the range [-0.1, 0.1] is added to the posititional attributes, while the taarget is selecting uniformly in the range [-0.2, 0.2]. A uniform noise in the range of [-0.005, 0.005] is added to the velocity elements, and the last index ("fingertip" - "target" distance) is calculated at the end once everything is set. The default setting has a framerate of 2 and a *dt = 4\*0.01 = 0.02*

### Episode Termination

The episode terminates when any of the following happens:

1. The episode duration reaches a 50 timesteps (with a new random target popping up if the reacher's fingertip reaches it before 50 timesteps)
2. Any of the state space values is no longer finite.

### Arguments

No additional arguments are currently supported (in v2 and lower), but modifications can be made to the XML file in the assets folder (or by changing the path to a modified XML file in another folder)..

```
env = gym.make('Reacher-v2')
```

There is no v3 for Reacher, unlike the robot environments where a v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight, reset_noise_scale etc.


### Version History

* v3: support for gym.make kwargs such as xml_file, ctrl_cost_weight, reset_noise_scale etc. rgb rendering comes from tracking camera (so agent does not run away from screen)
* v2: All continuous control environments now use mujoco_py >= 1.50
* v1: max_time_steps raised to 1000 for robot based tasks (not including reacher, which has a max_time_steps of 50). Added reward_threshold to environments. 
* v0: Initial versions release (1.0.0)
