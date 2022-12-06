import pygame
import sys


if __name__ == '__main__':
    pygame.init()
    width, height = list(map(int, input().split()))
    size = width, height
    screen = pygame.display.set_mode(size)
#    screen2 = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования выключен
    lasts = list()
    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # сохраняем нарисованное (на втором холсте)
#                screen2.blit(screen, (0, 0))
                lasts.append((x1, y1, w, h))
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
                a = True
            if event.type == pygame.MOUSEMOTION:
                # запоминаем текущие размеры
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if keys[pygame.K_z] and keys[pygame.K_LCTRL]:
                if lasts:
                    lasts.pop(-1)
##                    if lasts:
##                        screen2 = lasts[-1]
     #   # рисуем на экране сохранённое на втором холсте
        screen.fill('black')
#        screen.blit(screen2, (0, 0))
        for tmp in lasts:
            xt, yt, wt, ht = tmp
            pygame.draw.rect(screen, (0, 0, 255), ((xt, yt), (wt, ht)), 5)            
        if drawing:  # и, если надо, текущий прямоугольник
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
        #        lasts.append(screen2)
        print(lasts)
        pygame.display.flip()
