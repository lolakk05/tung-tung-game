import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

pygame.init()
width = 736
height = 474
bg_image = pygame.image.load('utils/background.jpg')
font = pygame.font.SysFont('Corbel', 35)

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


def create_surface_with_text(text, font_size, text_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, text_rgb, action=None):
        self.mouse_over = False
        
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb
        )
        
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size*1.2, text_rgb=text_rgb
        )
        
        self.images = [default_image, highlighted_image]
        
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)
        ]
        
        self.action = action
        
        super().__init__()
    
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    game_state = GameState.TITLE
    
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            # game_state = play_level(screen)
            continue

        if game_state == GameState.QUIT:
            pygame.quit()
            return
        

def title_screen(screen):
    # start konczy gre, paradoks startu
    start_btn = UIElement(
        center_position=(width/2, height/2),
        font_size=30,
        text_rgb=(255, 255, 255),
        text="Start",
        action=GameState.NEWGAME
    )
    
    quit_btn = UIElement(
        center_position=(width/2, height/2+50),
        font_size=30,
        text_rgb=(255, 255, 255),
        text="Quit",
        action=GameState.QUIT
    )

    buttons = [start_btn, quit_btn]
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg_image, (0, 0))
        
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
