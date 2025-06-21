'''
import numpy as np
a1 = np.array([[[6,5,2,4,9],[4,8,9,6,8],[7,4,2,1,6],[6,3,2,9,2]],[[6,5,2,8,4],[4,2,3,1,3],[7,8,9,6,3],[4,4,2,3,6]]])
print(a1)
print(np.where(a1%2==0, 0, a1))
np.savetxt(r"mat.txt", a1)
'''


#pandas series
'''
import pandas as pd
a = [10, "Ram", 23.23, 43]
mycol = pd.Series(a)
print(mycol)
#print(mycol[2])
'''


'''
import pandas as pd
b = [13,23,24]
s = pd.Series(b, index=['x','y','z'])
print(s)
print(s['y'])
print(s[1])
'''


'''
import pandas as pd
import numpy as np
data = np.array([12,13,14,15,16])
s = pd.Series(data, index = [1,2,3,4,5])
print(s)
'''



#create a series by using a dictionary
'''
import pandas as pd
dict = {'a':10,'b':20,'c':30}
ds1 = pd.Series(dict, index=['a','b','c','a','b','c','b','c','a',1,'d'])
print(ds1)
'''


'''
import pandas as pd
ds = pd.Series(20, index = [10,11,12,13,14])
print(ds)
'''



#create the series by using the numpy functions
'''
import pandas as pd
import numpy as np
ds = pd.Series(np.ones(10))
print(ds)
ds1 = pd.Series(np.arange(12,24))
print(ds1)
'''



#create a data frame from a list
'''
import pandas as pd
data = {
    "Name":['Ram', 'Ravi', 'Raj'],
    "roll_no":[100,101,102],
    "marks":[94,92,97]
    }
df = pd.DataFrame(data, index=[1,2,3])
print(df)


#loc
print(df.loc[1])
print(df['Name'])
print(df.loc[[1,2]])
'''



#create the dataframe using numpy array
'''
import pandas as pd
import numpy as np
n1 = np.array([['abc','xyz','pqr'],
               [101,102,103],
               [93,99,91]])
print(n1)
df = pd.DataFrame(n1,
                  columns=['st1', 'st2', 'st3'],
                  index=['Name', 'Roll_no', 'Marks'])
print(df)
'''



#create the dataframe by using lists of list
'''
import pandas as pd
x = [["Arpit",101,100], ["Anuj",102,64], ["Aarti",103,31]]
df = pd.DataFrame(x,columns=["Name", "Roll", "Marks"],index=[1,2,3])
print(df)
'''



#create the dataframe using list of dictionary
'''
import pandas as pd
y = [{"Name":"Aditi", "Roll":201, "Marks":12},
     {"Name":"Pooja", "Roll":202, "Marks":22},
     {"Name":"Rekha", "Roll":203, "Marks":34},
     {"Name":"Amitabh", "Roll":204, "Marks":69},]
df1 = pd.DataFrame(y)
print(df1)
'''



#create DF using dictionary of Series
'''
import pandas as pd
s1 = pd.Series(["Aditya", "Aman", "Ansh"])
s2 = pd.Series([101,102,103])
s3 = pd.Series([20,81,30])
dict1 = {"Name":s1, "Roll":s2, "Marks":s3}
df1 = pd.DataFrame(dict1)
print(df1)
'''
'''
print(df1.index)
print(df1.columns)
'''
#insert a new column in existing DF
'''
df1["Address"] = ["Delhi", "Faridabad", "Noida"]
print(df1)

df1["Status"] = df1["Marks"] > 80
print(df1)

df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)
'''
#delete a column
'''
df1["Address"] = ["Delhi", "Faridabad", "Noida"]
df1["Status"] = df1["Marks"] > 80
df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)

del df1["Status"]
print(df1)
'''
#pop operation
'''
df1["Address"] = ["Delhi", "Faridabad", "Noida"]
df1["Status"] = df1["Marks"] > 80
df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)

df = df1.pop("Branch")
print(df1)
print(df)
'''
#dropping a col or row from df using drop()
'''
df1["Address"] = ["Delhi", "Faridabad", "Noida"]
df1["Status"] = df1["Marks"] > 80
df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)

df1.drop("Marks", axis = 1, inplace = True)
print(df1)
'''
#rename a column using rename()
'''
df1["Address"] = ["Delhi", "Faridabad", "Noida"]
df1["Status"] = df1["Marks"] > 80
df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)

df1.rename(columns = {"Name":"Stu_Name"}, inplace = True)
print(df1)
'''




