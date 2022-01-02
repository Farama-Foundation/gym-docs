Swimmers-v2
---
|Title|Action Type|Action Shape|Action Values|Observation Type| Observation Shape|Observation Values|Average Total Reward|Import|
| ----------- | -----------| ----------- | -----------|-----------| ----------- | -----------| ----------- | -----------|
|Swimmer-v2|Continuous|(2,)|[-1,1], [-1,1]| Box |(4,)|[(-4.8,4.8),(-inf,inf), (~ -0.2095, ~ 0.2095), (-inf, inf)]| |`from gym.envs.mujoco import swimmer`|
---

### Description

This environment corresponds to the Swimmer environment described in Rémi Coulom's PhD thesis ["Reinforcement Learning Using Neural Networks, with Applications to Motor Control"](https://tel.archives-ouvertes.fr/tel-00003985/document). The environment aims to increase the number of indepedent state and control variables as compared to the classic control environments. The swimmers consist of three or more segments ('links') and one less articulation joints ('rotors') - one rotor joint connecting exactly two links to form a linear chain. The swimmer is suspended in a two dimensional pool and always starts in the same position (subject to some deviation drrawn from a normal distribution), and the goal is to move as fast as possible towards the right by applying torque on the rotors and using the fluids friction.

### Notes

The problem parameters are:
Problem parameters:
* *n*: number of body parts
* *m_i*: mass of part i (i ∈ {1...n}) 
* $l_{i}$: length of part i (i ∈ {1...n}) 
* *k*: viscous-friction coefficient

While the default environment has n = 3, mi = , li =, and k = . It is possible to tweak the MuJoCo XML files to increase the number of links, or to tweak any of the parameters.

### Action Space
The agent take a 4-element vector for actions.
The action space is `(action)` in `[-1, 1]`, where `action` is used to push the cart with a fixed amount of force:

| Num | Action                 |
|-----|------------------------|
| 0   | Torque applied on the first rotor  |
| 1   | Torque applied on the second rotor  |

Note: The amount the velocity is reduced or increased is not fixed as it depends on the angle the pole is pointing. 
This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it

### Observation Space
The observation is a `ndarray` with shape `(4,)` where the elements correspond to the following:

| Num | Observation           | Min                  | Max                |
|-----|-----------------------|----------------------|--------------------|
| 0   | Cart Position         | -4.8*                 | 4.8*                |
| 1   | Cart Velocity         | -Inf                 | Inf                |
| 2   | Pole Angle            | ~ -0.418 rad (-24°)** | ~ 0.418 rad (24°)** |
| 3   | Pole Angular Velocity | -Inf                 | Inf                |

**Note:** above denotes the ranges of possible observations for each element, but in two cases this range exceeds the
range of possible values in an un-terminated episode:
- `*`: the cart x-position can be observed between `(-4.8, 4.8)`, but an episode terminates if the cart leaves the
`(-2.4, 2.4)` range.
- `**`: Similarly, the pole angle can be observed between  `(-.418, .418)` radians or precisely **±24°**, but an episode is 
terminated if the pole angle is outside the `(-.2095, .2095)` range or precisely **±12°**

### Rewards
The reward consists of two parts:
- A reward of moviing forward which is measured as 

### Starting State
All observations are assigned a uniform random value between (-0.05, 0.05)

### Episode Termination
The episode terminates of one of the following occurs:

1. Pole Angle is more than ±12°
2. Cart Position is more than ±2.4 (center of the cart reaches the edge of the display)
3. Episode length is greater than 500 (200 for v0)

### Arguments

No additional arguments are currently supported.

```
gym.make('Swimmer-v2')
```

### Version History

* v1: Maximum episode length increased from 200 to 500 steps, reward threshold increased from 195 to 475.
* v0: Initial versions release (1.0.0)
