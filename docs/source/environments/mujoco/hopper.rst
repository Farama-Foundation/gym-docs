Hopper
======

Description
~~~~~~~~~~~

This environment is based on the work done by Erez, Tassa, and Todorov
in `“Infinite Horizon Model Predictive Control for Nonlinear Periodic
Tasks” <http://www.roboticsproceedings.org/rss07/p10.pdf>`__. The
environment aims to increase the number of independent state and control
variables as compared to the classic control environments. The hopper is
a two-dimensional one-legged figure that consist of four main body parts
- the torso at the top, the thigh in the middle, the leg in the bottom,
and a single foot on which the entire body rests. The goal is to make
hops that move in the forward (right) direction by applying torques on
the three hinges connecting the four body parts.

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (3,), float32)``. An action
represents the torques applied between *links*

+---+--------------------+------+------+-------------------+---+-------+
| N | Action             | Con  | Con  | Name (in          | J | Unit  |
| u |                    | trol | trol | corresponding XML | o |       |
| m |                    | Min  | Max  | file)             | i |       |
|   |                    |      |      |                   | n |       |
|   |                    |      |      |                   | t |       |
+===+====================+======+======+===================+===+=======+
| 0 | Torque applied on  | -1   | 1    | thigh_joint       | h | t     |
|   | the thigh rotor    |      |      |                   | i | orque |
|   |                    |      |      |                   | n | (N m) |
|   |                    |      |      |                   | g |       |
|   |                    |      |      |                   | e |       |
+---+--------------------+------+------+-------------------+---+-------+
| 1 | Torque applied on  | -1   | 1    | leg_joint         | h | t     |
|   | the leg rotor      |      |      |                   | i | orque |
|   |                    |      |      |                   | n | (N m) |
|   |                    |      |      |                   | g |       |
|   |                    |      |      |                   | e |       |
+---+--------------------+------+------+-------------------+---+-------+
| 3 | Torque applied on  | -1   | 1    | foot_joint        | h | t     |
|   | the foot rotor     |      |      |                   | i | orque |
|   |                    |      |      |                   | n | (N m) |
|   |                    |      |      |                   | g |       |
|   |                    |      |      |                   | e |       |
+---+--------------------+------+------+-------------------+---+-------+

Observation Space
~~~~~~~~~~~~~~~~~

Observations consist of positional values of different body parts of the
hopper, followed by the velocities of those individual parts (their
derivatives) with all the positions ordered before all the velocities.

By default, observations do not include the x-coordinate of the hopper.
It may be included by passing
``exclude_current_positions_from_observation=False`` during
construction. In that case, the observation space will have 12
dimensions where the first dimension represents the x-coordinate of the
hopper. Regardless of whether
``exclude_current_positions_from_observation`` was set to true or false,
the x-coordinate will be returned in ``info`` with key ``"x_position"``.

However, by default, the observation is a ``ndarray`` with shape
``(11,)`` where the elements correspond to the following:

