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

while True:
    # Построение случайного блуждания.
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму.

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
