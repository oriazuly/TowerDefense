
from View import *

class TextView(View):

    def __init__(self):
        super().__init__()

        self.text = None
        self.text_rect = None
        self.font = None
        self.content = ""
        self.font_name = ""
        self.font_size = 0
        self.color = (255, 255, 255)

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_font_name(self):
        return self.font_name

    def set_font_name(self, font_name):
        self.font_name = font_name

    def get_font_size(self):
        return self.font_size

    def set_font_size(self, font_size):
        self.font_size = font_size

    def get_font_color(self):
        return self.color

    def set_font_color(self, color):
        self.color = color

    def show_view(self, screen):
        if self.is_visible:
            pygame.font.init()
            self.font = pygame.font.SysFont(self.font_name, self.font_size)
            self.text = self.font.render(self.content, True, self.color)

            if self.should_be_centered:
                self.text_rect = self.text.get_rect(center=self.get_centered_position())
                screen.blit(self.text, self.text_rect)
            else:
                screen.blit(self.text, self.get_position())
