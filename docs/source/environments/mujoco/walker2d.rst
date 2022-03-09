Walker2d
========

Description
~~~~~~~~~~~

This environment builds on the hopper environment based on the work done
by Erez, Tassa, and Todorov in `“Infinite Horizon Model Predictive
Control for Nonlinear Periodic
Tasks” <http://www.roboticsproceedings.org/rss07/p10.pdf>`__ by adding
another set of legs making it possible for the robot to walker forward
instead of hop. Like other Mujoco environments, this environment aims to
increase the number of independent state and control variables as
compared to the classic control environments. The walker is a
two-dimensional two-legged figure that consist of four main body parts -
a single torso at the top (with the two legs splitting after the torso),
two thighs in the middle below the torso, two legs in the bottom below
the thighs, and two feet attached to the legs on which the entire body
rests. The goal is to make coordinate both sets of feet, legs, and
thighs to move in the forward (right) direction by applying torques on
the six hinges connecting the six body parts.

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (6,), float32)``. An action
represents the torques applied at the hinge joints.

+---+---------------------+------+------+------------------+---+-------+
| N | Action              | Con  | Con  | Name (in         | J | Unit  |
| u |                     | trol | trol | corresponding    | o |       |
| m |                     | Min  | Max  | XML file)        | i |       |
|   |                     |      |      |                  | n |       |
|   |                     |      |      |                  | t |       |
+===+=====================+======+======+==================+===+=======+
| 0 | Torque applied on   | -1   | 1    | thigh_joint      | h | t     |
|   | the thigh rotor     |      |      |                  | i | orque |
|   |                     |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+
| 1 | Torque applied on   | -1   | 1    | leg_joint        | h | t     |
|   | the leg rotor       |      |      |                  | i | orque |
|   |                     |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+
| 2 | Torque applied on   | -1   | 1    | foot_joint       | h | t     |
|   | the foot rotor      |      |      |                  | i | orque |
|   |                     |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+
| 3 | Torque applied on   | -1   | 1    | thigh_left_joint | h | t     |
|   | the left thigh      |      |      |                  | i | orque |
|   | rotor               |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+
| 4 | Torque applied on   | -1   | 1    | leg_left_joint   | h | t     |
|   | the left leg rotor  |      |      |                  | i | orque |
|   |                     |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+
| 5 | Torque applied on   | -1   | 1    | foot_left_joint  | h | t     |
|   | the left foot rotor |      |      |                  | i | orque |
|   |                     |      |      |                  | n | (N m) |
|   |                     |      |      |                  | g |       |
|   |                     |      |      |                  | e |       |
+---+---------------------+------+------+------------------+---+-------+

Observation Space
~~~~~~~~~~~~~~~~~

Observations consist of positional values of different body parts of the
walker, followed by the velocities of those individual parts (their
derivatives) with all the positions ordered before all the velocities.

By default, observations do not include the x-coordinate of the top. It
may be included by passing
``exclude_current_positions_from_observation=False`` during
construction. In that case, the observation space will have 18
dimensions where the first dimension represent the x-coordinates of the
top of the walker. Regardless of whether
``exclude_current_positions_from_observation`` was set to true or false,
the x-coordinate of the top will be returned in ``info`` with key
``"x_position"``.

By default, observation is a ``ndarray`` with shape ``(17,)`` where the
elements correspond to the following:

+---+--------------------------+------+-------+------------------+---+---+
| N | Observation              | Min  | Max   | Name (in         | J | U |
| u |                          |      |       | corresponding    | o | n |
| m |                          |      |       | XML file)        | i | i |
|   |                          |      |       |                  | n | t |
|   |                          |      |       |                  | t |   |
+===+==========================+======+=======+==================+===+===+
| 0 | z-coordinate of the top  | -Inf | Inf   | rootz (torso)    | s | p |
|   | (height of hopper)       |      |       |                  | l | o |
|   |                          |      |       |                  | i | s |
|   |                          |      |       |                  | d | i |
|   |                          |      |       |                  | e | t |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | n |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angle of the top         | -Inf | Inf   | rooty (torso)    | h | a |
|   |                          |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | angle of the thigh joint | -Inf | Inf   | thigh_joint      | h | a |
|   |                          |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 3 | angle of the leg joint   | -Inf | Inf   | leg_joint        | h | a |
|   |                          |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 4 | angle of the foot joint  | -Inf | Inf   | foot_joint       | h | a |
|   |                          |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 5 | angle of the left thigh  | -Inf | Inf   | thigh_left_joint | h | a |
|   | joint                    |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 6 | angle of the left leg    | -Inf | Inf   | leg_left_joint   | h | a |
|   | joint                    |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 7 | angle of the left foot   | -Inf | Inf   | foot_left_joint  | h | a |
|   | joint                    |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 8 | velocity of the          | -Inf | Inf   | rootx            | s | v |
|   | x-coordinate of the top  |      |       |                  | l | e |
|   |                          |      |       |                  | i | l |
|   |                          |      |       |                  | d | o |
|   |                          |      |       |                  | e | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 9 | velocity of the          | -Inf | Inf   | rootz            | s | v |
|   | z-coordinate (height) of |      |       |                  | l | e |
|   | the top                  |      |       |                  | i | l |
|   |                          |      |       |                  | d | o |
|   |                          |      |       |                  | e | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | rooty            | h | a |
| 0 | angle of the top         |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | thigh_joint      | h | a |
| 1 | thigh hinge              |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | leg_joint        | h | a |
| 2 | leg hinge                |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | foot_joint       | h | a |
| 3 | foot hinge               |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | thigh_left_joint | h | a |
| 4 | thigh hinge              |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | leg_left_joint   | h | a |
| 5 | leg hinge                |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angular velocity of the  | -Inf | Inf   | foot_left_joint  | h | a |
| 6 | foot hinge               |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | u |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | v |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | l |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+

