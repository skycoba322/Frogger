#jarjekord: 1. ulejaanud takistusd + muru 1.5 vaadata, et kordub 2. Kaotamis funktsioon 3. alla liikumine

import random
import pygame
import os
import time
pygame.font.init()
laius = 700
korgus = 500
hele_roheline = (144, 238, 144)
valge = (255,255,255)
kollane = (255,255,0)
tmepunane = (255,3,62)
sinine = (0,0,255)
punane = (255,0,0)
hall = (220,220,220)
varvid = [punane, kollane, tmepunane, sinine]
screen = pygame.display.set_mode([laius, korgus])
pygame.display.set_caption('frogger')
#lopmatuse paneb kirja nii et kui mangija jouab ekraani otsa laheb teise ekraani peale
fps = 60
ava_pilt = pygame.image.load(os.path.join('pildid', 'ava.png'))
avamine = pygame.transform.scale(ava_pilt, (laius, korgus))
vesi_pilt = pygame.image.load(os.path.join('pildid', 'vesi.gif'))
vesi = pygame.transform.scale(vesi_pilt, (laius, 160))

vesi2_pilt = pygame.image.load(os.path.join('pildid', 'vesi2.png'))
vesi2 = pygame.transform.scale(vesi2_pilt, (laius, 160))

konna_pilt = pygame.image.load(os.path.join('pildid', 'konn.png'))
konn = pygame.transform.scale(konna_pilt, (40, 40))

tee_pilt = pygame.image.load(os.path.join('pildid', 'tee.png'))
tee = pygame.transform.scale(tee_pilt, (laius, 180))

auto_pilt = pygame.image.load(os.path.join('pildid', 'auto.png'))
auto = pygame.transform.scale(auto_pilt, (60, 80))
auto2_pilt = pygame.image.load(os.path.join('pildid', 'auto2.png'))
auto2 = pygame.transform.scale(auto2_pilt, (60, 80))

palk_pilt = pygame.image.load(os.path.join('pildid', 'plank.jpg'))
palk = pygame.transform.scale(palk_pilt, (70, 80))

palk2_pilt = pygame.image.load(os.path.join('pildid', 'plank.jpg'))
palk2 = pygame.transform.scale(palk2_pilt, (60, 80))

koera_pilt = pygame.image.load(os.path.join('pildid', 'koer.png'))
koer = pygame.transform.scale(koera_pilt, (50, 50))

koera2_pilt = pygame.image.load(os.path.join('pildid', 'koer.png'))
koer2 = pygame.transform.scale(koera2_pilt, (50, 50))

vesiroos_pilt = pygame.image.load(os.path.join('pildid', 'roos.png'))
vesiroos = pygame.transform.scale(vesiroos_pilt, (80, 80))

vesiroos2_pilt = pygame.image.load(os.path.join('pildid', 'roos.png'))
vesiroos2 = pygame.transform.scale(vesiroos_pilt, (80, 80))

font = pygame.font.SysFont(None, 50) 

kogus = 30
lilledx = []
lilledy = []
varvvalik = []
for i in range(kogus):
    lilledx.append(random.randint(0, 600))
    lilledy.append(random.randint(-400, 500))
    varvvalik.append(varvid[random.randint(0,3)])

teekorgus = -200
vesikorgus = 150
järvkõrgus = -550
VEL = 30

def joonistamine(konrut, jõgiR, järvR, autoR, teeR, plankR, auto2R, plank2R, kogus, koerR, koer2R, vesiroosR, vesiroos2R):
    screen.fill(hele_roheline)#ekraani varv alguses
    screen.blit(tee, (teeR.x, teeR.y))
    screen.blit(vesi, (jõgiR.x, jõgiR.y))
    screen.blit(vesi2, (järvR.x, järvR.y))
    screen.blit(vesiroos, (vesiroosR.x, vesiroosR.y))
    screen.blit(vesiroos2, (vesiroos2R.x, vesiroos2R.y))
    screen.blit(auto, (autoR.x,autoR.y))
    screen.blit(palk, (plankR.x, plankR.y))
    screen.blit(auto2, (auto2R.x, auto2R.y))
    screen.blit(palk, (plank2R.x, plank2R.y))
    screen.blit(koer, (koerR.x, koerR.y))
    screen.blit(koer2, (koer2R.x, koer2R.y))
    
    for i in range(kogus):
        lilleR = pygame.Rect(lilledx[i], lilledy[i], 10, 10)
        if lilleR.colliderect(jõgiR) or lilleR.colliderect(teeR) or lilleR.colliderect(järvR):
            lilledx[i] = 0 - (random.randint(10,650))
            lilledy[i] = 0 - (random.randint(0, 400)) 
        else:
            pygame.draw.rect(screen, varvvalik[i], pygame.Rect(lilledx[i], lilledy[i], 10, 10))
        if lilledy[i] > 500:
            lilledx[i] = (random.randint(100, 650))
            lilledy[i] = 0 - (random.randint(0, 400))
    screen.blit(koer, (koerR.x, koerR.y))
    screen.blit(koer2, (koer2R.x, koer2R.y))
    screen.blit(konn, (konrut.x, konrut.y))
    pygame.display.update()


