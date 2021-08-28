import pygame as pg

class Game():
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((700, 500))
        self.screencolor = (255, 255, 200)
        self.running = True
    
    def new(self):
        self.run()
        
    def run(self):
        self.screen.fill(self.screencolor)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYUP:
                self.screencolor = (40, 255, 255)
        self.update()
        
    def update(self):
        pg.display.flip() 
        self.clock.tick(60)   


g = Game()
while g.running:
    g.new()