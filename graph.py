import matplotlib.pyplot as plt

x = []
y = []
title_given = input("\nEnter the title you want for the graph: ")
x_axis = input("Enter the label you want for x axis: ")
y_axis = input("Enter the label you want for y axis: ")
number_of_points = int(input("\nEnter the number of points you want to plot: "))
for n in range(number_of_points):
    x_values = int(input("\nEnter the number of x values you want to plot: "))
    x.append(x_values)
    y_values = int(input("Enter the number of y values you want to plot: "))
    y.append(y_values)
    
plt.plot(x,y)
plt.title(title_given)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.show()  
