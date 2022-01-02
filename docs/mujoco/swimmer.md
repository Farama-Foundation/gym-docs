Swimmers-v2
---
|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|Swimmer-v2|Continuous|(2,)|[-1,1], [-1,1]| Box |(8,)|[(-inf,inf), (-inf,inf), (-inf, inf), (-inf,inf), (-inf,inf), (-inf,inf), (-inf, inf), (-inf,inf)]| |`from gym.envs.mujoco import swimmer`|
---

### Description

This environment corresponds to the Swimmer environment described in Rémi Coulom's PhD thesis ["Reinforcement Learning Using Neural Networks, with Applications to Motor Control"](https://tel.archives-ouvertes.fr/tel-00003985/document). The environment aims to increase the number of indepedent state and control variables as compared to the classic control environments. The swimmers consist of three or more segments ('***links***') and one less articulation joints ('***rotors***') - one rotor joint connecting exactly two links to form a linear chain. The swimmer is suspended in a two dimensional pool and always starts in the same position (subject to some deviation drrawn from a normal distribution), and the goal is to move as fast as possible towards the right by applying torque on the rotors and using the fluids friction.

### Notes

The problem parameters are:
Problem parameters:
* *n*: number of body parts
* *m<sub>i*: mass of part *i* (*i* ∈ {1...n}) 
* *l<sub>i*: length of part *i* (*i* ∈ {1...n}) 
* *k*: viscous-friction coefficient

While the default environment has *n* = 3, *l<sub>i* = 0.1, and *k* = 0.1. It is possible to tweak the MuJoCo XML files to increase the number of links, or to tweak any of the parameters.

### Action Space
The agent take a 4-element vector for actions.
The action space is a continuous `(action, action)` in `[-1, 1]`, where `action` represents the numerical torques applied between *links*

| Num | Action                 | Control Min | Control Max | Name (in corresponding XML file) | Joint | Unit |
|-----|------------------------|-----|-----|------|-----|
| 0   | Torque applied on the first rotor  | -1 | 1 | rot2 | hinge | torque (N m) |
| 1   | Torque applied on the second rotor  | -1 | 1 | rot3 | hinge | torque (N m) |

### Observation Space

The state space consists of:
* A<sub>0: position of first point
* θ<sub>i: angle of part *i* with respect to the *x* axis
* A<sub>0, θ<sub>i: their derivatives with respect to time (velocity and angular velocity)

The observation is a `ndarray` with shape `(8,)` where the elements correspond to the following:

| Num | Observation           | Min                  | Max                | Name (in corresponding XML file) | Joint| Unit |
|-----|-----------------------|----------------------|--------------------|----------------------|--------------------|--------------------|
| 0   | x-coordinate of the front tip              | -Inf                 | Inf                | slider1 | slide | position (m) |
| 1   | y-coordinate of the front tip              | -Inf                 | Inf                | slider2 | slide | position (m) |
| 2   | angle of the front tip                          | -Inf                 | Inf                | rot | hinge | angle (rad) |
| 3   | angle of the second rotor                  | -Inf                 | Inf                | rot2 | hinge | angle (rad) |
| 4   | angle of the second rotor                  | -Inf                 | Inf                | rot3 | hinge | angle (rad) |
| 5   | velocity of the tip along the x-axis    | -Inf                 | Inf                | slider1 | slide | velocity (m/s) |
| 6   | velocity of the tip along the y-axis    | -Inf                 | Inf                | slider2 | slide | velocity (m/s) |
| 7   | angular velocity of front tip               | -Inf                 | Inf                | rot | hinge | angular velocity (rad/s) |
| 8   | angular velocity of second rotor       | -Inf                 | Inf                | rot2 | hinge | angular velocity (rad/s) |
| 9   | angular velocity of third rotor            | -Inf                 | Inf                | rot3 | hinge | angular velocity (rad/s) |

**Note:**
In practice (and Gym implementation), the first two positional elements are omitted from the state space since the reward function is calculated based on those values. Therefore, observation space has shape `(8,)` and looks like:
| Num | Observation           | Min                  | Max                | Name (in corresponding XML file) | Joint| Unit |
|-----|-----------------------|----------------------|--------------------|----------------------|--------------------|--------------------|
| 0   | angle of the front tip                          | -Inf                 | Inf                | rot | hinge | angle (rad) |
| 1   | angle of the second rotor                  | -Inf                 | Inf                | rot2 | hinge | angle (rad) |
| 2   | angle of the second rotor                  | -Inf                 | Inf                | rot3 | hinge | angle (rad) |
| 3   | velocity of the tip along the x-axis    | -Inf                 | Inf                | slider1 | slide | velocity (m/s) |
| 4   | velocity of the tip along the y-axis    | -Inf                 | Inf                | slider2 | slide | velocity (m/s) |
| 5   | angular velocity of front tip               | -Inf                 | Inf                | rot | hinge | angular velocity (rad/s) |
| 6   | angular velocity of second rotor       | -Inf                 | Inf                | rot2 | hinge | angular velocity (rad/s) |
| 7   | angular velocity of third rotor            | -Inf                 | Inf                | rot3 | hinge | angular velocity (rad/s) |

### Rewards
The reward consists of two parts:
- *reward_front*: A reward of moving forward which is measured as *(x-coordinate before action - x-coordinate after action)/dt*. *dt* is the time between actions and is dependeent on tthe frame_skip parameter (default is 4), where the *dt* for one frame is 0.01 - making the default *dt = 4*0.01 = 0.04*. This reward would be positive if the swimmer swims right as desired.
- *reward_control*: A negative reward for penalising the swimmer if it takes actions that are too large. It is measured as *-coefficient x sum(action<sup>2</sup>)* where *coefficient* is a parameter set for the control and has a default value of 0.0001

The total reward returned is ***reward*** *=* *reward_front + reward_control*

### Starting State
All observations start in state (0,0,0,0,0,0,0,0) with a Gausssian noise with mean of 0 and standard deviation of 0.1 (default) added to the initial state for stochasticity.

### Episode Termination
The episode terminates when the episode length is greater than 1000.

### Arguments

No additional arguments are currently supported, but modifications can be made to the XML file.

```
gym.make('Swimmer-v2')
```

### Version History

* v1: 
* v0:
