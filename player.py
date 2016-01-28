import pygame,time

positionlist =[(742,738),(637,715),(576,715), (512,715),(448,715),(385,715),(320, 715),(256,715),(192,715),(129,715)
,(52, 775),(52, 640),(52, 575), (52, 510),(52,455),(52, 390),(52,325),(52,260),(52,195),(52, 130),(30,35),
(130,30),(195,30),(260,30),(325,30),(390,30),(450,30),(515,30),(580,30),(640,30),(735,30),
(735,130),(735,195),(735,260),(735, 325),(735, 390),(735, 455),(735,510),(735,575),(735,650)]

class player:
    def __init__(self,player,position,char,money,i):
        self.player = player
        self.position = position
        self.char = char
        self.money = money
        self.i = i

    def move(self, dobbel):
        for t in range(0,dobbel):
            currenti = self.i
            next= currenti + 1
            if next> 39 :
                next = 0
            self.position = positionlist[next]
            self.i = next
            time.sleep(.15)

    def draw(self,veld):
        veld.blit(pygame.transform.scale(self.char,(10,10)),
                  (positionlist[self.i]))

p1= player("p1",positionlist[0],'C:/player1.png',1000,0 )

p1money= 1000
