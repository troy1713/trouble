#!/usr/bin/env python

# Player colors will be
# red (153, 0, 48)
# blue (47, 54, 153)
# green (6, 82, 28)
# yellow (196, 146, 8)


import pygame as pg

#class Player(place):
#    def __init__(self):
        


def main():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((1280,720), pg.SCALED)
    img = pg.image.load_extended("board.png")
    pg.display.set_caption("Trouble")
    
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))
    
    font64 = pg.font.Font(None, 64)
    font32 = pg.font.Font(None, 32)
    welcome_msg = font64.render("Welcome to Trouble!", True, (0, 0, 0))
    welcome_msg_pos = welcome_msg.get_rect(centerx = screen.get_width()/2, y = 10)
    background.blit(welcome_msg, welcome_msg_pos)
    
    chs_color = font32.render("Choose your color:", True, (0, 0, 0))
    chs_color_pos = chs_color.get_rect(centerx = 1100, y = 200)
    background.blit(chs_color, chs_color_pos)
    
    # Our red is (237, 28, 35)
    # blue is (77, 110, 243)
    # green is (34, 177, 77)
    # yellow is (255, 242, 0)
    
    # Inside (secondary colors are)
    # red (247, 104, 104)
    # blue (153, 217, 234)
    # green (212, 249, 188)
    # yellow (245, 229, 156)
    chs_red = pg.draw.rect(background, (237, 28, 35), (950, 270, 100, 40))
    chs_blue = pg.draw.rect(background, (77, 110, 243), (1100, 270, 100, 40))
    screen.blit(background, chs_red)
    
    
    screen.blit(background, (0, 0))

    while True:
        # Process player inputs.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

        # Do logical updates here.
        # ...

        screen.blit(img, (400, 150))

        # Render the graphics here.
        # ...

        pg.display.flip()  # Refresh on-screen display
        clock.tick(60)

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()