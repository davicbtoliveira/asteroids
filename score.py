import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


class Score():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(f"Score: {self.score}", True, "white")

    def increase(self):
        self.score += 1
        self.text = self.font.render(f"Score: {self.score}", True, "white")

    def display(self):
        self.screen.blit(self.text, (10, 10))
