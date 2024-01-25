import pygame
from settings import *

class Game_over_screen:
    def __init__(self, player):
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(UI_FONT, 20)
        
        #Message Box
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 3
        
        left = self.display_surface.get_size()[0] * 0.35
        top = self.display_surface.get_size()[1] * 0.1
        
        self.box = Box(left,top,self.width,self.height,self.font)
             
    def display(self):
        self.box.display(self.display_surface)
    
class Box: 
    def __init__(self, l, t, w, h, font):
        self.rect = pygame.Rect(l,t,w,h)
        self.font = font

    def display_text(self,surface):
        color = TEXT_COLOR
        
        # background
        pygame.draw.rect(surface, TEXT_COLOR_SELECTED, self.rect)
        
        # title (Game over) 
        title_surf = self.font.render('You are dead',False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,200))

		# Text
        text_surf = self.font.render('Press -R- to restart' ,False,color)
        text_rect = text_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

		# draw 
        surface.blit(title_surf,title_rect)
        surface.blit(text_surf, text_rect)
        
    def display(self, surface):
        self.display_text(surface)