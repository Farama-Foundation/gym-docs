MontezumaRevenge
================

Description
~~~~~~~~~~~

Your goal is to acquire Montezuma’s treasure by making your way through
a maze of chambers within the emperor’s fortress. You must avoid deadly
creatures while collecting valuables and tools which can help you escape
with the treasure. Detailed documentation can be found on `the AtariAge
page <https://atariage.com/manual_html_page.php?SoftwareLabelID=310>`__.

Actions
~~~~~~~

By default, all actions that can be performed on an Atari 2600 are
available in this environment. Even if you use v0 or v4 or specify
``full_action_space=False`` during initialization, all actions will be
available in the default flavor.

Observations
~~~~~~~~~~~~

By default, the environment returns the RGB image that is displayed to
human players as an observation. However, it is possible to observe -
The 128 Bytes of RAM of the console - A grayscale image

instead. The respective observation spaces are -
``Box([0 ... 0], [255 ... 255], (128,), uint8)`` -
``Box([[0 ... 0]  ...  [0  ... 0]], [[255 ... 255]  ...  [255  ... 255]], (250, 160), uint8)``

respectively. The general article on Atari environments outlines
different ways to instantiate corresponding environments via
``gym.make``.

Arguments
~~~~~~~~~

::

   env = gym.make("ALE/MontezumaRevenge-v5")

The various ways to configure the environment are described in detail in
the article on Atari environments.

+----+------------------------------------------------------+-----+---+
| E  | Valid Modes                                          | Va  | D |
| nv |                                                      | lid | e |
| ir |                                                      | Dif | f |
| on |                                                      | fic | a |
| me |                                                      | ult | u |
| nt |                                                      | ies | l |
|    |                                                      |     | t |
|    |                                                      |     | M |
|    |                                                      |     | o |
|    |                                                      |     | d |
|    |                                                      |     | e |
+====+======================================================+=====+===+
| Mo | ``[0]``                                              | `   | ` |
| nt |                                                      | `[0 | ` |
| ez |                                                      | ]`` | 0 |
| um |                                                      |     | ` |
| aR |                                                      |     | ` |
| ev |                                                      |     |   |
| en |                                                      |     |   |
| ge |                                                      |     |   |
+----+------------------------------------------------------+-----+---+

You may use the suffix “-ram” to switch to the RAM observation space. In
v0 and v4, the suffixes “Deterministic” and “Noframeskip” are available.
These are no longer supported in v5. In order to obtain equivalent
behavior, pass keyword arguments to ``gym.make`` as outlined in the
general article on Atari environments. The versions v0 and v4 are not
contained in the “ALE” namespace. I.e. they are instantiated via
``gym.make("MontezumaRevenge-v0")``

Version History
~~~~~~~~~~~~~~~

A thorough discussion of the intricate differences between the versions
and configurations can be found in the general article on Atari
environments.

-  v5: Stickiness was added back and stochastic frameskipping was
   removed. The entire action space is used by default. The environments
   are now in the “ALE” namespace.
-  v4: Stickiness of actions was removed
-  v0: Initial versions release (1.0.0)
