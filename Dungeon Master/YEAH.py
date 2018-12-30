import pygame
import os
import time

clock = pygame.time.Clock()
pygame.init()
screenSize = 1200, 650
running = True
display = pygame.display.set_mode(screenSize)
display.fill(pygame.Color(0,0,0))
pygame.mixer.music.load('audio/DungeonMaster.wav')
pygame.mixer.music.play(1)
time.sleep(1.1)
pygame.mixer.music.load('audio/main.mid')
pygame.mixer.music.play(-1)

HPchar = 100
HPenemy = 100
steps = 10
red = (255, 50 , 50)
green = (50, 255, 50)
text = "START"
font = pygame.font.Font(None ,50)
TextSurf = font.render(text, True, green)
TextRect = TextSurf.get_rect()
TextRect.center = ((1200/2),(650/2))
display.blit(TextSurf, TextRect)


textName = "DUNGEON MASTER"
font = pygame.font.Font(None , 90)          #pygame.font.Font(None , 90).render(textName, True, red).get_rect().center= ((1200/2),(650/4))
namePr = font.render(textName, True, red)
nameRect = namePr.get_rect()
nameRect.center = ((1200/2),(650/4))
display.blit(namePr, nameRect)

healthbarimg  = pygame.image.load("images/healthbars.jpg").convert() 
# textName = "HP"
# font = pygame.font.Font(None , 50)          #pygame.font.Font(None , 90).render(textName, True, red).get_rect().center= ((1200/2),(650/4))
# namePr = font.render(textName, True, red)
# nameRect = namePr.get_rect()
# nameRect.center = ((1200/2),(650/4))
# display.blit(namePr, nameRect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.images = []
        for i in range(1,4):
            img = pygame.image.load(os.path.join('images','shooter' + str(i) + '.jpg')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey((0, 0, 0)) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y
    
    def update(self):
        '''
        Update sprite position
        '''

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

class Text:
    def __init__(self, text, positionH, positionW, color):
        self.text = text
        self.positionH = positionH
        self.positionW = positionW
        self.color = color
        
    def renderFunct(this): 
        font = pygame.font.Font(None , 35)          #pygame.font.Font(None , 90).render(textName, True, red).get_rect().center= ((1200/2),(650/4))
        namePr = font.render(this.text, True, this.color)
        nameRect = namePr.get_rect()
        nameRect.center = (this.positionH, this.positionW)
        display.blit(namePr, nameRect)

 
class HPbars:
    def __init__(self, widthOffset, heightOffset,currentHP, barHeight):
        self.widthOffset = widthOffset
        self.heightOffset = heightOffset
        self.currentHP = currentHP
        self.barHeight = barHeight
        self.rect = pygame.Rect(self.widthOffset,self.heightOffset,self.currentHP*2, self.barHeight)
        pygame.draw.rect(display,red,self.rect)
    def createRect(this):
        this.rect.inflate(100 - this.currentHP*2,0)
        
        

running = True 
player = Player()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if TextRect.collidepoint(x, y):
                backgroundImage = pygame.image.load("images/bg.jpg").convert()
                display.blit(backgroundImage, (0,0))
                # pygame.display.update()
                # spawn player block
                  # spawn player
                player.rect.x = 600   # go to x
                player.rect.y = 450   # go to y
                player_list = pygame.sprite.Group()
                player_list.add(player)
                player_list.draw(display)
                #drawing rect
                hpbarChar = HPbars(10, 40, HPchar, 20)
                hpbarChar.createRect()
                hpbarEnemy = HPbars(990, 40, HPenemy, 20)
                hpbarEnemy.createRect()
                
                # pygame.draw.rect(display,red,(10,40,HPchar*2, 20))
                # pygame.draw.rect(display,red,(990,40,HPenemy*2, 20))
                #calling hp text
            Text1 = Text("HP", 100 , 25, green) 
            Text1.renderFunct()
            Text2 = Text("HP", 1095 , 25, red) 
            Text2.renderFunct()
        #how to read keypresses    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               player.control(-steps,0)
             
            player_list.draw(display)
            player.update() 
            
        # display.blit(backgroundImage, (0,0))
        #pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


    