class View:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.is_visible = True
        self.should_be_centered = False

    def get_x(self):
        return self.x

    def get_centered_x(self):
        return self.x + 0.5 * self.width

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def get_centered_y(self):
        return self.y - 0.5 * self.height

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_is_visible(self):
        return self.is_visible

    def set_visible(self, is_visible):
        self.is_visible = is_visible

    def get_should_be_centered(self):
        return self.should_be_centered

    def set_should_be_centered(self, should_be_centered):
        self.should_be_centered = should_be_centered
