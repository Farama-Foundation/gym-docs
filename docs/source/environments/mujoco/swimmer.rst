Swimmer
=======

Description
~~~~~~~~~~~

This environment corresponds to the Swimmer environment described in
Rémi Coulom’s PhD thesis `“Reinforcement Learning Using Neural Networks,
with Applications to Motor
Control” <https://tel.archives-ouvertes.fr/tel-00003985/document>`__.
The environment aims to increase the number of independent state and
control variables as compared to the classic control environments. The
swimmers consist of three or more segments (‘**links**’) and one less
articulation joints (‘**rotors**’) - one rotor joint connecting exactly
two links to form a linear chain. The swimmer is suspended in a two
dimensional pool and always starts in the same position (subject to some
deviation drawn from an uniform distribution), and the goal is to move
as fast as possible towards the right by applying torque on the rotors
and using the fluids friction.

Notes
~~~~~

The problem parameters are: Problem parameters: \* *n*: number of body
parts \* *mi*: mass of part *i* (*i* ∈ {1…n}) \* *li*: length of part
*i* (*i* ∈ {1…n}) \* *k*: viscous-friction coefficient

While the default environment has *n* = 3, *li* = 0.1, and *k* = 0.1. It
is possible to pass a custom MuJoCo XML file during construction to
increase the number of links, or to tweak any of the parameters.

Action Space
~~~~~~~~~~~~

The action space is a ``Box(-1, 1, (2,), float32)``. An action
represents the torques applied between *links*

+---+--------------------+------+------+-------------------+---+-------+
| N | Action             | Con  | Con  | Name (in          | J | Unit  |
| u |                    | trol | trol | corresponding XML | o |       |
| m |                    | Min  | Max  | file)             | i |       |
|   |                    |      |      |                   | n |       |
|   |                    |      |      |                   | t |       |
+===+====================+======+======+===================+===+=======+
| 0 | Torque applied on  | -1   | 1    | rot2              | h | t     |
|   | the first rotor    |      |      |                   | i | orque |
|   |                    |      |      |                   | n | (N m) |
|   |                    |      |      |                   | g |       |
|   |                    |      |      |                   | e |       |
+---+--------------------+------+------+-------------------+---+-------+
| 1 | Torque applied on  | -1   | 1    | rot3              | h | t     |
|   | the second rotor   |      |      |                   | i | orque |
|   |                    |      |      |                   | n | (N m) |
|   |                    |      |      |                   | g |       |
|   |                    |      |      |                   | e |       |
+---+--------------------+------+------+-------------------+---+-------+

Observation Space
~~~~~~~~~~~~~~~~~

By default, observations consists of: \* θi: angle of part *i* with
respect to the *x* axis \* θi’: its derivative with respect to time
(angular velocity)

In the default case, observations do not include the x- and
y-coordinates of the front tip. These may be included by passing
``exclude_current_positions_from_observation=False`` during
construction. Then, the observation space will have 10 dimensions where
the first two dimensions represent the x- and y-coordinates of the front
tip. Regardless of whether
``exclude_current_positions_from_observation`` was set to true or false,
the x- and y-coordinates will be returned in ``info`` with keys
``"x_position"`` and ``"y_position"``, respectively.

By default, the observation is a ``ndarray`` with shape ``(8,)`` where
the elements correspond to the following:

+---+-----------+-----------+---------+-----------+---------+---------+
| N | Ob        | Min       | Max     | Name (in  | Joint   | Unit    |
| u | servation |           |         | corr      |         |         |
| m |           |           |         | esponding |         |         |
|   |           |           |         | XML file) |         |         |
+===+===========+===========+=========+===========+=========+=========+
| 0 | angle of  | -Inf      | Inf     | rot       | hinge   | angle   |
|   | the front |           |         |           |         | (rad)   |
|   | tip       |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 1 | angle of  | -Inf      | Inf     | rot2      | hinge   | angle   |
|   | the       |           |         |           |         | (rad)   |
|   | second    |           |         |           |         |         |
|   | rotor     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 2 | angle of  | -Inf      | Inf     | rot3      | hinge   | angle   |
|   | the       |           |         |           |         | (rad)   |
|   | second    |           |         |           |         |         |
|   | rotor     |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 3 | velocity  | -Inf      | Inf     | slider1   | slide   | v       |
|   | of the    |           |         |           |         | elocity |
|   | tip along |           |         |           |         | (m/s)   |
|   | the       |           |         |           |         |         |
|   | x-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 4 | velocity  | -Inf      | Inf     | slider2   | slide   | v       |
|   | of the    |           |         |           |         | elocity |
|   | tip along |           |         |           |         | (m/s)   |
|   | the       |           |         |           |         |         |
|   | y-axis    |           |         |           |         |         |
+---+-----------+-----------+---------+-----------+---------+---------+
| 5 | angular   | -Inf      | Inf     | rot       | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of front  |           |         |           |         | elocity |
|   | tip       |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 6 | angular   | -Inf      | Inf     | rot2      | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of second |           |         |           |         | elocity |
|   | rotor     |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+
| 7 | angular   | -Inf      | Inf     | rot3      | hinge   | angular |
|   | velocity  |           |         |           |         | v       |
|   | of third  |           |         |           |         | elocity |
|   | rotor     |           |         |           |         | (rad/s) |
+---+-----------+-----------+---------+-----------+---------+---------+

Rewards
~~~~~~~

The reward consists of two parts: - *forward_reward*: A reward of moving
forward which is measured as *``forward_reward_weight``* (x-coordinate
before action - x-coordinate after action)/dt\ *.*\ dt\* is the time
between actions and is dependent on the frame_skip parameter (default is
4), where the frametime is 0.01 - making the default *dt = 4* 0.01 =
0.04\ *. This reward would be positive if the swimmer swims right as
desired. -*\ ctrl_cost\ *: A cost for penalising the swimmer if it takes
actions that are too large. It is measured as*\ ``ctrl_cost_weight``
*sum(action2)* where *``ctrl_cost_weight``* is a parameter set for the
control and has a default value of 1e-4

The total reward returned is **reward** *=* *forward_reward - ctrl_cost*
and ``info`` will also contain the individual reward terms

Starting State
~~~~~~~~~~~~~~

All observations start in state (0,0,0,0,0,0,0,0) with a Uniform noise
in the range of [-``reset_noise_scale``, ``reset_noise_scale``] is added
to the initial state for stochasticity.

Episode Termination
~~~~~~~~~~~~~~~~~~~

The episode terminates when the episode length is greater than 1000.

Arguments
~~~~~~~~~

No additional arguments are currently supported in v2 and lower.

::

   gym.make('Swimmer-v2')

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight,
reset_noise_scale etc.

::

   env = gym.make('Swimmer-v3', ctrl_cost_weight=0.1, ....)

+--------------------+---------+-----------+--------------------------+
| Parameter          | Type    | Default   | Description              |
+====================+=========+===========+==========================+
| ``xml_file``       | **str** | ``"swimm  | Path to a MuJoCo model   |
|                    |         | er.xml"`` |                          |
+--------------------+---------+-----------+--------------------------+
| ``forwa            | **      | ``1.0``   | Weight for               |
| rd_reward_weight`` | float** |           | *forward_reward* term    |
|                    |         |           | (see section on reward)  |
+--------------------+---------+-----------+--------------------------+
| ``                 | **      | ``1e-4``  | Weight for *ctrl_cost*   |
| ctrl_cost_weight`` | float** |           | term (see section on     |
|                    |         |           | reward)                  |
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
