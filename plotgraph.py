import matplotlib.pyplot as plt
import pandas as pd
#Reading CSV file
data=pd.read_csv("sww.csv")

x=data['State/UT']
y=data['All Schools']
#Printing values
print(x)

#fig=plt.figure()
plt.title("Bar Graph",color='r')
plt.xlabel("State",color='g')
plt.ylabel("All schools",color='g')

plt.bar(x,y,color='y')

data.plot(color='r')
plt.scatter(x,y,color='g')
data.min()

plt.show()
