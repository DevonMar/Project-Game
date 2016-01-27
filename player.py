import pygame,time

positionlist =[(698,695),(694,695),(630,695), (566,695),(503,695),(440,695),(375, 695),(312,695),(248,695),(187,695)
,(122, 775),(120, 690),(120, 625), (120, 561),(120,499),(120, 435),(120,430),(120,370),(120,307),(120, 245),(120,180),
(1,1),(125,0),(190,0),(250,0),(315,0),(380,0),(445,0),(508,0),(572,0),(635,0),(698,0),
(698,122),(698,186),(698,250),(698, 310),(698, 375),(698, 440),(698,503),(698,565),(698,630)]

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
