---
title: Utils
---

# Utils

## Visualization

```{eval-rst}
.. autoclass:: gym.utils.play.PlayableGame
    
    .. automethod:: __init__
    .. automethod:: process_event

.. autoclass:: gym.utils.play.PlayPlot
    
    .. automethod:: __init__
    .. automethod:: callback

.. autofunction:: gym.utils.play.display_arr
.. autofunction:: gym.utils.play.play

```

## Save Rendering Videos

```{eval-rst}
.. autofunction:: gym.utils.save_video.capped_cubic_video_schedule
.. autofunction:: gym.utils.save_video.save_video
```

## Old to New Step API Compatibility

```{eval-rst}
.. autofunction:: gym.utils.step_api_compatibility.convert_to_terminated_truncated_step_api
.. autofunction:: gym.utils.step_api_compatibility.convert_to_done_step_api
.. autofunction:: gym.utils.step_api_compatibility.step_api_compatibility
```

## Seeding

```{eval-rst}
.. autofunction:: gym.utils.seeding.np_random
```

## Environment Checking

### Invasive

```{eval-rst}
.. autofunction:: gym.utils.env_checker.data_equivalence
.. autofunction:: gym.utils.env_checker.check_reset_seed
.. autofunction:: gym.utils.env_checker.check_reset_options
.. autofunction:: gym.utils.env_checker.check_reset_return_info_deprecation
.. autofunction:: gym.utils.env_checker.check_seed_deprecation
.. autofunction:: gym.utils.env_checker.check_reset_return_type
.. autofunction:: gym.utils.env_checker.check_space_limit
.. autofunction:: gym.utils.env_checker.check_env
``` 

### Passive

```{eval-rst}
.. autofunction:: gym.utils.passive_env_checker.check_space
.. autofunction:: gym.utils.passive_env_checker.check_obs
.. autofunction:: gym.utils.passive_env_checker.env_reset_passive_checker
.. autofunction:: gym.utils.passive_env_checker.env_step_passive_checker
.. autofunction:: gym.utils.passive_env_checker.env_render_passive_checker
``` 
