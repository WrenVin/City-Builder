import pygame as pg
import os

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
FPS = 60

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    
    def load(self):
        #self.spaceshipRed = pg.image.load(os.path.join('Assets', 'spaceship_red.png'))
        #self.spaceshipYellow = pg.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
        #pg.display.set_caption('Tutorial Game')
        #pg.display.set_icon(self.spaceshipRed)
        pass

    def draw(self):
        self.screen.fill(WHITE)
        #self.screen.blit(self.spaceshipRed, (300, 100))
        pg.display.update()
        
    def main(self):
        self.clock = pg.time.Clock()
        self.running = True
        
        while self.running:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            self.draw()
                
        pg.quit()
        quit()
        

if __name__ == '__main__':
    game = Game()
    game.load()
    game.main()