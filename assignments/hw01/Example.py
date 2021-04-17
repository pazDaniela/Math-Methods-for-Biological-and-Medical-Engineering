from BlackBox import BlackBox1, BlackBox2
from numpy import array

v = array([1,2,3,4,5]) #message to be encryoted
u = BlackBox1().encrypt(v) #encription
print(u)

v = array([1,2,3,4]) #message to be encryoted
u = BlackBox2().encrypt(v) #encription
print(u)