Ant
===

Description
~~~~~~~~~~~

This environment is based on the environment introduced by Schulman,
Moritz, Levine, Jordan and Abbeel in `“High-Dimensional Continuous
Control Using Generalized Advantage
Estimation” <https://arxiv.org/abs/1506.02438>`__. The ant is a 3D robot
consisting of one torso (free rotational body) with four legs attached
to it with each leg having two links. The goal is to coordinate the four
legs to move in the forward (right) direction by applying torques on the
eight hinges connecting the two links of each leg and the torso (nine
parts and eight hinges).

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (8,), float32)``. An action
represents the torques applied at the hinge joints.

+---+-------------+--------+---------+------------------------+---+---+
| N | Action      | C      | Control | Name (in corresponding | J | U |
| u |             | ontrol | Max     | XML file)              | o | n |
| m |             | Min    |         |                        | i | i |
|   |             |        |         |                        | n | t |
|   |             |        |         |                        | t |   |
+===+=============+========+=========+========================+===+===+
| 0 | Torque      | -1     | 1       | hip_1 (front_left_leg) | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | front left  |        |         |                        |   | e |
|   | hip         |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 1 | Torque      | -1     | 1       | angle_1                | h | t |
|   | applied on  |        |         | (front_left_leg)       | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | front left  |        |         |                        | e | u |
|   | two links   |        |         |                        |   | e |
|   |             |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 2 | Torque      | -1     | 1       | hip_2                  | h | t |
|   | applied on  |        |         | (front_right_leg)      | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | front right |        |         |                        |   | e |
|   | hip         |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 3 | Torque      | -1     | 1       | angle_2                | h | t |
|   | applied on  |        |         | (front_right_leg)      | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | front right |        |         |                        | e | u |
|   | two links   |        |         |                        |   | e |
|   |             |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 4 | Torque      | -1     | 1       | hip_3 (back_leg)       | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | back left   |        |         |                        |   | e |
|   | hip         |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 5 | Torque      | -1     | 1       | angle_3 (back_leg)     | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | back left   |        |         |                        | e | u |
|   | two links   |        |         |                        |   | e |
|   |             |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 6 | Torque      | -1     | 1       | hip_4 (right_back_leg) | h | t |
|   | applied on  |        |         |                        | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | torso and   |        |         |                        | e | u |
|   | back right  |        |         |                        |   | e |
|   | hip         |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+
| 7 | Torque      | -1     | 1       | angle_4                | h | t |
|   | applied on  |        |         | (right_back_leg)       | i | o |
|   | the rotor   |        |         |                        | n | r |
|   | between the |        |         |                        | g | q |
|   | back right  |        |         |                        | e | u |
|   | two links   |        |         |                        |   | e |
|   |             |        |         |                        |   | ( |
|   |             |        |         |                        |   | N |
|   |             |        |         |                        |   | m |
|   |             |        |         |                        |   | ) |
+---+-------------+--------+---------+------------------------+---+---+

Observation Space
~~~~~~~~~~~~~~~~~

Observations consist of positional values of different body parts of the
ant, followed by the velocities of those individual parts (their
derivatives) with all the positions ordered before all the velocities.

By default, observations do not include the x- and y-coordinates of the
ant’s torso. These may be included by passing
``exclude_current_positions_from_observation=False`` during
construction. In that case, the observation space will have 113
dimensions where the first two dimensions represent the x- and y-
coordinates of the ant’s torso. Regardless of whether
``exclude_current_positions_from_observation`` was set to true or false,
the x- and y-coordinates of the torso will be returned in ``info`` with
keys ``"x_position"`` and ``"y_position"``, respectively.

However, by default, an observation is a ``ndarray`` with shape
``(111,)`` where the elements correspond to the following:

