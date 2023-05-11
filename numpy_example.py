# Library import

import numpy as np
import matplotlib.pyplot as plt

# Functions

# Random walk function

def random_walk(steps):
    steps_list = np.zeros(steps)
    for x in range(steps-1):
        steps_list[x] = steps_list[x-1] + np.random.choice([-1, 1])
    return steps_list

#  Shows plot from given arguments

def show_walk_plot(array, plot_length):
    x = np.arange(0, plot_length)
    y = array
    plt.title(f"Random walk steps: {plot_length}")
    plt.xlabel("Step number")
    plt.ylabel("Value")
    plt.plot(x , y, color ="green")
    plt.show()

# Returning min and max value from given array

def min_max(array):
    return (f"Maximum value of array: {array.max()}\n Minimum value of array: {array.min()}")

# Calling variables

nr_of_steps = 100
nr_of_sim = 50
max_list = np.zeros(nr_of_sim)
ex_value = 30
ex = 0

# Calling functions

value = random_walk(nr_of_steps)
show_walk_plot(value, nr_of_steps)
print(min_max(value))

# Simulating n steps random walk function and saving max value when exceeding x value

for x in range(nr_of_sim):
    value = random_walk(nr_of_steps)
    if(value.max()>=ex_value):
        max_list[x] = value.max()
        ex = ex + 1

print(f"More than {ex_value}: {ex}")
if (ex != 0):
    show_walk_plot(max_list, nr_of_sim)
