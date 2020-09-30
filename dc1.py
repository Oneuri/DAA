'''
import matplotlib.pyplot as urjit
year=[2017,2018,2019,2020]
pop=[2.22,3.33,4.44,5.55]
urjit.plot(year,pop)
urjit
urjit.xlabel('Year')
urjit.ylabel('Population')
urjit.title('GRAPH')

urjit.show()
''
import datetime
x = datetime.datetime.now()
print(x.strftime('%x'))

''
import json

x='{"name": "json","age": 20,"city": "Aurangabad"}'

p='{"name": "urjit","age": 20,"city": "Pune"}'

m='{"name": "Piyush","age": 20,"city": "Banglore"}'

y=json.loads(x)
q=json.loads(p)
n=json.loads(m)
s=json.dumps(p)

print(y["age"])
print(q["name"])
print(n["city"])
print(s)
''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

''

username = input("Enter username: ")
print("Username is: "+username)
''

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))



f = open("demofile.txt", "r")
print(f.read(5))
''

from scipy import stats
speed=[10,20,20,20,30,30,30,40,40,40,40,50,50,50,60,60,60,40,40,60,50,50]
x=stats.mode(speed)
print(x)

''
from scipy import stats

speed = [103,99,86,87,88,86,103,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
''

import numpy
speed = [103,99,86,87,88,86,103,103,87,94,78,77,85,86]
x=numpy.std(speed)
print(x)
''
 
import numpy
speed = [103,99,86,87,88,86,103,103,87,94,78,77,85,86]
x=numpy.mean(speed)
print(x)
''

import numpy
speed = [103,99,86,87,88,86,103,103,87,94,78,77,85,86]
x=numpy.median(speed)
print(x)
''

import numpy
speed = [103,99,86,87,88,86,103,103,87,94,78,77,85,86]
x=numpy.var(speed)
print(x)
''


import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages,10)

print(x)


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

''
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
''
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
''
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
''
import matplotlib .pyplot as plt
from scipy import stats


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope* x + intercept

mymodel = list(map(myfunc,x))

plt.scatter(x,y,color='red')

plt.plot(x,mymodel,color='yellow')
plt.show()
''
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
''


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
''
s = 'hi i am urjit'
s.split()
''

def domainGet(email):
    return email.split('@')

'''
import numpy as np
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.arr(my_mat)
