import pygame


# Color globals
CLR_WHITE = (255, 255, 255)
CLR_BLACK = (0, 0, 0)
CLR_BLUE = (0, 0, 255)
CLR_RED = (255, 0, 0)
CLR_PURPLE = (70, 1, 188)

class QuitOrStartPanel:
    """
    Displays an onscreen prompt to quit game or start over.
    """

    def __init__(self, screen, main):
        # Initialize resources
        self.main = main
        self.screen = screen
        self.rect = pygame.Rect(258, 212, 286, 178)
        self.color = CLR_PURPLE
        self.FONT1 = pygame.font.SysFont('comicsans', 52)
        self.FONT2 = pygame.font.SysFont('comicsans', 36)

#        self.background = GameObject({
#            'image': cfg.get_config_value('background', 'SCREEN'),
#            'xpos': 0,
#            'ypos': 0,
#            'iwidth': self.width,
#            'iheight': self.height
#            })
    # End: def AlienInvaders.__init__

    def show(self, player):
        text = self.FONT1.render('Game Over', True, CLR_RED)
        text2 = self.FONT2.render('(Q) to quit', True, CLR_WHITE)
        text3 = self.FONT2.render('(Spc) to Start', True, CLR_WHITE)

        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(text, (268, 211))
        self.screen.blit(text2, (306, 274))
        self.screen.blit(text3, (282, 318))

        start_game = False
        while True:
            quit_game, start_game = self.main._check_events(player, True)
            if start_game:
                self.main._reset(player)
            if start_game or quit_game:
                break
            else:
                self.main._update(self.main.CLOCK_RATE)
        return start_game
    # End: def QuitOrStartPanel._quit_or_start
