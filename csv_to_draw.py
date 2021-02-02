import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/crt_uniform_c_232527_210_data.csv')

print(df.head())
x = df.quorum_size.values
y = df.average_overlap.values

plt.plot(x, y)
plt.xlabel('quorum size')
plt.ylabel('average_intersection')
plt.xlim(120, 210)
plt.show()
