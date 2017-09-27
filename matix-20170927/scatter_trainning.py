# -*- coding:utf8 -*-
import matplotlib.pyplot as plt

x_values=list(range(1,101))
y_values=[x**2 for x in x_values]

#必须放在scatter语句之前
#中文注释需要增加第一行编码格式说明
plt.figure(figsize=(10, 6))

plt.scatter(x_values, y_values, edgecolor='none', c='black', s=20)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=10)

#plt.tick_params(axis="both",which='major', width=1, labelsize=10)

plt.axis([0, 101, 0, 10010])

plt.show()