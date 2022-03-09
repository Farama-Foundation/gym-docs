InvertedPendulum
================

Description
~~~~~~~~~~~

This environment is the cartpole environment based on the work done by
Barto, Sutton, and Anderson in `“Neuronlike adaptive elements that can
solve difficult learning control
problems” <https://ieeexplore.ieee.org/document/6313077>`__, just like
in the classic environments but now powered by the Mujoco physics
simulator - allowing for more complex experiments (such as varying the
effects of gravity). This environment involves a cart that can moved
linearly, with a pole fixed on it at one end and having another end
free. The cart can be pushed left or right, and the goal is to balance
the pole on the top of the cart by applying forces on the cart.

Action Space
~~~~~~~~~~~~

The agent take a 1-element vector for actions.

The action space is a continuous ``(action)`` in ``[-3, 3]``, where
``action`` represents the numerical force applied to the cart (with
magnitude representing the amount of force and sign representing the
direction)

+---+----------------+-------+-------+---------------------+---+------+
| N | Action         | Co    | Co    | Name (in            | J | Unit |
| u |                | ntrol | ntrol | corresponding XML   | o |      |
| m |                | Min   | Max   | file)               | i |      |
|   |                |       |       |                     | n |      |
|   |                |       |       |                     | t |      |
+===+================+=======+=======+=====================+===+======+
| 0 | Force applied  | -3    | 3     | slider              | s | F    |
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

The observation is a ``ndarray`` with shape ``(4,)`` where the elements
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
| 1 | vertical  | -Inf      | Inf     | hinge     | hinge   | angle   |
|   | angle of  |           |         |           |         | (rad)   |
|   | the pole  |           |         |           |         |         |
|   | on the    |           |         |           |         |         |
|   | cart      |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | linear    | -Inf      | Inf     | slider    | slide   | v       |
|   | velocity  |           |         |           |         | elocity |
|   | of the    |           |         |           |         | (m/s)   |
|   | cart      |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | angular   | -Inf      | Inf     | hinge     | hinge   | a       |
|   | velocity  |           |         |           |         | nglular |
|   | of the    |           |         |           |         | v       |
|   | pole on   |           |         |           |         | elocity |
|   | the cart  |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+

Rewards
~~~~~~~

The goal is to make the inverted pendulum stand upright (within a
certain angle limit) as long as possible - as such a reward of +1 is
awarded for each timestep that the pole is upright.

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.0, 0.0) with a uniform
noise in the range of [-0.01, 0.01] added to the values for
stochasticity.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when any of the following happens:

1. The episode duration reaches 1000 timesteps.
2. Any of the state space values is no longer finite.
3. The absolutely value of the vertical angle between the pole and the
   cart is greater than 0.2 radian.

Arguments
~~~~~~~~~

No additional arguments are currently supported.

::

   env = gym.make('InvertedPendulum-v2')

There is no v3 for InvertedPendulum, unlike the robot environments where
a v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

Version History
~~~~~~~~~~~~~~~

-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks (including
   inverted pendulum)
-  v0: Initial versions release (1.0.0)
