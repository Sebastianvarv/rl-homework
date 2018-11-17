import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def read_log(filename):
    timesteps = []
    rewards = []
    best_rewards = []

    with open(filename) as f:
        content = f.readlines()

        for line in content:
            if "Timestep" in line:
                _, ts = line.split(" ")
                timesteps.append(int(ts))
            elif "mean reward (100 episodes)" in line:
                _, _, _, _, reward = line.split(" ")
                rewards.append(float(reward))
            elif "best mean reward" in line:
                _, _, _, best = line.split(" ")
                best_rewards.append(float(best))

    return timesteps, rewards, best_rewards


def create_df(ts, reward, max_reward):
    df = pd.DataFrame({"timestep": ts})
    df["reward"] = reward
    df["max_reward"] = max_reward
    return df



ts1, reward16, best16 = read_log("lunar_lander_16.txt")
ts2, reward32, best32 = read_log("lunar_lander_32.txt")
ts3, reward64, best64 = read_log("lunar_lander_64.txt")
ts4, reward128, best128 = read_log("lunar_lander_128.txt")

df1 = create_df(ts1, reward16, best16)
df2 = create_df(ts2, reward32, best32)
df3 = create_df(ts3, reward64, best64)
df4 = create_df(ts4, reward128, best128)


sns.set(style="darkgrid", font_scale=0.8)
sns.lineplot(x="timestep", y="reward",  data=df1, label="batch_size 16")
sns.lineplot(x="timestep", y="reward",  data=df2, label="batch_size 32")
sns.lineplot(x="timestep", y="reward",  data=df3, label="batch_size 64")
sns.lineplot(x="timestep", y="reward",  data=df4, label="batch_size 128")
plt.legend(loc='best').draggable()
plt.show()