HumanoidStandup
===============

Description
~~~~~~~~~~~

This environment is based on the environment introduced by Tassa, Erez
and Todorov in `“Synthesis and stabilization of complex behaviors
through online trajectory
optimization” <https://ieeexplore.ieee.org/document/6386025>`__. The 3D
bipedal robot is designed to simulate a human. It has a torso (abdomen)
with a pair of legs and arms. The legs each consist of two links, and so
the arms (representing the knees and elbows respectively). The
environment starts with the humanoid layiing on the ground, and then the
goal of the environment is to make the humanoid standup and then keep it
standing by applying torques on the various hinges.

Action Space
~~~~~~~~~~~~

The agent take a 17-element vector for actions.

The action space is a continuous ``(action, ...)`` all in ``[-1, 1]``,
where ``action`` represents the numerical torques applied at the hinge
joints.

+---+-------------+--------+---------+------------------------+---+---+
| N | Action      | C      | Control | Name (in corresponding | J | U |
| u |             | ontrol | Max     | XML file)              | o | n |
| m |             | Min    |         |                        | i | i |
|   |             |        |         |                        | n | t |
|   |             |        |         |                        | t |   |
+===+=============+========+=========+========================+===+===+
| 0 | Torque      | -0.4   | 0.4     | hip_1 (front_left_leg) | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the hinge   |        |         |                        | n | r |
|   | in the      |        |         |                        | g | q |
|   | y           |        |         |                        | e | u |
|   | -coordinate |        |         |                        |   | e |
|   | of the      |        |         |                        |   | ( |
|   | abdomen     |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | angle_1                | h | t |
|   | applied on  |        |         | (front_left_leg)       | i | o |
|   | the hinge   |        |         |                        | n | r |
|   | in the      |        |         |                        | g | q |
|   | z           |        |         |                        | e | u |
|   | -coordinate |        |         |                        |   | e |
|   | of the      |        |         |                        |   | ( |
|   | abdomen     |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 2 | Torque      | -0.4   | 0.4     | hip_2                  | h | t |
|   | applied on  |        |         | (front_right_leg)      | i | o |
|   | the hinge   |        |         |                        | n | r |
|   | in the      |        |         |                        | g | q |
|   | x           |        |         |                        | e | u |
|   | -coordinate |        |         |                        |   | e |
|   | of the      |        |         |                        |   | ( |
|   | abdomen     |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 3 | Torque      | -0.4   | 0.4     | right_hip_x            | h | t |
|   | applied on  |        |         | (right_thigh)          | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | right hip   |        |         |                        |   | N |
|   | (x-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 4 | Torque      | -0.4   | 0.4     | right_hip_z            | h | t |
|   | applied on  |        |         | (right_thigh)          | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | right hip   |        |         |                        |   | N |
|   | (z-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 5 | Torque      | -0.4   | 0.4     | right_hip_y            | h | t |
|   | applied on  |        |         | (right_thigh)          | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | right hip   |        |         |                        |   | N |
|   | (y-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 6 | Torque      | -0.4   | 0.4     | right_knee             | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | right       |        |         |                        | e | u |
|   | hip/thigh   |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | right shin  |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 7 | Torque      | -0.4   | 0.4     | left_hip_x             | h | t |
|   | applied on  |        |         | (left_thigh)           | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | left hip    |        |         |                        |   | N |
|   | (x-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 8 | Torque      | -0.4   | 0.4     | left_hip_z             | h | t |
|   | applied on  |        |         | (left_thigh)           | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | left hip    |        |         |                        |   | N |
|   | (z-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 9 | Torque      | -0.4   | 0.4     | left_hip_y             | h | t |
|   | applied on  |        |         | (left_thigh)           | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between     |        |         |                        | g | q |
|   | to          |        |         |                        | e | u |
|   | rso/abdomen |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | left hip    |        |         |                        |   | N |
|   | (y-         |        |         |                        |   | m |
|   | coordinate) |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | left_knee              | h | t |
| 0 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | left        |        |         |                        | e | u |
|   | hip/thigh   |        |         |                        |   | e |
|   | and the     |        |         |                        |   | ( |
|   | left shin   |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | right_shoulder1        | h | t |
| 1 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | right upper |        |         |                        |   | e |
|   | arm         |        |         |                        |   | ( |
|   | (coordinate |        |         |                        |   | N |
|   | -1)         |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | right_shoulder2        | h | t |
| 2 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | right upper |        |         |                        |   | e |
|   | arm         |        |         |                        |   | ( |
|   | (coordinate |        |         |                        |   | N |
|   | -2)         |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | right_elbow            | h | t |
| 3 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | right upper |        |         |                        | e | u |
|   | arm and     |        |         |                        |   | e |
|   | right lower |        |         |                        |   | ( |
|   | arm         |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | left_shoulder1         | h | t |
| 4 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | left upper  |        |         |                        |   | e |
|   | arm         |        |         |                        |   | ( |
|   | (coordinate |        |         |                        |   | N |
|   | -1)         |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | left_shoulder2         | h | t |
| 5 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | left upper  |        |         |                        |   | e |
|   | arm         |        |         |                        |   | ( |
|   | (coordinate |        |         |                        |   | N |
|   | -2)         |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -0.4   | 0.4     | left_elbow             | h | t |
| 6 | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | left upper  |        |         |                        | e | u |
|   | arm and     |        |         |                        |   | e |
|   | left lower  |        |         |                        |   | ( |
|   | arm         |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+

Observation Space
~~~~~~~~~~~~~~~~~

The state space consists of positional values of different body parts of
the Humanoid, followed by the velocities of those individual parts
(their derivatives) with all the positions ordered before all the
velocities.

**Note:** The x- and y-coordinates of the torso are being omitted to
produce position-agnostic behavior in policies

The observation is a ``ndarray`` with shape ``(376,)`` where the
elements correspond to the following:

+---+--------------------------+------+-------+------------------+---+---+
| N | Observation              | Min  | Max   | Name (in         | J | U |
| u |                          |      |       | corresponding    | o | n |
| m |                          |      |       | XML file)        | i | i |
|   |                          |      |       |                  | n | t |
|   |                          |      |       |                  | t |   |
+===+==========================+======+=======+==================+===+===+
| 0 | z-coordinate of the      | -Inf | Inf   | root             | f | p |
|   | torso (centre)           |      |       |                  | r | o |
|   |                          |      |       |                  | e | s |
|   |                          |      |       |                  | e | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | o |
|   |                          |      |       |                  |   | n |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | x-orientation of the     | -Inf | Inf   | root             | f | a |
|   | torso (centre)           |      |       |                  | r | n |
|   |                          |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | y-orientation of the     | -Inf | Inf   | root             | f | a |
|   | torso (centre)           |      |       |                  | r | n |
|   |                          |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 3 | z-orientation of the     | -Inf | Inf   | root             | f | a |
|   | torso (centre)           |      |       |                  | r | n |
|   |                          |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 4 | w-orientation of the     | -Inf | Inf   | root             | f | a |
|   | torso (centre)           |      |       |                  | r | n |
|   |                          |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 5 | z-angle of the abdomen   | -Inf | Inf   | abdomen_z        | h | a |
|   | (in lower_waist)         |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 6 | y-angle of the abdomen   | -Inf | Inf   | abdomen_y        | h | a |
|   | (in lower_waist)         |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 7 | x-angle of the abdomen   | -Inf | Inf   | abdomen_x        | h | a |
|   | (in pelvis)              |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 8 | x-coordinate of angle    | -Inf | Inf   | right_hip_x      | h | a |
|   | between pelvis and right |      |       |                  | i | n |
|   | hip (in right_thigh)     |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 9 | z-coordinate of angle    | -Inf | Inf   | right_hip_z      | h | a |
|   | between pelvis and right |      |       |                  | i | n |
|   | hip (in right_thigh)     |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | y-coordinate of angle    | -Inf | Inf   | right_hip_y      | h | a |
| 0 | between pelvis and right |      |       |                  | i | n |
|   | hip (in right_thigh)     |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angle between right hip  | -Inf | Inf   | right_knee       | h | a |
| 1 | and the right shin (in   |      |       |                  | i | n |
|   | right_knee)              |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | x-coordinate of angle    | -Inf | Inf   | left_hip_x       | h | a |
| 2 | between pelvis and left  |      |       |                  | i | n |
|   | hip (in left_thigh)      |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | z-coordinate of angle    | -Inf | Inf   | left_hip_z       | h | a |
| 3 | between pelvis and left  |      |       |                  | i | n |
|   | hip (in left_thigh)      |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | y-coordinate of angle    | -Inf | Inf   | left_hip_y       | h | a |
| 4 | between pelvis and left  |      |       |                  | i | n |
|   | hip (in left_thigh)      |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angle between left hip   | -Inf | Inf   | left_knee        | h | a |
| 5 | and the left shin (in    |      |       |                  | i | n |
|   | left_knee)               |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | coordinate-1             | -Inf | Inf   | right_shoulder1  | h | a |
| 6 | (multi-axis) angle       |      |       |                  | i | n |
|   | between torso and right  |      |       |                  | n | g |
|   | arm (in right_upper_arm) |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | coordinate-2             | -Inf | Inf   | right_shoulder2  | h | a |
| 7 | (multi-axis) angle       |      |       |                  | i | n |
|   | between torso and right  |      |       |                  | n | g |
|   | arm (in right_upper_arm) |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | angle between right      | -Inf | Inf   | right_elbow      | h | a |
| 8 | upper arm and            |      |       |                  | i | n |
|   | right_lower_arm          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 1 | coordinate-1             | -Inf | Inf   | left_shoulder1   | h | a |
| 9 | (multi-axis) angle       |      |       |                  | i | n |
|   | between torso and left   |      |       |                  | n | g |
|   | arm (in left_upper_arm)  |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | coordinate-2             | -Inf | Inf   | left_shoulder2   | h | a |
| 0 | (multi-axis) angle       |      |       |                  | i | n |
|   | between torso and left   |      |       |                  | n | g |
|   | arm (in left_upper_arm)  |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | angle between left upper | -Inf | Inf   | left_elbow       | h | a |
| 1 | arm and left_lower_arm   |      |       |                  | i | n |
|   |                          |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | e |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | r |
|   |                          |      |       |                  |   | a |
|   |                          |      |       |                  |   | d |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | x-coordinate velocity of | -Inf | Inf   | root             | f | v |
| 2 | the torso (centre)       |      |       |                  | r | e |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  | e | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | y-coordinate velocity of | -Inf | Inf   | root             | f | v |
| 3 | the torso (centre)       |      |       |                  | r | e |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  | e | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | z-coordinate velocity of | -Inf | Inf   | root             | f | v |
| 4 | the torso (centre)       |      |       |                  | r | e |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  | e | o |
|   |                          |      |       |                  |   | c |
|   |                          |      |       |                  |   | i |
|   |                          |      |       |                  |   | t |
|   |                          |      |       |                  |   | y |
|   |                          |      |       |                  |   | ( |
|   |                          |      |       |                  |   | m |
|   |                          |      |       |                  |   | / |
|   |                          |      |       |                  |   | s |
|   |                          |      |       |                  |   | ) |
+---+--------------------------+------+-------+------------------+---+---+
| 2 | x-coordinate angular     | -Inf | Inf   | root             | f | a |
| 5 | velocity of the torso    |      |       |                  | r | n |
|   | (centre)                 |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | u |
|   |                          |      |       |                  |   | l |
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
| 2 | y-coordinate angular     | -Inf | Inf   | root             | f | a |
| 6 | velocity of the torso    |      |       |                  | r | n |
|   | (centre)                 |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | u |
|   |                          |      |       |                  |   | l |
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
| 2 | z-coordinate angular     | -Inf | Inf   | root             | f | a |
| 7 | velocity of the torso    |      |       |                  | r | n |
|   | (centre)                 |      |       |                  | e | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | u |
|   |                          |      |       |                  |   | l |
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
| 2 | z-coordinate of angular  | -Inf | Inf   | abdomen_z        | h | a |
| 8 | velocity of the abdomen  |      |       |                  | i | n |
|   | (in lower_waist)         |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 2 | y-coordinate of angular  | -Inf | Inf   | abdomen_y        | h | a |
| 9 | velocity of the abdomen  |      |       |                  | i | n |
|   | (in lower_waist)         |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | x-coordinate of angular  | -Inf | Inf   | abdomen_x        | h | a |
| 0 | velocity of the abdomen  |      |       |                  | i | a |
|   | (in pelvis)              |      |       |                  | n | n |
|   |                          |      |       |                  | g | g |
|   |                          |      |       |                  | e | l |
|   |                          |      |       |                  |   | u |
|   |                          |      |       |                  |   | l |
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
| 3 | x-coordinate of the      | -Inf | Inf   | right_hip_x      | h | a |
| 1 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | right hip (in            |      |       |                  | g | l |
|   | right_thigh)             |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | z-coordinate of the      | -Inf | Inf   | right_hip_z      | h | a |
| 2 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | right hip (in            |      |       |                  | g | l |
|   | right_thigh)             |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | y-coordinate of the      | -Inf | Inf   | right_hip_y      | h | a |
| 3 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | right hip (in            |      |       |                  | g | l |
|   | right_thigh)             |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | angular velocity of the  | -Inf | Inf   | right_knee       | h | a |
| 5 | angle between right hip  |      |       |                  | i | n |
|   | and the right shin (in   |      |       |                  | n | g |
|   | right_knee)              |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | x-coordinate of the      | -Inf | Inf   | left_hip_x       | h | a |
| 6 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | left hip (in left_thigh) |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | z-coordinate of the      | -Inf | Inf   | left_hip_z       | h | a |
| 7 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | left hip (in left_thigh) |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | y-coordinate of the      | -Inf | Inf   | left_hip_y       | h | a |
| 8 | angular velocity of the  |      |       |                  | i | n |
|   | angle between pelvis and |      |       |                  | n | g |
|   | left hip (in left_thigh) |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 3 | angular velocity of the  | -Inf | Inf   | left_knee        | h | a |
| 9 | angle between left hip   |      |       |                  | i | n |
|   | and the left shin (in    |      |       |                  | n | g |
|   | left_knee)               |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 4 | coordinate-1             | -Inf | Inf   | right_shoulder1  | h | a |
| 0 | (multi-axis) of the      |      |       |                  | i | n |
|   | angular velocity of the  |      |       |                  | n | g |
|   | angle between torso and  |      |       |                  | g | l |
|   | right arm (in            |      |       |                  | e | u |
|   | right_upper_arm)         |      |       |                  |   | l |
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
| 4 | coordinate-2             | -Inf | Inf   | right_shoulder2  | h | a |
| 1 | (multi-axis) of the      |      |       |                  | i | n |
|   | angular velocity of the  |      |       |                  | n | g |
|   | angle between torso and  |      |       |                  | g | l |
|   | right arm (in            |      |       |                  | e | u |
|   | right_upper_arm)         |      |       |                  |   | l |
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
| 4 | angular velocity of the  | -Inf | Inf   | right_elbow      | h | a |
| 2 | angle between right      |      |       |                  | i | n |
|   | upper arm and            |      |       |                  | n | g |
|   | right_lower_arm          |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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
| 4 | coordinate-1             | -Inf | Inf   | left_shoulder1   | h | a |
| 3 | (multi-axis) of the      |      |       |                  | i | n |
|   | angular velocity of the  |      |       |                  | n | g |
|   | angle between torso and  |      |       |                  | g | l |
|   | left arm (in             |      |       |                  | e | u |
|   | left_upper_arm)          |      |       |                  |   | l |
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
| 4 | coordinate-2             | -Inf | Inf   | left_shoulder2   | h | a |
| 4 | (multi-axis) of the      |      |       |                  | i | n |
|   | angular velocity of the  |      |       |                  | n | g |
|   | angle between torso and  |      |       |                  | g | l |
|   | left arm (in             |      |       |                  | e | u |
|   | left_upper_arm)          |      |       |                  |   | l |
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
| 4 | angular velocitty of the | -Inf | Inf   | left_elbow       | h | a |
| 5 | angle between left upper |      |       |                  | i | n |
|   | arm and left_lower_arm   |      |       |                  | n | g |
|   |                          |      |       |                  | g | l |
|   |                          |      |       |                  | e | u |
|   |                          |      |       |                  |   | l |
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

Additionally, after all the positional and velocity based values in the
table, the state_space consists of (in order): - *cinert:* Mass and
inertia of a single rigid body relative to the center of mass (this is
an intermediate result of transition). It has shape 14\ *10 (*\ nbody \*
10\ *) and hence adds to another 140 elements in the state space.
-*\ cvel:\* Center of mass based velocity. It has shape 14 \* 6 (*nbody*
6\ *) and hence adds another 84 elements in the state space
-*\ qfrc_actuator:\* Constraint force generated as the actuator force.
This has shape ``(23,)`` *(nv* 1)\* and hence adds another 23 elements
to the state space. - *cfrc_ext:* This is the center of mass based
external force on the body. It has shape 14 \* 6 (*nbody* 6\ *) and
hence adds to another 84 elements in the state space. where*\ nbody\*
stands for the number of bodies in the robot and *nv* stands for the
number of degrees of freedom (*= dim(qvel)*)

The (x,y,z) coordinates are translational DOFs while the orientations
are rotational DOFs expressed as quaternions. One can read more about
free joints on the `Mujoco
Documentation <https://mujoco.readthedocs.io/en/latest/XMLreference.html>`__.

**Note:** There have been reported issues that using a Mujoco-Py version
> 2.0 results in the contact forces always being 0. As such we recommend
to use a Mujoco-Py version < 2.0 when using the Humanoid environment if
you would like to report results with contact forces (if contact forces
are not used in your experiments, you can use version > 2.0).

Rewards
~~~~~~~

The reward consists of three parts: - *uph_cost*: A reward for moving
upward (in an attempt to stand up). This is not a relative reward which
meaures how much upward it has moved from the last timestep, but it is
an absolute reward which measures how much upward the Humanoid has moved
overall. It is measured as *(z coordinate after action - 0)/(atomic
timestep)*, where *z coordinate after action* is index 0 in the
state/index 2 in the table, and *atomic timestep* is the time for one
frame of movement even though the simulation has a framerate of 5 (done
in order to inflate rewards a little for fassteer learning). -
*quad_ctrl_cost*: A negative reward for penalising the humanoid if it
has too large of a control force. If there are *nu* actuators/controls,
then the control has shape ``nu x 1``. It is measured as
*0.1*\ **x**\ *sum(control2)*. - *quad_impact_cost*: A negative reward
for penalising the humanoid if the external contact force is too large.
It is calculated as *min(0.5* 0.000001 \* sum(external contact force2),
10)*.

The total reward returned is **reward** *=* *uph_cost + 1 -
quad_ctrl_cost - quad_impact_cost*

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.105, 1.0, 0.0 … 0.0) with a
uniform noise in the range of [-0.01, 0.01] added to the positional and
velocity values (values in the table) for stochasticity. Note that the
initial z coordinate is intentionally selected to be low, thereby
indicating a laying down humanoid. The initial orientation is designed
to make it face forward as well.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when any of the following happens:

1. The episode duration reaches a 1000 timesteps
2. Any of the state space values is no longer finite

Arguments
~~~~~~~~~

No additional arguments are currently supported.

::

   env = gym.make('HumanoidStandup-v2')

There is no v3 for HumanoidStandup, unlike the robot environments where
a v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

Version History
~~~~~~~~~~~~~~~

-  v2: All continuous control environments now use mujoco_py >= 1.50
-  v1: max_time_steps raised to 1000 for robot based tasks. Added
   reward_threshold to environments.
-  v0: Initial versions release (1.0.0)
