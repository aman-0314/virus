import pygame,sys,random

class Mygame():
    def main(self):
        Xspeed=10
        Yspeed=10
        livesinit=5
        
        paddlespeed=30
        points=0
        bgcolor=0,0,0
        size=width.height =500,500
        
        pygame.init()
        screen=pygame.display.set_mode(size)
        
        paddle=pygame.image.load('bat.jfif')
        paddlerect=paddle.get_rect()
        
        ball=pygame.image.load('ball.jfif')
        ballrect=ball.get_rect()
        
        sound=pygame.mixer.sound