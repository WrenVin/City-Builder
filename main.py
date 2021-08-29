import pygame as pg
from os import path
from settings import *
from sprites import *
from tilemap import *
from pytmx import TiledObjectGroup
from platform import system
from sys import exit
from pygame.locals import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        flags = RESIZABLE
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), flags)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.redposx, self.redposy = self.screen.get_width()/2, self.screen.get_height()-40
        self.dragging = False
        self.squares = []
        #self.squares.append(pg.Rect(self.screen.get_width()/2, self.screen.get_height()-40, 30, 40))
        


    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.load_data()
        
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        exit()

    def update(self):
        self.screen.fill(GREEN)
        self.bluebar = pg.draw.rect(self.screen, BLACK, pg.Rect(0, self.screen.get_height()*(4.7/5), self.screen.get_width(), self.screen.get_height()*0.3/5))
        if self.dragging:
            self.redposx, self.redposy = pg.mouse.get_pos()
        pg.draw.rect(self.screen, RED, pg.Rect(self.redposx, self.redposy, 30, 40))
        self.redRect = pg.draw.rect(self.screen, RED, pg.Rect(self.screen.get_width()/2, self.screen.get_height()-40, 30, 40))
        if len(self.squares) != 0:
            for square in self.squares:
                pg.draw.rect(self.screen, RED, square)
        
    def draw(self):
        #for sprite in self.all_sprites:
            #self.screen.blit(sprite.image, self.camera.apply(sprite))
        #self.screen.blit(self.cursor, pg.mouse.get_pos())
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif event.type == pg.VIDEORESIZE:
                self.screen = pg.display.set_mode((event.w, event.h),
                                        pg.RESIZABLE)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.redRect.collidepoint(pg.mouse.get_pos()):
                    self.dragging = True
            elif event.type == pg.MOUSEBUTTONUP:
                x = self.redposx
                y = self.redposy
                print(len(self.squares))
                
                if self.dragging:
                    self.squares.append(pg.Rect(x, y, 30, 40))
                print(self.squares)
                self.dragging = False
        
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)        

    def show_start_screen(self):
        pass
        
    def wait_for_key(self):
        waiting = False
        while waiting:
            keys = pg.key.get_pressed()
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
                           
    def show_go_screen(self):
        pass
        
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
