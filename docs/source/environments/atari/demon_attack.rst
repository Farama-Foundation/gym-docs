Demon Attack
============

Description
~~~~~~~~~~~

You are facing waves of demons in the ice planet of Krybor. Points are
accumulated by destroying demons. You begin with 3 reserve bunkers, and
can increase its number (up to 6) by avoiding enemy attacks. Each attack
wave you survive without any hits, grants you a new bunker. Every time
an enemy hits you, a bunker is destroyed. When the last bunker falls,
the next enemy hit will destroy you and the game ends.

Detailed documentation can be found on `the AtariAge
page <https://atariage.com/manual_html_page.php?SoftwareLabelID=135>`__.

Actions
~~~~~~~

By default, all actions that can be performed on an Atari 2600 are
available in this environment. However, if you use v0 or v4 or specify
``full_action_space=False`` during initialization, only a reduced number
of actions (those that are meaningful in this game) are available. The
reduced action space may depend on the flavor of the environment (the
combination of ``mode`` and ``difficulty``). The reduced action space
for the default flavor looks like this:

=== =========
Num Action
=== =========
0   NOOP
1   UP
2   RIGHT
3   LEFT
4   DOWN
5   UPRIGHT
6   UPLEFT
7   DOWNRIGHT
8   DOWNLEFT
=== =========

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

Rewards
~~~~~~~

Each enemy you slay gives you points. The amount of points depends on
the type of demon and which wave you are in. A detailed table of scores
is provided on `the AtariAge
page <https://atariage.com/manual_html_page.php?SoftwareLabelID=135>`__.

Arguments
~~~~~~~~~

::

   env = gym.make("ALE/DemonAttack-v5")

The various ways to configure the environment are described in detail in
the article on Atari environments. It is possible to specify various
flavors of the environment via the keyword arguments ``difficulty`` and
``mode``. A flavor is a combination of a game mode and a difficulty
setting.

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
| D  | ``[1, 3, 5, 7]``                                     | `   | ` |
| em |                                                      | `[0 | ` |
| on |                                                      | , 1 | 1 |
| At |                                                      | ]`` | ` |
| ta |                                                      |     | ` |
| ck |                                                      |     |   |
+----+------------------------------------------------------+-----+---+

You may use the suffix “-ram” to switch to the RAM observation space. In
v0 and v4, the suffixes “Deterministic” and “Noframeskip” are available.
These are no longer supported in v5. In order to obtain equivalent
behavior, pass keyword arguments to ``gym.make`` as outlined in the
general article on Atari environments. The versions v0 and v4 are not
contained in the “ALE” namespace. I.e. they are instantiated via
``gym.make("DemonAttack-v0")``.

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
