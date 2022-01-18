__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import gym
import os
from os import mkdir, path

from PIL import Image

# how many steps to record an env for
LENGTH = 100
# iterate through all envspecs
for env_spec in gym.envs.registry.all():

    env = gym.make(env_spec.id)
    
    if not "rgb_array" in env.metadata["render.modes"]:
        continue
    
    # extract env name/type from class path
    split = str(type(env.env)).split(".")
    env_name = split[3]
    env_type = split[2]

    # path for saving video
    v_path = os.path.join("..", "pages", "environments", env_type, "videos")
    if not path.isdir(v_path):
        mkdir(v_path)
         
    frames = []
    while True:
        state = env.reset()
        done = False
        while not done and len(frames) <= LENGTH:
            frame = env.render(mode='rgb_array')
            frames.append(Image.fromarray(frame))
            action = env.action_space.sample()
            state_next, reward, done, info = env.step(action)
        
        if len(frames) > LENGTH:
            break

    env.close()
    frames[0].save(os.path.join(v_path, env_name + ".gif"), save_all=True, append_images=frames[1:], duration=50, loop=0)


