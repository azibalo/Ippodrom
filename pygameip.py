import pygame
import random
FPS = 60

class Horse():
    def __init__(self,screen,y,num):
        self.scr=screen
        self.speed=0
        self.num=num
        self.im = pygame.image.load("ip.png").convert_alpha()
        self.im = pygame.transform.scale(self.im, (220,220))
        self.im = pygame.transform.flip(self.im, 1, 0)
        self.im_rect = self.im.get_rect()
        self.im_rect.y=y
        self.blit()
    def blit(self):
        self.scr.blit(self.im, self.im_rect)

    def update(self):
        self.speed=random.randint(0,18)
        self.im_rect.x+=self.speed
        print("Лошадь {} - скорость {} положение {}".format(self.num,self.speed,self.im_rect.x))
        self.blit()

    @property
    def finish(self):
        if self.im_rect.x >=self.scr.get_size()[0]:
            return True
        else:
            return False

class Horses():
    def __init__(self,N,screen):
        self.N=N
        self.horses = []
        h = screen.get_size()[1]
        h1 = h // N
        for i in range(0, N):
            self.horses.append(Horse(screen, (0 + i) * h1,i+1))

    def update(self):
        for i in self.horses:
            i.update()

    @property
    def is_finish(self):
        for i in range(0, self.N):
            if self.horses[i].finish:
                return i
        return -1


def init(N):
    p=True
    screen=pygame.display.set_mode((0, 0), (pygame.FULLSCREEN | pygame.DOUBLEBUF))
    pygame.init()
    clock = pygame.time.Clock()
    bg= pygame.image.load("fon.jpg").convert_alpha()
    bg = pygame.transform.scale(bg, screen.get_size())
    bg_rect= bg.get_rect()
    hors=Horses(N,screen)
    while p:
        clock.tick(FPS)
        screen.blit(bg, bg_rect)
        hors.update()
        pygame.display.update()
        win=hors.is_finish
        if win>=0:
            p=False
    pygame.quit()
    return win+1