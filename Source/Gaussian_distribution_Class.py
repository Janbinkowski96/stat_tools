import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro
import matplotlib.mlab as mlab
from sklearn.preprocessing import minmax_scale

class Gaussian_distribution():
    
    def Saphiro_Test(array_of_values, data_set):
        """"Count mean and standard deviation based on above-mentioned values"""
        
        mean = np.mean(array_of_values) # mean
        stan_dev = np.std(array_of_values) # standard deviation 
        variation = stan_dev ** 2 # variation
        max_value = np.max(array_of_values)
        min_value = np.amin(array_of_values)
        print("""Values for data set number {} => Mean: {}, standard deviation: {}, variation {},
        max value {} and min value {}""".format(data_set, mean, stan_dev, variation, max_value, min_value))

        """Shapiro test, return p and W"""

        W, p = shapiro(array_of_values)
        print("Test walue: {}, p-value: {}". format(round(W, 4), round(p, 4)))
        return(mean, stan_dev)
    
    def Result_plot(list_of_unique_values, list_of_mean, list_of_std, list_of_dataset, list_of_arrays_of_value, data_set_number):
        """Generate plot"""

        if data_set_number == 1:

            values = list_of_arrays_of_value[0]
            mean = list_of_mean[0]
            std = list_of_std[0]
            data_Set = list_of_dataset[0]
            unique_values = list_of_unique_values[0]

            fig = plt.figure()
            axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            n, bins, patches = axes.hist(values, density=True, bins = unique_values, label="Empirical values")
            spread = np.linspace((mean - 3 * std), (mean + 3 * std))
            
            axes.plot(spread, mlab.normpdf(spread, mean, std), label="Gaussian curve")
            axes.set_ylabel("Probability")
            axes.set_xlabel("Value")
            axes.set_title("Data set 1")
            axes.legend()
            
            plt.show()
        
        else:

            fig, ax = plt.subplots(nrows = data_set_number, ncols=1)
            
            for counter, axis in enumerate(ax):
                array_values = list_of_arrays_of_value[counter]
                mean = list_of_mean[counter]
                std = list_of_std[counter]
                data_Set = list_of_dataset[counter]
                unique_values = list_of_unique_values[counter]

                n, bins, patches = axis.hist(array_values, density=True, bins = unique_values, label="Empirical values")
                spread = np.linspace((mean - 3 * std), (mean + 3 * std))
                
                axis.plot(spread, mlab.normpdf(spread, mean, std), label="Gaussian curve")
                axis.set_ylabel("Probability")
                axis.set_xlabel("Value")
                axis.set_title("Data set {}".format(data_Set))
                axis.legend()

            plt.tight_layout()
            plt.show()
    
    def Result_stand_plot(list_of_mean, list_of_std, list_of_dataset, list_of_arrays_of_value, data_set_number):

        if data_set_number == 1:
            
            values = list_of_arrays_of_value[0]
            mean = list_of_mean[0]
            std = list_of_std[0]
            data_range = len(values)

            data_normal = np.sort(np.random.normal(loc=mean, scale=std, size=data_range))
            data_normal_scaled = minmax_scale(data_normal)

            empirical_scaled_data = minmax_scale(values)
            spread = np.linspace(0, 1, data_range)

            fig = plt.figure()
            axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

            axes.plot(spread, data_normal_scaled, label="Scaled gaussian distribution")
            axes.plot(spread, empirical_scaled_data, label="Scaled empirical data")

            axes.set_ylabel("Scaled values")
            axes.set_xlabel("Scaled arguments")
            axes.set_title("Data set 1")
            
            axes.legend()
            plt.show()
        
        else:

            fig, ax = plt.subplots(nrows = data_set_number, ncols=1)
            
            for counter, axis in enumerate(ax):
                array_values = list_of_arrays_of_value[counter]
                mean = list_of_mean[counter]
                std = list_of_std[counter]
                data_Set = list_of_dataset[counter]

                data_range = len(array_values)

                spread = np.linspace(0, 1, data_range)

                data_normal_scaled = np.sort(np.random.normal(loc=mean, scale=std, size=data_range))
                data_normal_scaled = minmax_scale(data_normal_scaled)
                empirical_scaled_data = minmax_scale(array_values)
                
                axis.plot(spread, data_normal_scaled, label="Scaled gaussian distribution")
                axis.plot(spread, empirical_scaled_data, label="Scaled empirical data")

                axis.set_ylabel("Scaled values")
                axis.set_xlabel("Scaled arguments")
                axis.set_title("Data set {}".format(data_Set))
                axis.legend()
            
            fig.canvas.draw()
            plt.tight_layout()
            plt.show()
            


                





