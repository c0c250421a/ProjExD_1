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
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200#5,9
        screen.blit(bg_img, [-x, 0])#動かす
        screen.blit(bgf_img,[-(x)+1600,0])#もう一枚
        screen.blit(bg_img, [-x+3200, 0])#動かす2
        screen.blit(koukaton,koukaton_rect)#こうかとんを描画
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            koukaton_rect.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            koukaton_rect.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            koukaton_rect.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            koukaton_rect.move_ip((1, 0))
        pg.display.update()
        tmr += 1    
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()