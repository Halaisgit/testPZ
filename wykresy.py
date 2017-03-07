import matplotlib.pyplot as plt

x = []
y = []
c = []

f = open('train')

for line in f:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    c.append(float(line.split()[2]))

print (x)
print (y)

plt.axis([-10,10,-10,10])
for i in range(len(c)):
    if c[i] == 1:
        plt.plot(x[i],y[i],'ro',color ='red')
    elif c[i] == -1:
        plt.plot(x[i], y[i], 'ro', color='yellow')
    else:
        plt.plot(x[i], y[i], 'ro', color='blue')

plt.show()