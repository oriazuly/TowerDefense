
from Constants import *
from TextView import TextView
from View import *

run = True
pygame.display.set_caption("Tower Defense")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
a = TextView()
a.set_x(100)
a.set_y(100)
a.set_width(100)
a.set_height(100)
a.set_font_name("Ariel")
a.set_font_size(100)
a.set_font_color((255, 255, 255))
a.set_content("hi this is works")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    a.show_view(SCREEN)
    pygame.display.update()
pygame.quit()
