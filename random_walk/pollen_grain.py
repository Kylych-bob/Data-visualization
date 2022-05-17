from random import choice


class GrainPoll:
    def __init__(self, num_poll):
        self.num_poll = num_poll

        self.x_values = [0]
        self.y_values = [0]

    def random_walk(self):
        while len(self.x_values) < self.num_poll:
            x_st = self.get_step()[0]
            y_st = self.get_step()[1]

            if x_st == 0 and y_st == 0:
                continue

            x = self.x_values[-1] + x_st
            y = self.y_values[-1] + y_st

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction_x = choice([1, -1])
        distance_x = choice([1, 2, 3, 4, 5])
        step_x = direction_x * distance_x

        direction_y = choice([1, -1])
        distance_y = choice([1, 2, 3, 4, 5])
        step_y = direction_y * distance_y
        return step_x, step_y











