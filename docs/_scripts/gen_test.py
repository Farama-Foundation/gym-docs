# # import gym
# # from array2gif import write_gif
# # env = gym.make('CartPole-v0')
# # frames = []
# # for i in range(2):
# #     state = env.reset()
# #     done = False
# #     while not done:
# #         action = env.action_space.sample()
# #         state_next, reward, done, info = env.step(action)
# #         frames.append(env.render(mode='rgb_array'))

# # env.close()
# # write_gif(frames[0:5], 'rgbbgr.gif')
# import gym
# from gym.wrappers import Monitor
# env = Monitor(gym.make('CartPole-v0'), './video', force=True)

# for i in range(20):
#     state = env.reset()
#     done = False
#     while not done:
#         action = env.action_space.sample()
#         state_next, reward, done, info = env.step(action)
# env.close()

import gym
from gym import wrappers

from gym.envs.registration import EnvSpec
from gym.wrappers.time_limit import TimeLimit
from time import time # just to have timestamps in the files
LENGTH = 100
for env_spec in gym.envs.registry.all():
    env = gym.make(env_spec.id)
    # if env.__class__ == TimeLimit:
    #     env_type = ""
    #     env_name = str(env.env)
    #     print(str(env.env))
    
    # else:
    #     env_type = type(env.env).__name__
    # #     # if env_type == "AtariEnv":
    #     env_name = str(env.env._game)
    # #     # else:
    # #     #     print(type(env))
    # #     #     exit()

    # env = wrappers.RecordVideo(env, './videos/' + env_type + '/' + env_name + '/', video_length=LENGTH)
        
    # while True:
    #     state = env.reset()
    #     done = False
    #     while not done and env.recorded_frames < LENGTH:
    #         action = env.action_space.sample()
    #         state_next, reward, done, info = env.step(action)
    #     else:
    #         break
