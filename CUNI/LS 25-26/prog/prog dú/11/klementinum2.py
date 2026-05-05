import matplotlib.pyplot as plt
import csv

x = []
y = []
i = 0

with open('PKLM.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if i != 0:
            x.append(int(row[0]))
            y.append(int(row[1]))
        i +=1

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