+---+---------------------------+------+-------+-----------------+---+---+
| N | Observation               | Min  | Max   | Name (in        | J | U |
| u |                           |      |       | corresponding   | o | n |
| m |                           |      |       | XML file)       | i | i |
|   |                           |      |       |                 | n | t |
|   |                           |      |       |                 | t |   |
+===+===========================+======+=======+=================+===+===+
| 0 | z-coordinate of the torso | -Inf | Inf   | torso           | f | p |
|   | (centre)                  |      |       |                 | r | o |
|   |                           |      |       |                 | e | s |
|   |                           |      |       |                 | e | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | o |
|   |                           |      |       |                 |   | n |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | m |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | x-orientation of the      | -Inf | Inf   | torso           | f | a |
|   | torso (centre)            |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | y-orientation of the      | -Inf | Inf   | torso           | f | a |
|   | torso (centre)            |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 3 | z-orientation of the      | -Inf | Inf   | torso           | f | a |
|   | torso (centre)            |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 4 | w-orientation of the      | -Inf | Inf   | torso           | f | a |
|   | torso (centre)            |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 5 | angle between torso and   | -Inf | Inf   | hip_1           | h | a |
|   | first link on front left  |      |       | (               | i | n |
|   |                           |      |       | front_left_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 6 | angle between the two     | -Inf | Inf   | ankle_1         | h | a |
|   | links on the front left   |      |       | (               | i | n |
|   |                           |      |       | front_left_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 7 | angle between torso and   | -Inf | Inf   | hip_2           | h | a |
|   | first link on front right |      |       | (f              | i | n |
|   |                           |      |       | ront_right_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 8 | angle between the two     | -Inf | Inf   | ankle_2         | h | a |
|   | links on the front right  |      |       | (f              | i | n |
|   |                           |      |       | ront_right_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 9 | angle between torso and   | -Inf | Inf   | hip_3           | h | a |
|   | first link on back left   |      |       | (back_leg)      | i | n |
|   |                           |      |       |                 | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | angle between the two     | -Inf | Inf   | ankle_3         | h | a |
| 0 | links on the back left    |      |       | (back_leg)      | i | n |
|   |                           |      |       |                 | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | angle between torso and   | -Inf | Inf   | hip_4           | h | a |
| 1 | first link on back right  |      |       | (               | i | n |
|   |                           |      |       | right_back_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | angle between the two     | -Inf | Inf   | ankle_4         | h | a |
| 2 | links on the back right   |      |       | (               | i | n |
|   |                           |      |       | right_back_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | x-coordinate velocity of  | -Inf | Inf   | torso           | f | v |
| 3 | the torso                 |      |       |                 | r | e |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 | e | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | m |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | y-coordinate velocity of  | -Inf | Inf   | torso           | f | v |
| 4 | the torso                 |      |       |                 | r | e |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 | e | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | m |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | z-coordinate velocity of  | -Inf | Inf   | torso           | f | v |
| 5 | the torso                 |      |       |                 | r | e |
|   |                           |      |       |                 | e | l |
|   |                           |      |       |                 | e | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | m |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | x-coordinate angular      | -Inf | Inf   | torso           | f | a |
| 6 | velocity of the torso     |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | u |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | v |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | y-coordinate angular      | -Inf | Inf   | torso           | f | a |
| 7 | velocity of the torso     |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | u |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | v |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | z-coordinate angular      | -Inf | Inf   | torso           | f | a |
| 8 | velocity of the torso     |      |       |                 | r | n |
|   |                           |      |       |                 | e | g |
|   |                           |      |       |                 | e | u |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | v |
|   |                           |      |       |                 |   | e |
|   |                           |      |       |                 |   | l |
|   |                           |      |       |                 |   | o |
|   |                           |      |       |                 |   | c |
|   |                           |      |       |                 |   | i |
|   |                           |      |       |                 |   | t |
|   |                           |      |       |                 |   | y |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | / |
|   |                           |      |       |                 |   | s |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 1 | angular velocity of angle | -Inf | Inf   | hip_1           | h | a |
| 9 | between torso and front   |      |       | (               | i | n |
|   | left link                 |      |       | front_left_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of the   | -Inf | Inf   | ankle_1         | h | a |
| 0 | angle between front left  |      |       | (               | i | n |
|   | links                     |      |       | front_left_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of angle | -Inf | Inf   | hip_2           | h | a |
| 1 | between torso and front   |      |       | (f              | i | n |
|   | right link                |      |       | ront_right_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of the   | -Inf | Inf   | ankle_2         | h | a |
| 2 | angle between front right |      |       | (f              | i | n |
|   | links                     |      |       | ront_right_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of angle | -Inf | Inf   | hip_3           | h | a |
| 3 | between torso and back    |      |       | (back_leg)      | i | n |
|   | left link                 |      |       |                 | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of the   | -Inf | Inf   | ankle_3         | h | a |
| 4 | angle between back left   |      |       | (back_leg)      | i | n |
|   | links                     |      |       |                 | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of angle | -Inf | Inf   | hip_4           | h | a |
| 5 | between torso and back    |      |       | (               | i | n |
|   | right link                |      |       | right_back_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+
| 2 | angular velocity of the   | -Inf | Inf   | ankle_4         | h | a |
| 6 | angle between back right  |      |       | (               | i | n |
|   | links                     |      |       | right_back_leg) | n | g |
|   |                           |      |       |                 | g | l |
|   |                           |      |       |                 | e | e |
|   |                           |      |       |                 |   | ( |
|   |                           |      |       |                 |   | r |
|   |                           |      |       |                 |   | a |
|   |                           |      |       |                 |   | d |
|   |                           |      |       |                 |   | ) |
+---+---------------------------+------+-------+-----------------+---+---+

The remaining 14*6 = 84 elements of the observation are contact forces
(external forces - force x, y, z and torque x, y, z) applied to the
center of mass of each of the links. The 14 links are: the ground link,
the torso link, and 3 links for each leg (1 + 1 + 12) with the 6
external forces.

The (x,y,z) coordinates are translational DOFs while the orientations
are rotational DOFs expressed as quaternions. One can read more about
free joints on the `Mujoco
Documentation <https://mujoco.readthedocs.io/en/latest/XMLreference.html>`__.

**Note:** There have been reported issues that using a Mujoco-Py version
> 2.0 results in the contact forces always being 0. As such we recommend
to use a Mujoco-Py version < 2.0 when using the Ant environment if you
would like to report results with contact forces (if contact forces are
not used in your experiments, you can use version > 2.0).

Rewards
~~~~~~~

The reward consists of three parts: - *healthy_reward*: Every timestep
that the ant is healthy (see definition in section “Episode
Termination”), it gets a reward of fixed value ``healthy_reward`` -
*forward_reward*: A reward of moving forward which is measured as
*(x-coordinate before action - x-coordinate after action)/dt*. *dt* is
the time between actions and is dependent on the ``frame_skip``
parameter (default is 5), where the frametime is 0.01 - making the
default *dt = 5* 0.01 = 0.05\ *. This reward would be positive if the
ant moves forward (in positive x direction). -*\ ctrl_cost\ *: A
negative reward for penalising the ant if it takes actions that are too
large. It is measured as*\ ``ctrl_cost_weight`` \*
sum(action2)\ *where*\ ``ctr_cost_weight``\ \* is a parameter set for
the control and has a default value of 0.5. - *contact_cost*: A negative
reward for penalising the ant if the external contact force is too
large. It is calculated *``contact_cost_weight``* sum(clip(external
contact force to ``contact_force_range``)2)*.

The total reward returned is **reward** *=* *healthy_reward +
forward_reward - ctrl_cost - contact_cost* and ``info`` will also
contain the individual reward terms.

Starting State
~~~~~~~~~~~~~~

All observations start in state (0.0, 0.0, 0.75, 1.0, 0.0 … 0.0) with a
uniform noise in the range of [-``reset_noise_scale``,
``reset_noise_scale``] added to the positional values and standard
normal noise with mean 0 and standard deviation ``reset_noise_scale``
added to the velocity values for stochasticity. Note that the initial z
coordinate is intentionally selected to be slightly high, thereby
indicating a standing up ant. The initial orientation is designed to
make it face forward as well.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The ant is said to be unhealthy if any of the following happens:

1. Any of the state space values is no longer finite
2. The z-coordinate of the torso is **not** in the closed interval given
   by ``healthy_z_range`` (defaults to [0.2, 1.0])

If ``terminate_when_unhealthy=True`` is passed during construction
(which is the default), the episode terminates when any of the following
happens:

1. The episode duration reaches a 1000 timesteps
2. The ant is unhealthy

If ``terminate_when_unhealthy=False`` is passed, the episode is
terminated only when 1000 timesteps are exceeded.

Arguments
~~~~~~~~~

No additional arguments are currently supported in v2 and lower.

::

   env = gym.make('Ant-v2')

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

::

   env = gym.make('Ant-v3', ctrl_cost_weight=0.1, ...)

+--------------------+---------+-----------+--------------------------+
| Parameter          | Type    | Default   | Description              |
+====================+=========+===========+==========================+
| ``xml_file``       | **str** | ``"a      | Path to a MuJoCo model   |
|                    |         | nt.xml"`` |                          |
+--------------------+---------+-----------+--------------------------+
| ``                 | **      | ``0.5``   | Weight for *ctrl_cost*   |
| ctrl_cost_weight`` | float** |           | term (see section on     |
|                    |         |           | reward)                  |
+--------------------+---------+-----------+--------------------------+
| ``con              | **      | ``5e-4``  | Weight for               |
| tact_cost_weight`` | float** |           | *contact_cost* term (see |
|                    |         |           | section on reward)       |
+--------------------+---------+-----------+--------------------------+
| ``healthy_reward`` | **      | ``1``     | Constant reward given if |
|                    | float** |           | the ant is “healthy”     |
|                    |         |           | after timestep           |
+--------------------+---------+-----------+--------------------------+
| ``terminat         | *       | ``True``  | If true, issue a done    |
| e_when_unhealthy`` | *bool** |           | signal if the            |
|                    |         |           | z-coordinate of the      |
|                    |         |           | torso is no longer in    |
|                    |         |           | the ``healthy_z_range``  |
+--------------------+---------+-----------+--------------------------+
| `                  | **      | ``(       | The ant is considered    |
| `healthy_z_range`` | tuple** | 0.2, 1)`` | healthy if the           |
|                    |         |           | z-coordinate of the      |
|                    |         |           | torso is in this range   |
+--------------------+---------+-----------+--------------------------+
| ``con              | **      | ``        | Contact forces are       |
| tact_force_range`` | tuple** | (-1, 1)`` | clipped to this range in |
|                    |         |           | the computation of       |
|                    |         |           | *contact_cost*           |
+--------------------+---------+-----------+--------------------------+
| ``r                | **      | ``0.1``   | Scale of random          |
| eset_noise_scale`` | float** |           | perturbations of initial |
|                    |         |           | position and velocity    |
|                    |         |           | (see section on Starting |
|                    |         |           | State)                   |
+--------------------+---------+-----------+--------------------------+
| ``exclude_         | *       | ``True``  | Whether or not to omit   |
| current_positions_ | *bool** |           | the x- and y-coordinates |
| from_observation`` |         |           | from observations.       |
|                    |         |           | Excluding the position   |
|                    |         |           | can serve as an          |
|                    |         |           | inductive bias to induce |
|                    |         |           | position-agnostic        |
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
