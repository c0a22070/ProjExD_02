import random
import sys

import pygame as pg

delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }

def i_kk_imgs():  # 追加機能１未完 
    kk_img = pg.image0.load("ex02/fig/3.png")  # 追加機能１未完 
    kk_img0 = pg.transform.rotozoom(kk_img, 0, 2.0)  # 追加機能１未完 
    return{
            (0, -1): pg.transform.rotozoom(kk_img, 270, 1.0),   # 追加機能１未完 
            (+1, -1): pg.transform.rotozoom(kk_img, 315, 1.0), # 追加機能１未完 
            (+1, 0): pg.transform.rotozoom(kk_img, 0, 1.0),  # 追加機能１未完 
            (+1, +1): pg.transform.rotozoom(kk_img, 45, 1.0),  # 追加機能１未完 
            (0, +1): pg.transform.rotozoom(kk_img, 90, 1.0),  # 追加機能１未完 
            (-1, +1): pg.transform.rotozoom(kk_img, 135, 1.0),  # 追加機能１未完 
            (-1, 0): pg.transform.rotozoom(kk_img, 180, 1.0),  # 追加機能１未完 
            (-1, -1): pg.transform.rotozoom(kk_img, 225, 1.0),  # 追加機能１未完 
            }

def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面買いを判定し、真理値タプルを返す関数
    引数1：画面SurfaceのRect
    引数2：こうかとんまたは爆弾SurfaceのRect
    返り値：横方向、縦方向のはみ出し判定結果(画面内：True 画面外：False)
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = kk_img0  # 追加機能１未完 
    kk_img = init_kk_imgs[+1, 0]  # 追加機能１未完 
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bb_img = pg.Surface((20, 20))  # 練習1
    pg.draw.circle(bb_img,(255, 0, 0), (10, 10) , 10)  # 練習1
    bb_img.set_colorkey((0, 0, 0))  # 練習1
    x, y=random.randint(0, 1600), random.randint(0, 900)  # 練習2
    screen.blit(bb_img, [x, y])
    vx, vy = +1 ,+1
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y

    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        for l, nv in kk_kai.items():
            if key_lst[l]:
                bb_rct.move_ip(nv)

        if check_bound(screen.get_rect(),kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])  

        if main[0] == 0

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:  # 横方向にはみ出ていたら
            vx *= -1
        if not tate:  # 縦方向にはみ出ていたら
            vy *= -1
        screen.blit(bb_img, bb_rct)
        if kk_rct.colliderect(bb_rct):
            return #練習６
        pg.display.update()
        clock.tick(1000)
"""     for r in range(1,11):
            bb_img = pg.Surface((20*r, 20*r))
            pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
            bb_imgs.append(bb_img)
"""
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()