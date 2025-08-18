import pygame.display
from pygame import Rect, Surface
from pygame.font import Font

from src.consts import COLOR_WHITE, WIN_HEIGHT
from src.entity import Entity
from src.entity_factory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.timeout = 20000  # 20 segundos

    def run(self):
        pygame.mixer_music.load(f"./assets/{self.name}.flac")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:

            clock.tick(30)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.level_text(
                14,
                f"{self.name} - Timeout: {self.timeout /1000 :.1f}s",
                COLOR_WHITE,
                (10, 5),
            )
            self.level_text(
                14, f"fps: {clock.get_fps() :.0f}", COLOR_WHITE, (10, WIN_HEIGHT - 35)
            )
            self.level_text(
                14,
                f"entidades: {len(self.entity_list)}",
                COLOR_WHITE,
                (10, WIN_HEIGHT - 20),
            )
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
