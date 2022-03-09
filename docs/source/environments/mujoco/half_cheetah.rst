HalfCheetah
===========

Description
~~~~~~~~~~~

This environment is based on the work by P. Wawrzy´nski in `“A Cat-Like
Robot Real-Time Learning to
Run” <http://staff.elka.pw.edu.pl/~pwawrzyn/pub-s/0812_LSCLRR.pdf>`__.
The HalfCheetah is a 2-dimensional robot consisting of 9 links and 8
joints connecting them (including two paws). The goal is to apply a
torque on the joints to make the cheetah run forward (right) as fast as
possible, with a positive reward allocated based on the distance moved
forward and a negative reward allocated for moving backward. The torso
and head of the cheetah are fixed, and the torque can only be applied on
the other 6 joints over the front and back thighs (connecting to the
torso), shins (connecting to the thighs) and feet (connecting to the
shins).

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (6,), float32)``. An action
represents the torques applied between *links*.

+---+--------------------+-------+--------+--------------------+---+---+
| N | Action             | Co    | C      | Name (in           | J | U |
| u |                    | ntrol | ontrol | corresponding XML  | o | n |
| m |                    | Min   | Max    | file)              | i | i |
|   |                    |       |        |                    | n | t |
|   |                    |       |        |                    | t |   |
+===+====================+=======+========+====================+===+===+
| 0 | Torque applied on  | -1    | 1      | bthigh             | h | t |
|   | the back thigh     |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+
| 1 | Torque applied on  | -1    | 1      | bshin              | h | t |
|   | the back shin      |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+
| 2 | Torque applied on  | -1    | 1      | bfoot              | h | t |
|   | the back foot      |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+
| 3 | Torque applied on  | -1    | 1      | fthigh             | h | t |
|   | the front thigh    |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+
| 4 | Torque applied on  | -1    | 1      | fshin              | h | t |
|   | the front shin     |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+
| 5 | Torque applied on  | -1    | 1      | ffoot              | h | t |
|   | the front foot     |       |        |                    | i | o |
|   | rotor              |       |        |                    | n | r |
|   |                    |       |        |                    | g | q |
|   |                    |       |        |                    | e | u |
|   |                    |       |        |                    |   | e |
|   |                    |       |        |                    |   | ( |
|   |                    |       |        |                    |   | N |
|   |                    |       |        |                    |   | m |
|   |                    |       |        |                    |   | ) |
+---+--------------------+-------+--------+--------------------+---+---+

Observation Space
~~~~~~~~~~~~~~~~~

Observations consist of positional values of different body parts of the
cheetah, followed by the velocities of those individual parts (their
derivatives) with all the positions ordered before all the velocities.

By default, observations do not include the x-coordinate of the
cheetah’s center of mass. It may be included by passing
``exclude_current_positions_from_observation=False`` during
construction. In that case, the observation space will have 18
dimensions where the first dimension represents the x-coordinate of the
cheetah’s center of mass. Regardless of whether
``exclude_current_positions_from_observation`` was set to true or false,
the x-coordinate will be returned in ``info`` with key ``"x_position"``.

However, by default, the observation is a ``ndarray`` with shape
``(17,)`` where the elements correspond to the following:

+---+-----------+-----------+---------+-----------+---------+---------+
| N | Ob        | Min       | Max     | Name (in  | Joint   | Unit    |
| u | servation |           |         | corr      |         |         |
| m |           |           |         | esponding |         |         |
|   |           |           |         | XML file) |         |         |
+===+===========+===========+=========+===========+=========+=========+
| 0 | z-c       | -Inf      | Inf     | rootz     | slide   | p       |
|   | oordinate |           |         |           |         | osition |
|   | of the    |           |         |           |         | (m)     |
|   | front tip |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | rooty     | hinge   | angle   |
|   | the front |           |         |           |         | (rad)   |
|   | tip       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | angle of  | -Inf      | Inf     | bthigh    | hinge   | angle   |
|   | the       |           |         |           |         | (rad)   |
|   | second    |           |         |           |         |         |
|   | rotor     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | angle of  | -Inf      | Inf     | bshin     | hinge   | angle   |
|   | the       |           |         |           |         | (rad)   |
|   | second    |           |         |           |         |         |
|   | rotor     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 4 | velocity  | -Inf      | Inf     | bfoot     | hinge   | angle   |
|   | of the    |           |         |           |         | (rad)   |
|   | tip along |           |         |           |         |         |
|   | the       |           |         |           |         |         |
|   | x-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 5 | velocity  | -Inf      | Inf     | fthigh    | hinge   | angle   |
|   | of the    |           |         |           |         | (rad)   |
|   | tip along |           |         |           |         |         |
|   | the       |           |         |           |         |         |
|   | y-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 6 | angular   | -Inf      | Inf     | fshin     | hinge   | angle   |
|   | velocity  |           |         |           |         | (rad)   |
|   | of front  |           |         |           |         |         |
|   | tip       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 7 | angular   | -Inf      | Inf     | ffoot     | hinge   | angle   |
|   | velocity  |           |         |           |         | (rad)   |
|   | of second |           |         |           |         |         |
|   | rotor     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 8 | x-c       | -Inf      | Inf     | rootx     | slide   | v       |
|   | oordinate |           |         |           |         | elocity |
|   | of the    |           |         |           |         | (m/s)   |
|   | front tip |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 9 | y-c       | -Inf      | Inf     | rootz     | slide   | v       |
|   | oordinate |           |         |           |         | elocity |
|   | of the    |           |         |           |         | (m/s)   |
|   | front tip |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | rooty     | hinge   | angular |
| 0 | the front |           |         |           |         | v       |
|   | tip       |           |         |           |         | elocity |
|   |           |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | bthigh    | hinge   | angular |
| 1 | the       |           |         |           |         | v       |
|   | second    |           |         |           |         | elocity |
|   | rotor     |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | bshin     | hinge   | angular |
| 2 | the       |           |         |           |         | v       |
|   | second    |           |         |           |         | elocity |
|   | rotor     |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | velocity  | -Inf      | Inf     | bfoot     | hinge   | angular |
| 3 | of the    |           |         |           |         | v       |
|   | tip along |           |         |           |         | elocity |
|   | the       |           |         |           |         | (rad/s) |
|   | x-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | velocity  | -Inf      | Inf     | fthigh    | hinge   | angular |
| 4 | of the    |           |         |           |         | v       |
|   | tip along |           |         |           |         | elocity |
|   | the       |           |         |           |         | (rad/s) |
|   | y-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angular   | -Inf      | Inf     | fshin     | hinge   | angular |
| 5 | velocity  |           |         |           |         | v       |
|   | of front  |           |         |           |         | elocity |
|   | tip       |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angular   | -Inf      | Inf     | ffoot     | hinge   | angular |
| 6 | velocity  |           |         |           |         | v       |
|   | of second |           |         |           |         | elocity |
|   | rotor     |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+