def lilled(jõgiR, järvR, teeR, konrut):
    for i in range(kogus):
        lilleR = pygame.Rect(lilledx[i], lilledy[i], 10, 10)
        if lilleR.colliderect(jõgiR) or lilleR.colliderect(teeR) or lilleR.colliderect(järvR):
            lilledx[i] = 0 - (random.randint(-200, 700))
            lilledy[i] = 0 - (random.randint(0, 200)) 
        else:
            pygame.draw.rect(screen, varvvalik[i], pygame.Rect(lilledx[i], lilledy[i], 10, 10))
        if lilledy[i] > 500:
            lilledx[i] = (random.randint(0, 650))
            lilledy[i] = 0 - (random.randint(0, 400))
    screen.blit(konn, (konrut.x, konrut.y))
    pygame.display.update()

def sonum(sona, varv, kohtx, kohty):
    ekraani_text = font.render(sona, True, varv)
    screen.blit(ekraani_text, (laius/kohtx, korgus/kohty))


def algus():
    avamne = True
    while avamne:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#see osa utleb programmile kinni minna kui kasutaja sulgeb selle
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    avamne = False
        
        screen.fill((0,0,0))
        screen.blit(avamine, (-20, 110))
        sonum('Press k to begin', hele_roheline, 3.5, 3.5)
        pygame.display.update()
   
                
def lopp():
     loppemine = True
     while loppemine:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:#see osa utleb programmile kinni minna kui kasutaja sulgeb selle
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
         screen.fill((0,0,0))
         sonum('GAME OVER', punane,3,2.5)
         sonum('Press r to try again', valge,3.7, 1.7)
         sonum('Press q to quit', valge,3.2, 1.2)
         pygame.display.update()
    
    
def liikumine_ekraan(jõgiR, järvR, teeR, autoR, plankR, konrut, auto2R, plank2R, koerR, koer2R, lilledx, lilledy, vesiroosR, vesiroos2R):#Viib ekrranil olevaid objekte alla poole, et naeks valja nagu ekraan liiguks ules
    jõgiR.y += 20
    teeR.y += 20
    järvR.y += 20
    vesiroosR.y += 20
    vesiroos2R.y += 20
    autoR.y += 20
    plankR.y += 20
    konrut.y += 20
    plank2R.y += 20
    auto2R.y += 20
    koerR.y += 20
    koer2R.y += 20
    if jõgiR.y > 500:
        jõgiR.y, plankR.y, plank2R.y = -480, -480, -400
    if teeR.y > 500:
        teeR.y, autoR.y, auto2R.y = -480, -480, -400
    if järvR.y > 500:
        järvR.y, vesiroosR.y, vesiroos2R.y = -480, -480, -400
    if koerR.y > 500:
        koerR.y = jõgiR.y - 120
    if koer2R.y > 500:
        koer2R.y = teeR.y - 120
    for i in range(kogus):
        lilledy[i] = lilledy[i] + 20
        
    
def liikumine_objektid(autoR, plankR, konrut, auto2R, plank2R, koerR, koer2R, jõgiR):
    autoR.x -= 2
    auto2R.x += 5
    if autoR.x < -60:
        autoR.x = 700
    if auto2R.x > 700:
        auto2R.x = -60
    plankR.x += 4
    plank2R.x -= 2
    if plankR.x > 700:
        plankR.x = -60
    if plank2R.x < -60:
        plank2R.x = 700
    if konrut.colliderect(plankR):
        konrut.x += 4
    if konrut.colliderect(plank2R):
        konrut.x -= 2
    if konrut.x < 10:
        konrut.x = 10
    if konrut.x > 690:
        konrut.x = 690
    if konrut.y > 490:
        konrut.y = 490
    if koerR.x < 700:
        koerR.x += random.randint(-7,-3)
        koerR.y += random.randint(-3,3)
    if koerR.x < -50:
        koerR.x = 700
        
    if koerR.colliderect(jõgiR) == True or koerR.colliderect(autoR) == True or koerR.colliderect(auto2R) == True:
        koerR.x = 700
    
    if koer2R.x > -50:
        koer2R.x += random.randint(3,7)
        koer2R.y += random.randint(-3,3)
    if koer2R.x > 700:
        koer2R.x = -50
        
    if koer2R.colliderect(jõgiR) == True or koer2R.colliderect(autoR) == True or koer2R.colliderect(auto2R) == True:
        koer2R.x = -50

