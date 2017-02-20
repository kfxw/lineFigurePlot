# A brief demo to make line plot.
# Author: Wei Zhen @ IIE, CAS & Yingcai, UESTC
# Finish on: 2016-03-25
# Last update: 2017-02-20
import numpy as np
import matplotlib.pyplot as plt

# a for variable 'x'
a = np.array(range(6),dtype='float32')/10
# b, c are variable 'y1' and 'y2'
b = np.array([0.8, 0.75, 0.73, 0.55, 0.21, 0.16], dtype='float32')
c = np.array([0.8, 0.65, 0.60, 0.55, 0.35, 0.19], dtype='float32')

# create figure, get figure and frame handle
fig, ax = plt.subplots()

# call each plot(x, y, linestyle, label) to add lines
#    linestyle: '-' for solid line;
#	        'b','g' are color abbr.;
#	        'd' for thin_diamond marker
#    label: a string to identify each line, will be used in legend
#    more options: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
plt.plot(a, b, '-bd', label='CCA')
plt.plot(a, c, '-yc', label='SCM')
## matplotlib support Latex string
# plt.plot(a, c, color='#FF6633', marker='o', label='w $l_{SC}$', linewidth=2)

# create legend automatically
#    numpoints: num of markers (thin_diamonds) of each label in the legend
#    shadow: create a shadow
#    loc: a general loacation of legend,
#	  accept a string = ['{} {}'.format(i,j) for i in ['upper', 'lower', 'center'] for j in ['right', 'center', 'left']]
#    bbox_to_anchor: a specific location, (x, y) means locate at (1.1*width, 1*height), x and y could be negative or larger than 1
#    ncol: he number of columns that the legend has. Default is 1. Integer.
#    more option:http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
plt.legend(numpoints='2',shadow=True, ncol=1, bbox_to_anchor=(1.1, 1))#,loc='upper right')

# create grid. set 'True' to create grid
#    linestyle: the same to plot::linestyle
#    color: grid line's color, could be color abbr. OR grayscale value
#    more options:http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.grid
#    add minor grid and change grid interval:http://stackoverflow.com/questions/24943991/matplotlib-change-grid-interval-and-specify-tick-labels
plt.grid(True, linestyle='-',color='0.7')

# create axis label, accept label names directly
#    fontsize: font size
#    other options are correspond to text() options
#    text() options:http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.text
plt.xlabel('Recall', fontsize=16)
plt.ylabel('Precision', fontsize=16)

# limit axis range, take a list param which stands for [x_min, x_max, y_min, y_max]
#    more general options: http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes
plt.axis([0,1,0.15,1.05])

# set frame visibility
#    ax: frame handle obtained from plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# show the overall plot
plt.show()
# save figure with resolution option
#plt.savefig('normRF_1.png', dpi=800)
