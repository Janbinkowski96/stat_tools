import pandas as pd
import numpy as np
from Source.Gaussian_distribution_Class import Gaussian_distribution 

list_of_mean = []
list_of_std = []
list_of_dataset = []
list_of_arrays_of_value = []
list_of_unique_values = []

print("Define the path of the input file in 'csv' format")
path_file = input(" ==> ")

values_csv = pd.read_csv(path_file, delimiter=";")

data_set_number = len(values_csv.columns)
data_range = range(data_set_number)

values_csv.columns = range(data_set_number)

for data_set in data_range:
    
    temp_values_csv = values_csv[data_set]
    temp_values_csv = temp_values_csv.dropna()

    array_of_values = np.array(temp_values_csv)
    array_of_values = np.sort(array_of_values, axis=None)

    unique_values = len(pd.unique(np.around(array_of_values, 1)))
    mean, stan_dev = Gaussian_distribution.Saphiro_Test(array_of_values, data_set)
    
    list_of_mean.append(mean)
    list_of_std.append(stan_dev)
    list_of_dataset.append(data_set)
    list_of_arrays_of_value.append(array_of_values)
    list_of_unique_values.append(unique_values)

Gaussian_distribution.Result_plot(list_of_unique_values, list_of_mean, list_of_std, list_of_dataset, list_of_arrays_of_value, data_set_number)
Gaussian_distribution.Result_stand_plot(list_of_mean, list_of_std, list_of_dataset, list_of_arrays_of_value, data_set_number)

