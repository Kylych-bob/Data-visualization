import matplotlib.pyplot as plt

# # x_values = [1, 2, 3, 4, 5]
# # y_values = [1, 4, 9, 16, 25]
#
# x_values = list(range(1, 1_001))
# y_values = [x**2 for x in x_values]
#
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# # ax.scatter(x_values, y_values, s=10)
# # Определение цвета
# # красный
# # ax.scatter(x_values, y_values, c='red', s=5)
# # зеленый
# # ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=5)
# # Colormap
# # ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.prism, s=5)
#
# # Название заголовка диаграммы и меток осей.
# ax.set_title('Square Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Square of Value', fontsize=14)
#
# # Назначение размера шрифта делений на осях
# ax.tick_params(axis='both', which='major', labelsize=10)
#
# # Назначение диапазона для каждой оси.
# ax.axis([0, 1_100, 0, 1_100_000])
#
# plt.show()

# -------------------------------------------------------------------
# Кубы

num1 = [2, 3, 4, 5, 6]
num2 = [x ** 3 for x in num1]

num1 = list(range(1, 5_001))
num2 = (x ** 3 for x in num1)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(num1, list(num2))

plt.show()













