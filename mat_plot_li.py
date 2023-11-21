# pip3 install matplotlib
import matplotlib.pyplot as plt
Partition = 'Python', 'JavaScript', 'C++', 'C'
sizes = [400, 300, 200, 100]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()