from pollen_grain import GrainPoll
import matplotlib.pyplot as mat

pg = GrainPoll(5_000)
pg.random_walk()

mat.style.use('classic')
fig, ax = mat.subplots()

# Use plot instead scatter
# ax.plot(pg.x_values, pg.y_values, linewidth=1)

ax.scatter(pg.x_values, pg.y_values, cmap=mat.cm.Blues)

mat.show()
