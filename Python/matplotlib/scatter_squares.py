import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]
# edgecolors删除数据点的轮廓，c定义颜色，colormap颜色映射
plt.scatter(x_value, y_value, c='red',
            cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title('Square Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
# 自动保存图表,前者保存文件名，后者裁剪掉空白区域
plt.savefig('squares_plot.png', bbox_inches='tight')
