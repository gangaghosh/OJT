import matplotlib.pyplot as plt
# dataset
x=[1,2,3,4,5]
y=[2,3,6,7,10]

# create a plot with marker
plt.plot(x,y,marker='o',linestyle='-.',color='g',markersize=6,markerfacecolor='y')

# add the lable as well as title
plt.title('line plot with markers')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()


