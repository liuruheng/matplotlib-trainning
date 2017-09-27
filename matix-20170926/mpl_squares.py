import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values, squares,linewidth=1)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=15)

plt.tick_params(axis="y",which='both', width=2)

plt.show()