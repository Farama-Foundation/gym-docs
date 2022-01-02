---
layout: env_selection
title: Classic Control Environments
---
<div class="selection-content" markdown="1">

MuJoCo stands for Multi-Joint dynamics with Contact. It is a physics engine for faciliatating research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.

The unique dependencies for this set of environments can be installed via:

````bash
pip install gym[classic_control]
````

These environments also require that the MuJoCo engine be installed. As of October 2021 DeepMind has acquired MuJoCo and is open sourcing it in 2022, making it free for everyone. 

There are ten Mujoco environments: Ant, HalfCheetah, Hopper, Humanoid, HumanoidStandup, IvertedDoublePendulum, InvertedPendulum, Reacher, Swimmer, and Walker. All of these environments are stochastic in terms of their initial state, with a Gaussian noise added to a fixed initial state in order to add stochasticity.

Among Gym environments, this set of environments can be considered as more difficult ones to solve by a policy.

All environments are highly configurable via arguments specified in each environment's documentation.

</div>
