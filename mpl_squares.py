import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 23, 22, 12, 13, 13, 11, 10]
fig, ax = plt.subplots()
# ax.plot(squares)
# plt.show()

# Настройка визуализации
ax.plot(squares, linewidth=2)

# Назначение заголовка диаграммы и меток
ax.set_title('Square Numbers', fontsize=10)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of Value', fontsize=10)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=10)

plt.show()


