import gymnasium as gym
import gymnasium_robotics
from stable_baselines3 import SAC
from stable_baselines3.her import HerReplayBuffer

def main():
    env = gym.make("FetchReach-v4")

    model = SAC(
        "MultiInputPolicy",
        env,
        replay_buffer_class=HerReplayBuffer,
        replay_buffer_kwargs=dict(
            n_sampled_goal=4,
            goal_selection_strategy="future",
        ),
        verbose=1,
    )

    model.learn(total_timesteps=100_000)
    model.save("sac_fetch_reach")

    env.close()

if __name__ == "__main__":
    main()
