---
layout: "docu"
title: "BipedalWalker-v2"
actions: "Discrete"
agents: "2"
manual-control: "No"
action-shape: "(1,)"
action-values: "[0,17]"
observation-shape: "(210, 160, 3)"
observation-values: "(0,255)"
import: "from gym.envs.box2d.bipedal_walker import BipedalWalker"
---
<!-- TODO: fix the front matter info; its wrong -->

<div class="docu-info" markdown="1">
{% include info_box.md %}
</div>

<div class="docu-content" markdown="1">
<div class="appear_big env-title" markdown="1">
{% include env_icon.md %}
## {{page.title}}

</div>


### Description
Reward is given for moving forward, total 300+ points up to the far end. If the robot falls, it gets -100. Applying motor torque costs a small amount of points, more optimal agent will get better score. State consists of hull angle speed, angular velocity, horizontal speed, vertical speed, position of joints and joints angular speed, legs contact with ground, and 10 lidar rangefinder measurements. There's no coordinates in the state vector.


![BipedalWalker Episode Example](./bipedal_walker.jpg)

### Action Space

### Observation Space

### Rewards

### Starting State

### Episode Termination

### Arguments

### Version History

### References