+---+-----------+-----------+---------+-----------+---------+---------+
| N | Ob        | Min       | Max     | Name (in  | Joint   | Unit    |
| u | servation |           |         | corr      |         |         |
| m |           |           |         | esponding |         |         |
|   |           |           |         | XML file) |         |         |
+===+===========+===========+=========+===========+=========+=========+
| 0 | z-c       | -Inf      | Inf     | rootz     | slide   | p       |
|   | oordinate |           |         |           |         | osition |
|   | of the    |           |         |           |         | (m)     |
|   | top       |           |         |           |         |         |
|   | (height   |           |         |           |         |         |
|   | of        |           |         |           |         |         |
|   | hopper)   |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | rooty     | hinge   | angle   |
|   | the top   |           |         |           |         | (rad)   |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | angle of  | -Inf      | Inf     | th        | hinge   | angle   |
|   | the thigh |           |         | igh_joint |         | (rad)   |
|   | joint     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | angle of  | -Inf      | Inf     | leg_joint | hinge   | angle   |
|   | the leg   |           |         |           |         | (rad)   |
|   | joint     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 4 | angle of  | -Inf      | Inf     | f         | hinge   | angle   |
|   | the foot  |           |         | oot_joint |         | (rad)   |
|   | joint     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 5 | velocity  | -Inf      | Inf     | rootx     | slide   | v       |
|   | of the    |           |         |           |         | elocity |
|   | x-c       |           |         |           |         | (m/s)   |
|   | oordinate |           |         |           |         |         |
|   | of the    |           |         |           |         |         |
|   | top       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 6 | velocity  | -Inf      | Inf     | rootz     | slide   | v       |
|   | of the    |           |         |           |         | elocity |
|   | z-c       |           |         |           |         | (m/s)   |
|   | oordinate |           |         |           |         |         |
|   | (height)  |           |         |           |         |         |
|   | of the    |           |         |           |         |         |
|   | top       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 7 | angular   | -Inf      | Inf     | rooty     | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | angle of  |           |         |           |         | (rad/s) |
|   | the top   |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 8 | angular   | -Inf      | Inf     | th        | hinge   | angular |
|   | velocity  |           |         | igh_joint |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | thigh     |           |         |           |         | (rad/s) |
|   | hinge     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 9 | angular   | -Inf      | Inf     | leg_joint | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | leg hinge |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angular   | -Inf      | Inf     | f         | hinge   | angular |
| 0 | velocity  |           |         | oot_joint |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | foot      |           |         |           |         | (rad/s) |
|   | hinge     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+

Rewards
~~~~~~~

The reward consists of three parts: - *healthy_reward*: Every timestep
that the hopper is healthy (see definition in section “Episode
Termination”), it gets a reward of fixed value ``healthy_reward``. -
*forward_reward*: A reward of hopping forward which is measured as
*``forward_reward_weight``* (x-coordinate before action - x-coordinate
after action)/dt\ *.*\ dt\* is the time between actions and is dependent
on the frame_skip parameter (fixed to 4), where the frametime is 0.002 -
making the default *dt = 4* 0.002 = 0.008\ *. This reward would be
positive if the hopper hops forward (positive x direction).
-*\ ctrl_cost\ *: A cost for penalising the hopper if it takes actions
that are too large. It is measured as*\ ``ctrl_cost_weight``
*sum(action2)* where *``ctrl_cost_weight``* is a parameter set for the
control and has a default value of 0.001

The total reward returned is **reward** *=* *healthy_reward +
forward_reward - ctrl_cost* and ``info`` will also contain the
individual reward terms

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0) with a uniform noise in the range of
[-``reset_noise_scale``, ``reset_noise_scale``] added to the values for
stochasticity.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The hopper is said to be unhealthy if any of the following happens:

1. An element of ``observation[1:]`` (if
   ``exclude_current_positions_from_observation=True``, else
   ``observation[2:]``) is no longer contained in the closed interval
   specified by the argument ``healthy_state_range``
2. The height of the hopper (``observation[0]`` if
   ``exclude_current_positions_from_observation=True``, else
   ``observation[1]``) is no longer contained in the closed interval
   specified by the argument ``healthy_z_range`` (usually meaning that
   it has fallen)
3. The angle (``observation[1]`` if
   ``exclude_current_positions_from_observation=True``, else
   ``observation[2]``) is no longer contained in the closed interval
   specified by the argument ``healthy_angle_range``

If ``terminate_when_unhealthy=True`` is passed during construction
(which is the default), the episode terminates when any of the following
happens:

1. The episode duration reaches a 1000 timesteps
2. The hopper is unhealthy

If ``terminate_when_unhealthy=False`` is passed, the episode is
terminated only when 1000 timesteps are exceeded.

Arguments
~~~~~~~~~

No additional arguments are currently supported in v2 and lower.

