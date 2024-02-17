import gym
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# import pygame

# env = gym.make("CartPole-v1", render_mode="rgb_array")
# # env.reset()
# for _ in range(100):
#     observation = env.reset()
#     done = False
#     while not done:
#         env.render()
#         observation, reward, done, info = env.step(env.action_space.sample())
#         if done:
#             # env.reset()
#             env.step()



# env = gym.make("CartPole-v1", render_mode="rgb_array")
# env.reset()
# for _ in range(100):
#     env.render()
#     env.step(env.action_space.sample())  # take a random action


env = gym.make("CartPole-v1", render_mode="rgb_array")
observation = env.reset()

for _ in range(100):
    env.render()
    action = env.action_space.sample()  # 选择一个随机动作
    # observation, reward, terminated = env.step(action)
    result = env.step(action)
    terminated = result[2]
    # print(result[0], result[1], result[2], result[3])

    if terminated:
        observation = env.reset()  # 如果环境已经结束，重置环境