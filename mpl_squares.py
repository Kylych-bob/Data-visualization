import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]



# plt.style.use('seaborn')
# plt.style.use('bmh')
plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# ax.plot(squares)
# plt.show()

# Настройка визуализации
ax.plot(squares, linewidth=3)

# Назначение заголовка диаграммы и меток
ax.set_title('Square Numbers', fontsize=10)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of Value', fontsize=10)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=7)

plt.show()