::

   env = gym.make('Hopper-v2')

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

::

   env = gym.make('Hopper-v3', ctrl_cost_weight=0.1, ....)

+--------------------+---------+------------+-------------------------+
| Parameter          | Type    | Default    | Description             |
+====================+=========+============+=========================+
| ``xml_file``       | **str** | ``"hop     | Path to a MuJoCo model  |
|                    |         | per.xml"`` |                         |
+--------------------+---------+------------+-------------------------+
| ``forwa            | **      | ``1.0``    | Weight for              |
| rd_reward_weight`` | float** |            | *forward_reward* term   |
|                    |         |            | (see section on reward) |
+--------------------+---------+------------+-------------------------+
| ``                 | **      | ``0.001``  | Weight for *ctrl_cost*  |
| ctrl_cost_weight`` | float** |            | reward (see section on  |
|                    |         |            | reward)                 |
+--------------------+---------+------------+-------------------------+
| ``healthy_reward`` | **      | ``1``      | Constant reward given   |
|                    | float** |            | if the ant is “healthy” |
|                    |         |            | after timestep          |
+--------------------+---------+------------+-------------------------+
| ``terminat         | *       | ``True``   | If true, issue a done   |
| e_when_unhealthy`` | *bool** |            | signal if the hopper is |
|                    |         |            | no longer healthy       |
+--------------------+---------+------------+-------------------------+
| ``hea              | **      | ``(-1      | The elements of         |
| lthy_state_range`` | tuple** | 00, 100)`` | ``observation[1:]`` (if |
|                    |         |            | ``excl                  |
|                    |         |            | ude_current_positions_f |
|                    |         |            | rom_observation=True``, |
|                    |         |            | else                    |
|                    |         |            | ``observation[2:]``)    |
|                    |         |            | must be in this range   |
|                    |         |            | for the hopper to be    |
|                    |         |            | considered healthy      |
+--------------------+---------+------------+-------------------------+
| `                  | **      | ``(        | The z-coordinate must   |
| `healthy_z_range`` | tuple** | 0.7, float | be in this range for    |
|                    |         | ("inf"))`` | the hopper to be        |
|                    |         |            | considered healthy      |
+--------------------+---------+------------+-------------------------+
| ``hea              | **      | ``(-0      | The angle given by      |
| lthy_angle_range`` | tuple** | .2, 0.2)`` | ``observation[1]`` (if  |
|                    |         |            | ``excl                  |
|                    |         |            | ude_current_positions_f |
|                    |         |            | rom_observation=True``, |
|                    |         |            | else                    |
|                    |         |            | ``observation[2]``)     |
|                    |         |            | must be in this range   |
|                    |         |            | for the hopper to be    |
|                    |         |            | considered healthy      |
+--------------------+---------+------------+-------------------------+
| ``r                | **      | ``5e-3``   | Scale of random         |
| eset_noise_scale`` | float** |            | perturbations of        |
|                    |         |            | initial position and    |
|                    |         |            | velocity (see section   |
|                    |         |            | on Starting State)      |
+--------------------+---------+------------+-------------------------+
| ``exclude_         | *       | ``True``   | Whether or not to omit  |
| current_positions_ | *bool** |            | the x-coordinate from   |
| from_observation`` |         |            | observations. Excluding |
|                    |         |            | the position can serve  |
|                    |         |            | as an inductive bias to |
|                    |         |            | induce                  |
|                    |         |            | position-agnostic       |
|                    |         |            | behavior in policies    |
+--------------------+---------+------------+-------------------------+

Version History
~~~~~~~~~~~~~~~

-  v3: support for gym.make kwargs such as xml_file, ctrl_cost_weight,
   reset_noise_scale etc. rgb rendering comes from tracking camera (so
   agent does not run away from screen)
-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks. Added
   reward_threshold to environments.
-  v0: Initial versions release (1.0.0)
