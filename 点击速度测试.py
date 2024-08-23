import pygame
import sys
import time
pygame.init()
times=1
screen=pygame.display.set_mode((600,400))
screen.fill((43,229,221))
while 1:
    event=pygame.event.wait()
    font=pygame.font.Font(None,50)
    text=font.render('click screen to start',1,(255,255,255),(43,229,221))
    if event.type==pygame.MOUSEBUTTONDOWN:
        break
    if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.blit(text,(150,200))    
    pygame.display.flip()
time1=pygame.time.get_ticks()
while 1:
    time2=pygame.time.get_ticks()
    myfont=pygame.font.Font(None,50)
    text=myfont.render(str(times),1,(255,255,255),(43,229,221))
    screen.fill((43,229,221))
    screen.blit(text,(300,200))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            times+=1
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if time2-time1>10000:
            text2=myfont.render('CPS:{0} clicks:{1}'.format(str(times/10),times),1,(255,255,255),(43,229,221))
            screen.fill((43,229,221))
            screen.blit(text2,(300,200))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    pygame.display.flip()


    
        
        
