InvertedDoublePendulum
======================

Description
~~~~~~~~~~~

This environment originates from control theory and builds on the
cartpole environment based on the work done by Barto, Sutton, and
Anderson in `“Neuronlike adaptive elements that can solve difficult
learning control
problems” <https://ieeexplore.ieee.org/document/6313077>`__, powered by
the Mujoco physics simulator - allowing for more complex experiments
(such as varying the effects of gravity or constraints). This
environment involves a cart that can moved linearly, with a pole fixed
on it and a second pole fixed on the other end of the first one (leaving
the second pole as the only one with one free end). The cart can be
pushed left or right, and the goal is to balance the second pole on top
of the first pole, which is in turn on top of the cart, by applying
continuous forces on the cart.

Action Space
~~~~~~~~~~~~

The agent take a 1-element vector for actions. The action space is a
continuous ``(action)`` in ``[-1, 1]``, where ``action`` represents the
numerical force applied to the cart (with magnitude representing the
amount of force and sign representing the direction)

+---+----------------+-------+-------+---------------------+---+------+
| N | Action         | Co    | Co    | Name (in            | J | Unit |
| u |                | ntrol | ntrol | corresponding XML   | o |      |
| m |                | Min   | Max   | file)               | i |      |
|   |                |       |       |                     | n |      |
|   |                |       |       |                     | t |      |
+===+================+=======+=======+=====================+===+======+
| 0 | Force applied  | -1    | 1     | slider              | s | F    |
|   | on the cart    |       |       |                     | l | orce |
|   |                |       |       |                     | i | (N)  |
|   |                |       |       |                     | d |      |
|   |                |       |       |                     | e |      |
+---+----------------+-------+-------+---------------------+---+------+

Observation Space
~~~~~~~~~~~~~~~~~

The state space consists of positional values of different body parts of
the pendulum system, followed by the velocities of those individual
parts (their derivatives) with all the positions ordered before all the
velocities.

The observation is a ``ndarray`` with shape ``(11,)`` where the elements
correspond to the following:

+---+-----------+-----------+---------+-----------+---------+---------+
| N | Ob        | Min       | Max     | Name (in  | Joint   | Unit    |
| u | servation |           |         | corr      |         |         |
| m |           |           |         | esponding |         |         |
|   |           |           |         | XML file) |         |         |
+===+===========+===========+=========+===========+=========+=========+
| 0 | position  | -Inf      | Inf     | slider    | slide   | p       |
|   | of the    |           |         |           |         | osition |
|   | cart      |           |         |           |         | (m)     |
|   | along the |           |         |           |         |         |
|   | linear    |           |         |           |         |         |
|   | surface   |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | sine of   | -Inf      | Inf     | s         | hinge   | u       |
|   | the angle |           |         | in(hinge) |         | nitless |
|   | between   |           |         |           |         |         |
|   | the cart  |           |         |           |         |         |
|   | and the   |           |         |           |         |         |
|   | first     |           |         |           |         |         |
|   | pole      |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | sine of   | -Inf      | Inf     | si        | hinge   | u       |
|   | the angle |           |         | n(hinge2) |         | nitless |
|   | between   |           |         |           |         |         |
|   | the two   |           |         |           |         |         |
|   | poles     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | cosine of | -Inf      | Inf     | c         | hinge   | u       |
|   | the angle |           |         | os(hinge) |         | nitless |
|   | between   |           |         |           |         |         |
|   | the cart  |           |         |           |         |         |
|   | and the   |           |         |           |         |         |
|   | first     |           |         |           |         |         |
|   | pole      |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 4 | cosine of | -Inf      | Inf     | co        | hinge   | u       |
|   | the angle |           |         | s(hinge2) |         | nitless |
|   | between   |           |         |           |         |         |
|   | the two   |           |         |           |         |         |
|   | poles     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 5 | velocity  | -Inf      | Inf     | slider    | slide   | v       |
|   | of the    |           |         |           |         | elocity |
|   | cart      |           |         |           |         | (m/s)   |
+---+-----------+-----------+---------+-----------+---------+---------+
| 6 | angular   | -Inf      | Inf     | hinge     | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | angle     |           |         |           |         | (rad/s) |
|   | between   |           |         |           |         |         |
|   | the cart  |           |         |           |         |         |
|   | and the   |           |         |           |         |         |
|   | first     |           |         |           |         |         |
|   | pole      |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 7 | angular   | -Inf      | Inf     | hinge2    | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | angle     |           |         |           |         | (rad/s) |
|   | between   |           |         |           |         |         |
|   | the two   |           |         |           |         |         |
|   | poles     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 8 | c         | -Inf      | Inf     |           |         | Force   |
|   | onstraint |           |         |           |         | (N)     |
|   | force - 1 |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 9 | c         | -Inf      | Inf     |           |         | Force   |
|   | onstraint |           |         |           |         | (N)     |
|   | force - 2 |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | c         | -Inf      | Inf     |           |         | Force   |
| 0 | onstraint |           |         |           |         | (N)     |
|   | force - 3 |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+

There is physical contact between the robots and their environment - and
Mujoco attempts at getting realisitic physics simulations for the
possible physical contact dynamics by aiming for physical accuracy and
computational efficiency.

There is one constraint force for contacts for each degree of freedom
(3). The approach and handling of constraints by Mujoco is unique to the
simulator and is based on their research. Once can find more information
in their
`documentation <https://mujoco.readthedocs.io/en/latest/computation.html>`__
or in their paper `“Analytically-invertible dynamics with contacts and
constraints: Theory and implementation in
MuJoCo” <https://homes.cs.washington.edu/~todorov/papers/TodorovICRA14.pdf>`__.

Rewards
~~~~~~~

The reward consists of two parts: - *alive_bonus*: The goal is to make
the second inverted pendulum stand upright (within a certain angle
limit) as long as possible - as such a reward of +10 is awarded for each
timestep that the second pole is upright. - *distance_penalty*: This
reward is a measure of how far the *tip* of the second pendulum (the
only free end) moves, and it is calculated as *0.01* x2 + (y - 2)2\ *,
where*\ x\* is the x-coordinate of the tip and *y* is the y-coordinate
of the tip of the second pole. - *velocity_penalty*: A negative reward
for penalising the agent if it moves too fast *0.001* v12 + 0.005 \* v2
2\*

The total reward returned is **reward** *=* *alive_bonus -
distance_penalty - velocity_penalty*

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0) with a uniform noise in the range of [-0.1, 0.1] added to
the positional values (cart position and pole angles) and standard
normal force with a standard deviation of 0.1 added to the velocity
values for stochasticity.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when any of the following happens:

1. The episode duration reaches 1000 timesteps.
2. Any of the state space values is no longer finite.
3. The y_coordinate of the tip of the second pole *is less than or
   equal* to 1. The maximum standing height of the system is 1.196 m
   when all the parts are perpendicularly vertical on top of each
   other).

Arguments
~~~~~~~~~

No additional arguments are currently supported.

::

   env = gym.make('InvertedDoublePendulum-v2')

There is no v3 for InvertedPendulum, unlike the robot environments where
a v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

Version History
~~~~~~~~~~~~~~~

-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks (including
   inverted pendulum)
-  v0: Initial versions release (1.0.0)