#creating a DF by using numpy random()
'''
import pandas as pd
import numpy as np
dfr = pd.DataFrame(np.random.rand(250,5))
print(dfr)
print(dfr.head())    #it will print first 5 rows
print(dfr.tail())    #it will print first 5 columns
print(dfr.head(15))
print(dfr.tail(15))
'''


#creating csv and xlsx file
'''
import pandas as pd
s1 = pd.Series(["Aditya", "Aman", "Ansh"])
s2 = pd.Series([101,102,103])
s3 = pd.Series([20,81,30])
dict1 = {"Name":s1, "Roll":s2, "Marks":s3}
df1 = pd.DataFrame(dict1)
print(df1)

df1["Address"] = ["Delhi", "Faridabad", "Noida"]
df1["Status"] = df1["Marks"] > 80
df1.insert(2,"Branch", ["CSE", "IT", "ML"])
print(df1)

df1.to_csv(r"csedata.csv")  #to write a file .csv
df1.to_excel(r"csedata.xlsx")   #to write a file .xlsx
'''


'''
import pandas as pd
#df2 = pd.read_excel(r"Book1.xlsx")
#print(df2)
df2 = pd.read_csv(r"Book1.csv")
print(df2)
print("Total count", df2.Name.count())
print("Sub1", df2.Subject1.max())

#aggregate()   #used to apply more than one function on desired column
print(df2.aggregate(['sum','max','min','count']))
'''



#Grouping: groupby()
'''
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Name':["Aman", "Aditya", "Aditi", "Ram", "Aditi", "Aman", "Aman"],
    'Roll':["A","B","C","A","B","C","A"],
    'Marks':np.random.randint(11,19,size=(7,)),
    'Total':np.random.randint(85,99,size=(7,))})
print(df)
x = df.groupby("Name")
print(x)
print(x.groups)
'''



#merging two dataframe
'''
import pandas as pd
sts = pd.DataFrame({
    "Name":["Virat","Rohit","Kuldeep","Rahul","Shreyash","Subhman","Shami"],
    "Teams":["RCB","MI","DC","LSG","PKB","GT","SRH"]})
#print(sts)
sts1 = pd.DataFrame({
    "Name":["Virat","Rohit","Kuldeep","Rahul","Shreyash","Subhman","Shami","Raju","Loki"],
    "Score":[23,34,54,65,74,23,12,46,99]})
#print(sts1)
rst = pd.merge(sts, sts1)
print(rst)
rst = pd.merge(sts, sts1, on = "Name", how = "inner")
print(rst)
rst = pd.merge(sts, sts1, on = "Name", how = "outer")
print(rst)
rst = pd.merge(sts, sts1, on = "Name", how = "left")
print(rst)
rst = pd.merge(sts, sts1, on = "Name", how = "right")
print(rst)
'''



#apply functions on dataframes

import pandas as pd
student = pd.DataFrame({
    'name':["Ram", "Shyam", "Raju", "Kaju", "Golu", "Harsh", "Monu", "Sonu"],
    'marks1':[43,24,15,32,54,25,32,98],
    'marks2':[24,62,82,27,73,83,93,87]})
print(student)
def check(row):
    if row['marks1'] > 30:
        return 'Pass'
    else:
        return 'Fail'

student['Result'] = student.apply(check, axis=1)
print(student)

def grade(row):
    total = row['marks1'] + row['marks2']
    per = (total*100)/200
    if per >= 90:
        return 'A'
    elif per >=80:
        return 'B'
    elif per >= 70:
        return 'C'
    elif per >=60:
        return 'D'
    elif per >= 50:
        return 'E'
    else:
        return 'F'

student['Grade'] = student.apply(grade, axis=1)
student.to_csv(r"day8.csv")
print(student)
print(student.describe())