Rewards
~~~~~~~

The reward consists of two parts: - *forward_reward*: A reward of moving
forward which is measured as *``forward_reward_weight``* (x-coordinate
before action - x-coordinate after action)/dt\ *.*\ dt\* is the time
between actions and is dependent on the frame_skip parameter (fixed to
5), where the frametime is 0.01 - making the default *dt = 5* 0.01 =
0.05\ *. This reward would be positive if the cheetah runs forward
(right). -*\ ctrl_cost\ *: A cost for penalising the cheetah if it takes
actions that are too large. It is measured as*\ ``ctrl_cost_weight``
*sum(action2)* where *``ctrl_cost_weight``* is a parameter set for the
control and has a default value of 0.1

The total reward returned is **reward** *=* *forward_reward - ctrl_cost*
and ``info`` will also contain the individual reward terms

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,) with a noise added to the
initial state for stochasticity. As seen before, the first 8 values in
the state are positional and the last 9 values are velocity. A uniform
noise in the range of [-``reset_noise_scale``, ``reset_noise_scale``] is
added to the positional values while a standard normal noise with a mean
of 0 and standard deviation of ``reset_noise_scale`` is added to the
initial velocity values of all zeros.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when the episode length is greater than 1000.

Arguments
~~~~~~~~~

No additional arguments are currently supported in v2 and lower.

::

   env = gym.make('HalfCheetah-v2')

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

::

   env = gym.make('HalfCheetah-v3', ctrl_cost_weight=0.1, ....)

+-------------------+--------+----------------+-----------------------+
| Parameter         | Type   | Default        | Description           |
+===================+========+================+=======================+
| ``xml_file``      | *      | ``"half_       | Path to a MuJoCo      |
|                   | *str** | cheetah.xml"`` | model                 |
+-------------------+--------+----------------+-----------------------+
| ``forwar          | **f    | ``1.0``        | Weight for            |
| d_reward_weight`` | loat** |                | *forward_reward* term |
|                   |        |                | (see section on       |
|                   |        |                | reward)               |
+-------------------+--------+----------------+-----------------------+
| ``c               | **f    | ``0.1``        | Weight for            |
| trl_cost_weight`` | loat** |                | *ctrl_cost* weight    |
|                   |        |                | (see section on       |
|                   |        |                | reward)               |
+-------------------+--------+----------------+-----------------------+
| ``re              | **f    | ``0.1``        | Scale of random       |
| set_noise_scale`` | loat** |                | perturbations of      |
|                   |        |                | initial position and  |
|                   |        |                | velocity (see section |
|                   |        |                | on Starting State)    |
+-------------------+--------+----------------+-----------------------+
| ``exclude_cu      | **     | ``True``       | Whether or not to     |
| rrent_positions_f | bool** |                | omit the x-coordinate |
| rom_observation`` |        |                | from observations.    |
|                   |        |                | Excluding the         |
|                   |        |                | position can serve as |
|                   |        |                | an inductive bias to  |
|                   |        |                | induce                |
|                   |        |                | position-agnostic     |
|                   |        |                | behavior in policies  |
+-------------------+--------+----------------+-----------------------+

Version History
~~~~~~~~~~~~~~~

-  v3: support for gym.make kwargs such as xml_file, ctrl_cost_weight,
   reset_noise_scale etc. rgb rendering comes from tracking camera (so
   agent does not run away from screen)
-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks. Added
   reward_threshold to environments.
-  v0: Initial versions release (1.0.0)
