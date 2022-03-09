Reacher
=======

Description
~~~~~~~~~~~

“Reacher” is a two-jointed robot arm. The goal is to move the robot’s
end effector (called *fingertip*) close to a target that is spawned at a
random position.

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (2,), float32)``. An action
``(a, b)`` represents the torques applied at the hinge joints.

+---+-------------------------------------+-----+-----+-----------+---+---+
| N | Action                              | C   | C   | Name (in  | J | U |
| u |                                     | ont | ont | corr      | o | n |
| m |                                     | rol | rol | esponding | i | i |
|   |                                     | Min | Max | XML file) | n | t |
|   |                                     |     |     |           | t |   |
+===+=====================================+=====+=====+===========+===+===+
| 0 | Torque applied at the first hinge   | -1  | 1   | joint0    | h | t |
|   | (connecting the link to the point   |     |     |           | i | o |
|   | of fixture)                         |     |     |           | n | r |
|   |                                     |     |     |           | g | q |
|   |                                     |     |     |           | e | u |
|   |                                     |     |     |           |   | e |
|   |                                     |     |     |           |   | ( |
|   |                                     |     |     |           |   | N |
|   |                                     |     |     |           |   | m |
|   |                                     |     |     |           |   | ) |
+---+-------------------------------------+-----+-----+-----------+---+---+
| 1 | Torque applied at the second hinge  | -1  | 1   | joint1    | h | t |
|   | (connecting the two links)          |     |     |           | i | o |
|   |                                     |     |     |           | n | r |
|   |                                     |     |     |           | g | q |
|   |                                     |     |     |           | e | u |
|   |                                     |     |     |           |   | e |
|   |                                     |     |     |           |   | ( |
|   |                                     |     |     |           |   | N |
|   |                                     |     |     |           |   | m |
|   |                                     |     |     |           |   | ) |
+---+-------------------------------------+-----+-----+-----------+---+---+

Observation Space
~~~~~~~~~~~~~~~~~

Observations consist of

-  The cosine of the angles of the two arms
-  The sine of the angles of the two arms
-  The coordinates of the target
-  The angular velocities of the arms
-  The vector between the target and the reacher’s fingertip (3
   dimensional with the last element being 0)

The observation is a ``ndarray`` with shape ``(11,)`` where the elements
correspond to the following:

+---+-----------+-----------+---------+-----------+---------+---------+
| N | Ob        | Min       | Max     | Name (in  | Joint   | Unit    |
| u | servation |           |         | corr      |         |         |
| m |           |           |         | esponding |         |         |
|   |           |           |         | XML file) |         |         |
+===+===========+===========+=========+===========+=========+=========+
| 0 | cosine of | -Inf      | Inf     | co        | hinge   | u       |
|   | the angle |           |         | s(joint0) |         | nitless |
|   | of the    |           |         |           |         |         |
|   | first arm |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | cosine of | -Inf      | Inf     | co        | hinge   | u       |
|   | the angle |           |         | s(joint1) |         | nitless |
|   | of the    |           |         |           |         |         |
|   | second    |           |         |           |         |         |
|   | arm       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | sine of   | -Inf      | Inf     | co        | hinge   | u       |
|   | the angle |           |         | s(joint0) |         | nitless |
|   | of the    |           |         |           |         |         |
|   | first arm |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | sine of   | -Inf      | Inf     | co        | hinge   | u       |
|   | the angle |           |         | s(joint1) |         | nitless |
|   | of the    |           |         |           |         |         |
|   | second    |           |         |           |         |         |
|   | arm       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 4 | x-co      | -Inf      | Inf     | target_x  | slide   | p       |
|   | orddinate |           |         |           |         | osition |
|   | of the    |           |         |           |         | (m)     |
|   | target    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 5 | y-co      | -Inf      | Inf     | target_y  | slide   | p       |
|   | orddinate |           |         |           |         | osition |
|   | of the    |           |         |           |         | (m)     |
|   | target    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 6 | angular   | -Inf      | Inf     | joint0    | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | first arm |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 7 | angular   | -Inf      | Inf     | joint1    | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of the    |           |         |           |         | elocity |
|   | second    |           |         |           |         | (rad/s) |
|   | arm       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 8 | x-value   | -Inf      | Inf     | NA        | slide   | p       |
|   | of        |           |         |           |         | osition |
|   | position_ |           |         |           |         | (m)     |
|   | fingertip |           |         |           |         |         |
|   | -         |           |         |           |         |         |
|   | positi    |           |         |           |         |         |
|   | on_target |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 9 | y-value   | -Inf      | Inf     | NA        | slide   | p       |
|   | of        |           |         |           |         | osition |
|   | position_ |           |         |           |         | (m)     |
|   | fingertip |           |         |           |         |         |
|   | -         |           |         |           |         |         |
|   | positi    |           |         |           |         |         |
|   | on_target |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | z-value   | -Inf      | Inf     | NA        | slide   | p       |
| 0 | of        |           |         |           |         | osition |
|   | position_ |           |         |           |         | (m)     |
|   | fingertip |           |         |           |         |         |
|   | -         |           |         |           |         |         |
|   | positi    |           |         |           |         |         |
|   | on_target |           |         |           |         |         |
|   | (0 since  |           |         |           |         |         |
|   | reacher   |           |         |           |         |         |
|   | is 2d and |           |         |           |         |         |
|   | z is same |           |         |           |         |         |
|   | for both) |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+

