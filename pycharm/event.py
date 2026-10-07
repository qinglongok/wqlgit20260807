import pygame
import sys

#初始化pygame
pygame.init()
size=width,height=600,400
win=pygame.display.set_mode(size)
pygame.display.set_caption('Qlok Homepage')
bg=('black')

font=pygame.font.SysFont('Arial',20)
line_height=font.get_linesize()
position=0
win.fill(bg) #将窗口颜色定义为bg

while True:
    for event in pygame.event.get(): #获取事件
        if event.type ==pygame.QUIT:
            sys.exit()
        win.blit(font.render(str(event),1,(0,255,0)),(0,position))
        position+=line_height
        if position>height:
           position=0
           win.fill(bg)
    pygame.display.flip()


