from src.movable import Movable


class Ghost(Movable):
    def __init__(self, x: int = None, y: int = None):
        super().__init__(x, y)
        self.target_x = 0
        self.target_y = 0
        self.state = "Home"

    def eaten_state(self):
        self.state = "eaten"

    def frightened_state(self):
        self.state = "frightened"

    def is_eaten(self):
        return self.state == "eaten"

    def chase_state(self):
        self.state = "chase"

    def backward_move(self, x, y):
        return x == 0 and y == -self.y_vel or y == 0 and x == -self.x_vel

    def shortest_path(self, backward=False):
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        min_dist = float("inf")
        min_index = 0
        for i in range(len(step_x)):
            if (not self.backward_move(step_x[i], step_y[i]) or backward) and not self.board.is_wall(self.x + step_x[i],
                                                                                                     self.y + step_y[
                                                                                                         i]):
                dist = (self.x + step_x[i] - self.target_x) ** 2 + (self.y + step_y[i] - self.target_y) ** 2
                if dist < min_dist:
                    min_dist = dist
                    min_index = i
        return step_x[min_index], step_y[min_index]

    def set_velocity(self):
        self.x_vel, self.y_vel = self.shortest_path()

    def step(self):
        self.prev_x, self.prev_y = self.x, self.y
        self.set_velocity()

        newX = self.x + self.x_vel
        newY = self.y + self.y_vel

        if not self.board.is_wall(newX, newY):
            self.x, self.y = newX, newY

    def set_target(self):
        if self.state == "home":
            self.chase_state()
        elif self.state == "eaten":
            pass
        elif self.state == "chase":
            self.chase_state_target()
        elif self.state == "frightened":
            pass

    def chase_state_target(self):
        return