Most Gym environments just return the positions and velocity of the
joints in the ``.xml`` file as the state of the environment. However, in
reacher the state is created by combining only certain elements of the
position and velocity, and performing some function transformations on
them. If one is to read the ``.xml`` for reacher then they will find 4
joints:

+---+-----------------+-----+-----+--------------------+---+-----------+
| N | Observation     | Min | Max | Name (in           | J | Unit      |
| u |                 |     |     | corresponding XML  | o |           |
| m |                 |     |     | file)              | i |           |
|   |                 |     |     |                    | n |           |
|   |                 |     |     |                    | t |           |
+===+=================+=====+=====+====================+===+===========+
| 0 | angle of the    | -   | Inf | joint0             | h | angle     |
|   | first arm       | Inf |     |                    | i | (rad)     |
|   |                 |     |     |                    | n |           |
|   |                 |     |     |                    | g |           |
|   |                 |     |     |                    | e |           |
+---+-----------------+-----+-----+--------------------+---+-----------+
| 1 | angle of the    | -   | Inf | joint1             | h | angle     |
|   | second arm      | Inf |     |                    | i | (rad)     |
|   |                 |     |     |                    | n |           |
|   |                 |     |     |                    | g |           |
|   |                 |     |     |                    | e |           |
+---+-----------------+-----+-----+--------------------+---+-----------+
| 2 | x-coordinate of | -   | Inf | target_x           | s | position  |
|   | the target      | Inf |     |                    | l | (m)       |
|   |                 |     |     |                    | i |           |
|   |                 |     |     |                    | d |           |
|   |                 |     |     |                    | e |           |
+---+-----------------+-----+-----+--------------------+---+-----------+
| 3 | y-coordinate of | -   | Inf | target_y           | s | position  |
|   | the target      | Inf |     |                    | l | (m)       |
|   |                 |     |     |                    | i |           |
|   |                 |     |     |                    | d |           |
|   |                 |     |     |                    | e |           |
+---+-----------------+-----+-----+--------------------+---+-----------+

Rewards
~~~~~~~

The reward consists of two parts: - *reward_distance*: This reward is a
measure of how far the *fingertip* of the reacher (the unattached end)
is from the target, with a more negative value assigned for when the
reacher’s *fingertip* is further away from the target. It is calculated
as the negative vector norm of (position of the fingertip - position of
target), or *-norm(“fingertip” - “target”)*. - *reward_control*: A
negative reward for penalising the walker if it takes actions that are
too large. It is measured as the negative squared Euclidean norm of the
action, i.e. as *- sum(action2)*.

The total reward returned is **reward** *=* *reward_distance +
reward_control*

Unlike other environments, Reacher does not allow you to specify weights
for the individual reward terms. However, ``info`` does contain the keys
*reward_dist* and *reward_ctrl*. Thus, if you’d like to weight the
terms, you should create a wrapper that computes the weighted reward
from ``info``.

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0) with a noise added for stochasticity. A uniform noise in
the range [-0.1, 0.1] is added to the positional attributes, while the
target position is selected uniformly at random in a disk of radius 0.2
around the origin. Independent, uniform noise in the range of [-0.005,
0.005] is added to the velocities, and the last element (“fingertip” -
“target”) is calculated at the end once everything is set. The default
setting has a framerate of 2 and a *dt = 2* 0.01 = 0.02\*

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when any of the following happens:

1. The episode duration reaches a 50 timesteps (with a new random target
   popping up if the reacher’s fingertip reaches it before 50 timesteps)
2. Any of the state space values is no longer finite.

Arguments
~~~~~~~~~

No additional arguments are currently supported (in v2 and lower), but
modifications can be made to the XML file in the assets folder (or by
changing the path to a modified XML file in another folder)..

::

   env = gym.make('Reacher-v2')

There is no v3 for Reacher, unlike the robot environments where a v3 and
beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

Version History
~~~~~~~~~~~~~~~

-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks (not
   including reacher, which has a max_time_steps of 50). Added
   reward_threshold to environments.
-  v0: Initial versions release (1.0.0)
