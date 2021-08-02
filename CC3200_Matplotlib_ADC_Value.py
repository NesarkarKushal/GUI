# Scattered Graph

import serial
import matplotlib.pyplot as plt

ser=serial.Serial('COM15',9600)

plt.ion()
# fig=plt.figure()
i=0;
x=list()
y=list()
plt.grid()

while True:
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())
    # plt.scatter(i,float(data.decode())
    # plt.stem(i,float(data.decode()))
    plt.bar(i,float(data.decode()))

    i+=1
    plt.show()
    plt.pause(0.0001)

