import pandas as pd
import numpy as np

np.random.seed(201)

random_values = np.random.randn(2000, 2) 
non_random_values = np.random.rand(2000, 2)
mixed_values = np.concatenate((random_values, non_random_values), 
                            axis=1)


df_1 = pd.DataFrame(data=random_values)
df_2 = pd.DataFrame(data=non_random_values)
df_3 = pd.DataFrame(data=mixed_values)

df_1.to_csv("normal_data_set.csv", sep=";", index=False, header=None)
df_2.to_csv("non_normal_data_set.csv", sep=";", index=False, header=None)
df_3.to_csv("mixed_data_set.csv", sep=";", index=False, header=None)