def surm(autoR, konrut, jõgiR, järvR, plankR, auto2R, plank2R, koerR, koer2R, vesiroosR, vesiroos2R):
    if konrut.colliderect(autoR) == True or konrut.colliderect(auto2R) == True:
        lopp()
    if konrut.colliderect(jõgiR) == True and konrut.colliderect(plankR) == False and konrut.colliderect(plank2R) == False:
        lopp()
    if konrut.colliderect(järvR) == True and konrut.colliderect(vesiroosR) == False and konrut.colliderect(vesiroos2R) == False:
        lopp()
    if konrut.colliderect(koerR) == True:
        lopp()
    if konrut.colliderect(koer2R) == True:
        lopp()
    

    
def liikummine_konn(event, konrut):
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    konrut.x -= VEL
                if event.key == pygame.K_RIGHT:
                    konrut.x += VEL
                if event.key == pygame.K_UP:
                    konrut.y -= VEL
                if event.key == pygame.K_DOWN:
                    konrut.y += VEL
  

def main(): #see funktsioon on peamine osa, siia hakkame kirjutama sisse koik ulejaanud funktsioone millest kokku
    algaeg = time.time()
    konrut = pygame.Rect(350,425, 20, 20)
    teeR = pygame.Rect(1, teekorgus, laius, 160)
    jõgiR = pygame.Rect(1, vesikorgus, laius, 160)
    järvR = pygame.Rect(1, järvkõrgus, laius, 160)
    vesiroosR = pygame.Rect(250, järvkõrgus, 80, 80)
    vesiroos2R = pygame.Rect(250, järvkõrgus + 80, 80, 80)
    autoR = pygame.Rect(600,teekorgus, 60, 80)
    plankR = pygame.Rect(-40,vesikorgus, 60, 80)
    auto2R = pygame.Rect(-40,teekorgus+80, 60, 80)
    plank2R = pygame.Rect(600,vesikorgus+80, 60, 80)
    koerR = pygame.Rect(700, jõgiR.y - 120, 50, 50)
    koer2R = pygame.Rect(-50, teeR.y - 120, 50, 50)
    
   
    clock = pygame.time.Clock()        #tekib meie mang
    running = True
    
    
    
    while running:
        clock.tick(fps)
           
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#see osa utleb programmile kinni minna kui kasutaja sulgeb selle
                running = False
        
            liikummine_konn(event, konrut)
            
            
        #koera tekkimise juhuslikkus
        if koerR.x == 700:
            koer_juhuslik = random.randint(1,500)
            
            if koer_juhuslik == 1:
                koerR.x -= 1
                
        if koer2R.x == -50:
            koer2_juhuslik = random.randint(1,500)
            
            if koer2_juhuslik == 1:
                koer2R.x += 1
                
        if järvR.y == -550 or järvR.y == -480:
             x = random.randint(0, laius-80)
             
             vesiroosR.x = x
             vesiroos2R.x = x
        
        
        joonistamine(konrut, jõgiR, järvR, autoR, teeR, plankR, auto2R, plank2R, kogus, koerR, koer2R, vesiroosR, vesiroos2R)
        
        
        liikumine_objektid(autoR, plankR, konrut, auto2R, plank2R, koerR, koer2R, jõgiR)
        
        surm(autoR, konrut, jõgiR, järvR, plankR, auto2R, plank2R, koerR, koer2R, vesiroosR, vesiroos2R)
        
        if time.time() - algaeg > 0.4:#eraldi liigutab iga sekund ekraani allapoole ilma, et segaks mangija liigutusi
            algaeg = time.time()
            liikumine_ekraan(jõgiR, järvR, teeR, autoR, plankR, konrut, auto2R, plank2R, koerR, koer2R, lilledx, lilledy, vesiroosR, vesiroos2R)
       
        
        
    pygame.quit()
algus()
main()
