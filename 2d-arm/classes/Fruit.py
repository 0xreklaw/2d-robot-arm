class Fruit:
    def __init__(self, draw_func, x, y):
        self.draw_func = draw_func
        self.x = x
        self.y = y
        self.dragging = False

    def draw(self, screen):
        self.draw_func(screen, self.x, self.y)

    def is_mouse_over(self, mouse_pos):
        # Assuming fruits are drawn as circles with a radius of 20
        return (mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2 < 20 ** 2
