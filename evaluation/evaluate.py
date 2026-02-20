import gymnasium as gym
import gymnasium_robotics
from stable_baselines3 import SAC

def main():
    env = gym.make("FetchReach-v4", render_mode="human")
    model = SAC.load("sac_fetch_reach", env=env)

    obs, info = env.reset()

    for _ in range(300):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            obs, info = env.reset()

    env.close()

if __name__ == "__main__":
    main()
