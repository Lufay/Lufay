import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

print(matplotlib.matplotlib_fname())

# x = np.linspace(-5, 5, 20)
# y = x*x +1

# # plt.plot(x, y, 'y--_',
# #          x+3, y, "r:x",
# #          x+6, y, "b-D", label='first')
# # # plt.scatter(x, y)

# # plt.xticks([-5, -2, -1])
# # plt.yticks([2, 5, 10, 20], ['two', 'five', 'ten', 'twen'])

# # plt.legend(loc='upper left')

# # plt.annotate('sample points', xy=(x[2], y[2]), xytext=(-5, 5), arrowprops={"facecolor": "black", "shrink": 0.05})
# # plt.title('Easy Matplot', fontdict={"fontsize":20}, loc='center')
# # plt.xlabel('X values', fontdict={"fontsize":12})
# # plt.ylabel('Y values', fontdict={"fontsize":12})
# # plt.text(x[1], y[1], 'kaf', va='top', ha='right')

# # plt.grid(True,'both','both',linestyle ='-',color = "red",linewidth="0.5")

# # plt.show()

# # ax1 = plt.subplot(2,2,3)
# # ax2 = plt.subplot(1,2,2)
# # ax2.spines['top'].set_color('none')
# # plt.show()

# fig = plt.figure(figsize=(6, 4))
# # fig, ax = plt.subplots()
# # fig.subplots_adjust(top=0.8, bottom=0.2, left=0.1, right=0.9)

# labels = ['Apple', 'Banana', 'Grapes', 'Kiwi', 'Orange']
# labels.extend(string.ascii_lowercase)
# sizes = [20, 15, 25, 10, 17]
# sizes.extend([0.5]*26)
# two = [10, 10, 15, 5, 20, *([1]*26)]

# # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90) # , shadow=True
# plt.bar(labels, sizes)
# plt.bar(labels, two)


# # 设置图表标题
# plt.title('Fruit preference')
# plt.xlabel('psm')
# plt.ylabel('rate')

# # # 饼图参数设置
# # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
# # explode = (0.1, 0, 0, 0, 0)  # 突出显示某些扇形

# # # 创建饼图
# # plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
# #         shadow=True, startangle=90)

# # # 设置图表标题
# # plt.title('Fruit preference', fontweight='bold', fontsize=14)

# # # 添加图例
# # plt.legend(labels, loc='best')

# # # 显示图表
# # plt.show()

# canvas = FigureCanvas(fig)
# canvas.print_figure('a.png', dpi=80)

x = np.array(['JAN 01', 'JAN 02', 'JAN 03', 'JAN 04'])
y = np.random.randn(4)

fig, ax = plt.subplots()
ax.plot(x, y)

# 使用缩略词
x_tick_labels = ['01', '02', '03', '04']
ax.set_xticklabels(x_tick_labels, rotation=90)

plt.show()