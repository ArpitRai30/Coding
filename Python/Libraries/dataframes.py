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
