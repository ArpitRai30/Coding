#plotting a line
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
x,y = [2,3,8,3,9,1,5],[6,8,9,3,6,2,8]
plt.plot(x,y,color='red',marker='o',markersize=5,markerfacecolor='blue',linestyle='--',label='line-1')
plt.title("MatPlotLib")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x1 = [9,4,7,2]
y1 = [2,6,4,1]
plt.plot(x1,y1,color='green',marker='o',markersize=5,markerfacecolor='yellow',linestyle=':',label='line-2')

plt.legend(loc=4)
plt.show()
'''



#create two array and represent both array as a graph
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
x = np.arange(5)
y = np.arange(7,12)
plt.plot(x,y)
plt.show()
'''



#plotting a velocity graph by using v = u + at

#from matplotlib import pyplot as plt
#import pandas as pd
#import numpy as np
#u, a = 20, 5
#t = np.arange(2,21)
#v = []
#for i in t:
#    v.append(u + a*i)
#print(t)
#print(v)
#plt.plot(t,v,marker='o',markersize=5,markerfacecolor='red')
#plt.title('velocity-time graph')
#plt.xlabel('time (s)')
#plt.ylabel('velocity (m/s)')
#plt.grid()
#plt.savefig(r"C:\Users\styuent\Desktop\Python CSE248\OOPs\graph.jpg")

#plt.show()




#plot graph of s = ut + 1/2(at**2)
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
u, a = 25, 5
t = np.arange(2,21)
s = []
for i in t:
    s.append(u*i + 1/2*(a*(i**2)))
plt.plot(t,s,marker='o',markersize=5,markerfacecolor='red')
plt.title('distance-time graph')
plt.xlabel('time (s)')
plt.ylabel('distance (m)')

plt.show()
'''



#plot graph of v**2 = u**2 + 2as
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math
u, a = 25, 5
s = np.arange(1,21)
v = []
for i in s:
    v.append(math.sqrt(u**2 + 2*a*i))
plt.plot(s,v,marker='o',markersize=5,markerfacecolor='red')
plt.title('velocity-distance graph')
plt.xlabel('distance (m)')
plt.ylabel('velocity (m/s)')
plt.show()
'''



#plot graph from existing data
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('Book1.csv')
print(data)
#plt.bar(data['Subject1'],data['Subject2'])
data.plot.bar()
data.hist()
plt.grid()
plt.show()
'''



#histogram()  #used for frequency distribution
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
age = [3,5,16,12,15,85,91,17,23,42,62,12,16,17,18]
range0 = [0,100]
inter = 10
plt.xlabel("AGE")
plt.ylabel("No. of person")
plt.title("Age Distribution Plot")
plt.hist(age,inter,range0,color='pink')
plt.show()
'''



#pie chart   #used to show percentage of different entities in a whole
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
marks = [94,83,70,92,100]
ex = [0,0,1.0,0,1.0]
sub = ['Maths', 'DT', 'Physics', 'Python', 'ABC']
plt.pie(marks, labels=sub, explode=ex, wedgeprops={'edgecolor':'Black'},autopct='%1.1f%%', startangle=180)
plt.title("1st Sem Result")
plt.show()
'''




#plotting curve of different trigonometric function
#sin
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
a = np.arange(0, 2*(np.pi), 0.1)   #difference is 0.1
#sin
x = np.sin(a)
plt.plot(a,x)
plt.show()

#cos
y = np.cos(a)
plt.plot(a,y)
plt.show()

#tan
z = np.tan(a)
plt.plot(a,z)
plt.show()
'''



#write a function to find the square of user defined array, also plot the graph between number and square
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
n = input("Enter number list:").split()
n = [int(i) for i in n]
n_arr = np.array(n)
def sq(num):
    return num**2
print("squared array is:",sq(n_arr))
plt.plot(n_arr, sq(n_arr), marker='o', markersize=5, markerfacecolor='pink')
plt.title("square numbers graph")
plt.xlabel("Numbers")
plt.ylabel("Squares")
plt.grid()
plt.show()
'''



#WAP for a company department with the following number of employees:
#HR-50
#IT-120
#Finance-70
#Sales-90
#Marketing-80
#Create a pie chart
#cond:1.Add a legend()
#     2.use startangle for better readability
#     3.highlight the department with the highest count
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
emp = [50,120,70,90,80]
ex = [0.1 if n==max(emp) else 0 for n in emp] 
dep = ['HR', 'IT', 'Finance', 'Sales', 'Marketing']
plt.pie(emp, labels=dep, explode=ex, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%', startangle=180)
plt.title('Employee Data')
plt.legend(loc=3)
plt.show()
'''












