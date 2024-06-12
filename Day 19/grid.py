import matplotlib.pyplot as plt

# data
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,2,3,4,5]

# create the plot
plt.plot(x,y1,linestyle='-',color='g',linewidth=3,marker='o',markersize=8,markerfacecolor='green')

plt.plot(x,y2,linestyle='--',color='r',linewidth=3,marker='x',markersize=8,markerfacecolor='red')

# title and label
plt.title('customized line plot with grid')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# create a legend method with chart that we have created

plt.legend()

# Add the value as grid
plt.grid(True)

# customize the grid
plt.grid(color='grey',linestyle='--',linewidth=1)

plt.show()