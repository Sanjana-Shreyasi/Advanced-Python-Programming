#Unit : 4 ; Scenario : 2 ; Q6

import numpy as np
import pandas as pd

# create an array of runs scored by players

runs = np.array([4500, 6200, 3800, 7500, 5200, 4100, 6800, 3000, 5600, 4900])

# calculate player statistics

print("Average runs:", np.mean(runs))

print("Highest runs:", np.max(runs))

print("Lowest runs:", np.min(runs))


# create a dataframe

data = {
    "Player": ["Player A", "Player B", "Player C", "Player D", "Player E",
               "Player F", "Player G", "Player H", "Player I", "Player J"],
    "Runs": runs
}

df = pd.DataFrame(data)

print("\nCricket player details:")
print(df)


# display players scoring more than 5000 runs

high_runs = df[df["Runs"] > 5000]

print("\nPlayers scoring more than 5000 runs:")
print(high_runs)

#Output
'''Average runs: 5160.0
Highest runs: 7500
Lowest runs: 3000

Cricket player details:
     Player  Runs
0  Player A  4500
1  Player B  6200
2  Player C  3800
3  Player D  7500
4  Player E  5200
5  Player F  4100
6  Player G  6800
7  Player H  3000
8  Player I  5600
9  Player J  4900

Players scoring more than 5000 runs:
     Player  Runs
1  Player B  6200
3  Player D  7500
4  Player E  5200
6  Player G  6800
8  Player I  5600'''