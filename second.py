import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scienceplots as sp

# 使用Scienceplots风格
plt.style.use('science')

# 创建一个Figure对象，设置图形大小
fig = plt.figure(figsize=(14,7 ))



x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# example variable error bar values
yerr1 = 0.1 + 0.2*np.sqrt(x)
xerr1 = 0.1 + yerr1

# 绘制图像
plt.errorbar(x, y, xerr=xerr1, yerr=yerr1, label='$yerr=0.1+\sqrt{x},xerr=0.1+yerr$', color='b')

# 添加坐标轴标签
plt.xlabel('X Axis (units)')
plt.ylabel('Y Axis (units)')

# 添加图例
plt.legend(loc='upper right')

plt.style.use('science')
x = np.linspace(0, 30, 100)
y = np.sin(x) * 0.5

x1 = np.linspace(0, 30, 30)
y1 = np.sin(x1 / 6 * np.pi)
error1 = np.random.normal(0.1, 0.02, size=y1.shape) + 0.1
y1 += np.random.normal(0, 0.1, size=y1.shape)

x2 = np.linspace(0, 30, 30)
y2 = np.cos(x2/6*np.pi)
error2 = np.random.normal(0.1, 0.02, size=y2.shape) + 0.1
y2 += np.random.normal(0, 0.1, size=y2.shape)


x3 = np.linspace(0, 30, 30)
y3 = np.cos(x3 / 6 * np.pi) + np.sin(x3 / 3 * np.pi)
error3 = np.random.normal(0.1, 0.02, size=y3.shape) + 0.1
y3 += np.random.normal(0, 0.1, size=y3.shape)

# 创建图二,调整大小
plt.figure(figsize=(6, 4))  
plt.plot(x, y, '-k', label="Sine Wave")
plt.fill_between(x1, y1 - error1, y1 + error1, alpha=0.5, edgecolor='#CC4F1B', facecolor='#CC4F1B', label='data1:$\sin(\dfrac{\pi x}{6})$')
plt.fill_between(x2, y2 - error2, y2 + error2, alpha=0.5, edgecolor='#1B2ACC', facecolor='#1B2ACC', label='data2:$\cos(\dfrac{\pi x}{6})$')
plt.fill_between(x3, y3 - error3, y3 + error3, alpha=0.2, edgecolor='#3F7F4C', facecolor='#089FFF', linewidth=4,
                 linestyle='dashdot', antialiased=True,label="data3:$\cos(\dfrac{\pi x}{6})+\sin(\dfrac{\pi x}{6})$")
# 保存图像为PDF格式

plt.legend()
plt.savefig('journal_figure.pdf', format='pdf', dpi=300)

# 显示图像
plt.show()
