import pygame.image
from View import View


class ImageView(View):

    def __init__(self):
        super().__init__()

        self.image_path = None
        self.image = None
        self.scaled_image = None
        self.alpha = 255

    def get_image_path(self):
        return self.image_path

    def get_image(self):
        return self.image

    def get_scaled_image(self):
        return self.scaled_image

    def set_image_by_path(self, image_path):
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.scaled_image.set_alpha(self.alpha)

    def show_view(self, screen):
        if self.is_visible:
            if self.should_be_centered:
                screen.blit(self.scaled_image, (self.get_centered_x(), self.get_centered_y()))
            else:
                screen.blit(self.scaled_image, (self.x, self.y))
