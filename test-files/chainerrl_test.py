import gym

env = gym.make("CartPole-v1", render_mode="rgb_array")
# env.reset()
for _ in range(100):
    observation = env.reset()
    done = False
    while not done:
        env.render()
        observation, reward, done, info = env.step(env.action_space.sample())
        if done:
            # env.reset()
            env.step()
