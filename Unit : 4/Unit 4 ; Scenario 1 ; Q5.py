#Unit 4 ; Scenario 1 ; O5

import numpy as np
import pandas as pd

# create an array of electricity bills

bills = np.array([1200, 2500, 3500, 1800, 4200, 2900, 5000, 1500, 3200, 2700])

# calculate bill details

print("Average bill:", np.mean(bills))

print("Median bill:", np.median(bills))

print("Maximum bill:", np.max(bills))

print("Minimum bill:", np.min(bills))


# create a dataframe

data = {
    "Consumer": ["A", "B", "C", "D", "E",
                 "F", "G", "H", "I", "J"],
    "Bill amount": bills
}

df = pd.DataFrame(data)

print("\nElectricity bill details:")
print(df)


# display consumers with bills above 3000

high_bills = df[df["Bill amount"] > 3000]

print("\nConsumers with bills above 3000:")
print(high_bills)

#Output
'''Average bill: 2850.0
Median bill: 2800.0
Maximum bill: 5000
Minimum bill: 1200

Electricity bill details:
  Consumer  Bill amount
0        A         1200
1        B         2500
2        C         3500
3        D         1800
4        E         4200
5        F         2900
6        G         5000
7        H         1500
8        I         3200
9        J         2700

Consumers with bills above 3000:
  Consumer  Bill amount
2        C         3500
4        E         4200
6        G         5000
8        I         3200'''