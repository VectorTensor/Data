import  numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import requests
url='http://127.0.0.1:8000/api/'

r= requests.get(url)
events = r.json()
print(events)
x=len(events)
#print(x)
a=[]# for X

b=[]#for Y
for event in events:
    a.append(event['X'])
    b.append(event['Y'])


dataX=np.array(a)#Making numpy array of data X
dataY=np.array(b)#Making numpy array of data Y

meanX= dataX.mean()
meanY=dataY.mean()

print(f'X\t\t\tY')
#Printing the table 
for (i,j) in zip(dataX,dataY):
    print(f'{i} \t\t\t{j}')
    
print("___________________________________________________")

print(f'{meanX}\t\t\t{meanY}')


fig,ax=plt.subplots()
ax.scatter(dataX,dataY)
ax.set_xlabel("X")
ax.set_ylabel(("Y"))
plt.show()
