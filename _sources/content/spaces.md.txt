# Spaces

Spaces define the valid format of observation and action spaces for an environment. 

## General Functions

Each space implements the following functions:

```{eval-rst}
.. autofunction:: gym.spaces.Space.sample

.. autofunction:: gym.spaces.Space.contains

.. autoproperty:: gym.spaces.Space.shape

.. property:: gym.spaces.Space.dtype

    Return the data type of this space.

.. autofunction:: gym.spaces.Space.seed

.. autofunction:: gym.spaces.Space.to_jsonable

.. autofunction:: gym.spaces.Space.from_jsonable
``` 

## Box

```{eval-rst}
.. autoclass:: gym.spaces.Box

    .. automethod:: is_bounded
    .. automethod:: sample
``` 

## Discrete

```{eval-rst}
.. autoclass:: gym.spaces.Discrete
``` 

## MultiBinary

```{eval-rst}
.. autoclass:: gym.spaces.MultiBinary
``` 

## MultiDiscrete

```{eval-rst}
.. autoclass:: gym.spaces.MultiDiscrete
``` 

## Dict

```{eval-rst}
.. autoclass:: gym.spaces.Dict
``` 

## Tuple

```{eval-rst}
.. autoclass:: gym.spaces.Tuple
``` 

## Utility Functions

```{eval-rst}
.. autofunction:: gym.spaces.utils.flatdim

.. autofunction:: gym.spaces.utils.flatten_space

.. autofunction:: gym.spaces.utils.flatten

.. autofunction:: gym.spaces.utils.unflatten
``` 