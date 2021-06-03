import pygame

pygame.init()


screen_width=800
screen_height=int(screen_width*0.8)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shooting Combat")

#including the  character:

A=250
B=250
scale=4
img=pygame.image.load("in .png")
img=pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
rect=img.get_rect()
rect.center = (A,B)

#including the loop:
run=True
while  run:

    screen.blit(img,rect)

    for event in pygame.event.get():
     if event.type==pygame.QUIT:
        run=False

    pygame.display.update()

pygame.quit()


