Rewards
~~~~~~~

The reward consists of three parts: - *healthy_reward*: Every timestep
that the walker is alive, it receives a fixed reward of value
``healthy_reward``, - *forward_reward*: A reward of walking forward
which is measured as *``forward_reward_weight``* (x-coordinate before
action - x-coordinate after action)/dt\ *.*\ dt\* is the time between
actions and is dependeent on the frame_skip parameter (default is 4),
where the frametime is 0.002 - making the default *dt = 4* 0.002 =
0.008\ *. This reward would be positive if the walker walks forward
(right) desired. -*\ ctrl_cost\ *: A cost for penalising the walker if
it takes actions that are too large. It is measured
as*\ ``ctrl_cost_weight`` \* sum(action2)\* where *``ctrl_cost_weight``*
is a parameter set for the control and has a default value of 0.001

The total reward returned is **reward** *=* *healthy_reward bonus +
forward_reward - ctrl_cost* and ``info`` will also contain the
individual reward terms

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) with a uniform noise
in the range of [-``reset_noise_scale``, ``reset_noise_scale``] added to
the values for stochasticity.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The walker is said to be unhealthy if any of the following happens:

1. Any of the state space values is no longer finite
2. The height of the walker is **not** in the closed interval specified
   by ``healthy_z_range``
3. The absolute value of the angle (``observation[1]`` if
   ``exclude_current_positions_from_observation=False``, else
   ``observation[2]``) is **not** in the closed interval specified by
   ``healthy_angle_range``

If ``terminate_when_unhealthy=True`` is passed during construction
(which is the default), the episode terminates when any of the following
happens:

1. The episode duration reaches a 1000 timesteps
2. The walker is unhealthy

If ``terminate_when_unhealthy=False`` is passed, the episode is
terminated only when 1000 timesteps are exceeded.

Arguments
~~~~~~~~~

No additional arguments are currently supported in v2 and lower.

::

   env = gym.make('Walker2d-v2')

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

::

   env = gym.make('Walker2d-v3', ctrl_cost_weight=0.1, ....)

+--------------------+---------+-----------+--------------------------+
| Parameter          | Type    | Default   | Description              |
+====================+=========+===========+==========================+
| ``xml_file``       | **str** | ``"walker | Path to a MuJoCo model   |
|                    |         | 2d.xml"`` |                          |
+--------------------+---------+-----------+--------------------------+
| ``forwa            | **      | ``1.0``   | Weight for               |
| rd_reward_weight`` | float** |           | *forward_reward* term    |
|                    |         |           | (see section on reward)  |
+--------------------+---------+-----------+--------------------------+
| ``                 | **      | ``1e-3``  | Weight for *ctr_cost*    |
| ctrl_cost_weight`` | float** |           | term (see section on     |
|                    |         |           | reward)                  |
+--------------------+---------+-----------+--------------------------+
| ``healthy_reward`` | **      | ``1.0``   | Constant reward given if |
|                    | float** |           | the ant is “healthy”     |
|                    |         |           | after timestep           |
+--------------------+---------+-----------+--------------------------+
| ``terminat         | *       | ``True``  | If true, issue a done    |
| e_when_unhealthy`` | *bool** |           | signal if the            |
|                    |         |           | z-coordinate of the      |
|                    |         |           | walker is no longer      |
|                    |         |           | healthy                  |
+--------------------+---------+-----------+--------------------------+
| `                  | **      | ``(       | The z-coordinate of the  |
| `healthy_z_range`` | tuple** | 0.8, 2)`` | top of the walker must   |
|                    |         |           | be in this range to be   |
|                    |         |           | considered healthy       |
+--------------------+---------+-----------+--------------------------+
| ``hea              | **      | ``        | The angle must be in     |
| lthy_angle_range`` | tuple** | (-1, 1)`` | this range to be         |
|                    |         |           | considered healthy       |
+--------------------+---------+-----------+--------------------------+
| ``r                | **      | ``5e-3``  | Scale of random          |
| eset_noise_scale`` | float** |           | perturbations of initial |
|                    |         |           | position and velocity    |
|                    |         |           | (see section on Starting |
|                    |         |           | State)                   |
+--------------------+---------+-----------+--------------------------+
| ``exclude_         | *       | ``True``  | Whether or not to omit   |
| current_positions_ | *bool** |           | the x-coordinate from    |
| from_observation`` |         |           | observations. Excluding  |
|                    |         |           | the position can serve   |
|                    |         |           | as an inductive bias to  |
|                    |         |           | induce position-agnostic |
|                    |         |           | behavior in policies     |
+--------------------+---------+-----------+--------------------------+

Version History
~~~~~~~~~~~~~~~

-  v3: support for gym.make kwargs such as xml_file, ctrl_cost_weight,
   reset_noise_scale etc. rgb rendering comes from tracking camera (so
   agent does not run away from screen)
-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks. Added
   reward_threshold to environments.
-  v0: Initial versions release (1.0.0)
