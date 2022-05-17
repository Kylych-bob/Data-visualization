import matplotlib.pyplot as plt
from random_walk import RandomWalk

# # Построение случайного блуждания.
# rw = RandomWalk()
# rw.fill_walk()
#
# # Нанесение точек на диаграмму.
#
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

# ------------------------------------------------------------

# Новые блуждания строятся до тех пор,
# пока программа остается активной.

# while True:
#     # Построение случайного блуждания.
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # Нанесение точек на диаграмму.
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     # ax.scatter(rw.x_values, rw.y_values, s=15)
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values,
#                c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='None', s=15)
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n): ')
#     if keep_running == 'n':
#         break

# ------------------------------------------------------------
# Начало и конец блуждания

# while True:
#     # Построение случайного блуждания.
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     # ax.scatter(rw.x_values, rw.y_values, s=15)
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values,
#                c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='None', s=15)
#
#     # Выделение первой и последней точек.
#     ax.scatter(0, 0, c='green',
#                edgecolors='none', s=50)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
#                edgecolor='none', s=50)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n): ')
#     if keep_running == 'n':
#         break

# ------------------------------------------------------------
# Удаление осей

# while True:
#     # Построение случайного блуждания.
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     # ax.scatter(rw.x_values, rw.y_values, s=15)
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values,
#                c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='None', s=15)
#
#     # Выделение первой и последней точек.
#     ax.scatter(0, 0, c='green',
#                edgecolors='none', s=50)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
#                edgecolor='none', s=50)
#
#     # Удаление осей.
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n): ')
#     if keep_running == 'n':
#         break

# ------------------------------------------------------------
# Добавление точек

# while True:
#     rw = RandomWalk(50_000)
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values,
#                c=point_numbers, cmap=plt.cm.Blues,
#                edgecolor='None', s=1)
#     # ax.scatter(rw.x_values, rw.y_values,
#     #            c=point_numbers, cmap=plt.cm.Blues,
#     #            edgecolors='None', s=15)
#
#     ax.scatter(0, 0, c='green',
#                edgecolors='None', s=50)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
#                edgecolor='None', s=50)
#
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n): ')
#     if keep_running == 'n':
#         break

# ------------------------------------------------------------
# Изменение размера диаграммы для заполнения экрана
# while True:
#
#     rw = RandomWalk(5_000)
#     rw.fill_walk()
#
#     plt.style.use('classic')
#     # размер диаграммы
#     fig, ax = plt.subplots(figsize=(15, 9))
#
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values,
#                c=point_numbers, cmap=plt.cm.Blues,
#                edgecolors='none', s=15)
#
#     ax.scatter(0, 0, c='green',
#                edgecolors='none', s=50)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1],
#                c='red', edgecolors='none', s=50)
#
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n): ')
#     if keep_running == 'n':
#         break

# ------------------------------------------------------------












