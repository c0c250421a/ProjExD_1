import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgf_img = pg.transform.flip(bg_img,True,False)#背景反転
    koukaton = pg.image.load("fig/3.png")#こうかとんSurfaceの作成
    koukaton = pg.transform.flip(koukaton,True,False)#左右反転
    koukaton_rect = koukaton.get_rect()#rectを取得
    koukaton_rect.center = 300,200#初期座標を設定
    tmr = 0
    k_x = 0
    k_y = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200#5,9
        k_x = 0
        k_y = 0

        screen.blit(bg_img, [-x, 0])#動かす
        screen.blit(bgf_img,[-(x)+1600,0])#もう一枚
        screen.blit(bg_img, [-x+3200, 0])#動かす2
        screen.blit(koukaton,koukaton_rect)#こうかとんを描画

        key_lst = pg.key.get_pressed()
        #課題1
        if key_lst[pg.K_UP]:
            k_y = -1
        if key_lst[pg.K_DOWN]:
            k_y = 1
        if key_lst[pg.K_LEFT]:
            k_x = -1
        if key_lst[pg.K_RIGHT]:
            k_x = 2
        koukaton_rect.move_ip((k_x-1, k_y))#課題2
        pg.display.update()
        tmr += 1    
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()