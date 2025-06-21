#http:/github.com/mwaskom/seaborn-data
'''
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
a = sns.load_dataset("flights")
print(a)

#to plot line with the help of lineplot()
sns.lineplot(x='year', y='passengers', hue='month', data=a)
plt.show()

#bar plot
#color palette   #moko #rocket
plt.figure(figsize = (20,10))
sns.set(style = "darkgrid")
sns.barplot(x="month", y="passengers", data=a, palette="rocket")
plt.show()

#scatterplot
sns.scatterplot(x="month", y="passengers", hue="year", data=a)
plt.grid()
plt.show()
'''


'''
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
b = sns.load_dataset("diamonds")
print(b)

sns.distplot(b['price'], bins=10, color='red', hist=False)
plt.show()

sns.jointplot(x='carat', y='price', data=b)
plt.show()
'''


'''
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
x = sns.load_dataset("tips")
print(x)
sns.catplot(x='day', y='total_bill', data=x)
plt.show()

#catplot(): kind = 'point', 'swarm', 'count'
sns.catplot(x='day', data=x, kind='count')
plt.show()
'''



#color palets
#'deep', 'bright', 'dark', 'muted', 'pastel', 'colorblind'
'''
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
a = sns.color_palette('colorblind')
sns.palplot(a)
plt.show()
'''



#plotting bar and scatterplot
'''
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

t = sns.load_dataset('car_crashes')
print(t)
sns.lineplot(x='speeding', y='alcohol', data=t)
plt.show()

h = sns.load_dataset('healthexp')
sns.barplot(x='Year', y='Spending_USD', data = h)
plt.show()
sns.scatterplot(x='Year', y='Spending_USD', hue='Spending_USD', data = h)
plt.show()

plt.pie(h.Spending_USD, labels = h.Country, autopct='%1.1f%%')
plt.show()
'''





















