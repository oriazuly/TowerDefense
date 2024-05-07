import pygame

from View import View


class Button(View):

    def __init__(self):
        super().__init__()

        self.text = None
        self.function = None

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_function(self):
        return self.function

    def set_function(self, function):
        if function is not None and not callable(function):
            raise Warning("The new function is not callable!")

        self.function = function

    def is_clicked(self, mouse_position):
        return self.x <= mouse_position[0] <= self.x + self.width and self.y <= mouse_position[1] <= self.y + self.height

    def perform_action(self, params):
        if callable(self.function):
            self.function(params)

    def show_view(self, screen):
        if self.is_visible:
            pygame.font.init()
            font = pygame.font.SysFont("ariel", 16)
            font = font.render(self.text, True, (255, 255, 255))

            if self.should_be_centered:
                screen.blit(font, font.get_rect(center=(self.get_centered_x(), self.get_centered_y())))
            else:
                screen.blit(font, (self.x, self.y))
