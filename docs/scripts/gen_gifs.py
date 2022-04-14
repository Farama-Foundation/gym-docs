__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import gym
import os
from os import mkdir, path

from PIL import Image
import re

from utils import kill_strs
from tqdm import tqdm

# snake to camel case: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
pattern = re.compile(r'(?<!^)(?=[A-Z])')
# how many steps to record an env for
LENGTH = 100
# iterate through all envspecs
for env_spec in tqdm(gym.envs.registry.all()):
    if "Taxi" not in env_spec.id:
        continue

    if any(x in str(env_spec.id) for x in kill_strs):
        continue
    print(env_spec.id)
    # try catch in case missing some installs
    try:
        env = gym.make(env_spec.id)

        # the gym needs to be rgb renderable
        if not ("rgb_array" in env.metadata["render_modes"]):
            continue
        
        # extract env name/type from class path
        split = str(type(env.unwrapped)).split(".")

        # get rid of version info
        env_name = env_spec.id.split("-")[0]
        # convert NameLikeThis to name_like_this
        env_name = pattern.sub('_', env_name).lower()
        # get the env type (e.g. Box2D)
        env_type = split[2]

        # if its an atari gym
        # if env_spec.id[0:3] == "ALE":
        #     continue
        #     env_name = env_spec.id.split("-")[0][4:] 
        #     env_name = pattern.sub('_', env_name).lower()

        # path for saving video
        # v_path = os.path.join("..", "pages", "environments", env_type, "videos")
        # # create dir if it doesnt exist
        # if not path.isdir(v_path):
        #     mkdir(v_path)
            
        # obtain and save LENGTH frames worth of steps
        frames = []
        while True:
            state = env.reset()
            terminated = False
            truncated = False 
            while not (terminated or truncated) and len(frames) <= LENGTH:
                
                frame = env.render(mode='rgb_array')
                repeat = int(60/env.metadata["render_fps"]) if env_type == "toy_text" else 1
                for i in range(repeat):
                    frames.append(Image.fromarray(frame))
                action = env.action_space.sample()
                state_next, reward, terminated, truncated, info = env.step(action)
            
            if len(frames) > LENGTH:
                break

        env.close()

        # make sure video doesnt already exist
        # if not os.path.exists(os.path.join(v_path, env_name + ".gif")):
        frames[0].save(os.path.join("..", "source", "videos",  env_name + ".gif"), save_all=True, append_images=frames[1:], duration=50, loop=0)
        print("Saved: " + env_name)

    except BaseException as e:
        print("ERROR", e)
        continue

