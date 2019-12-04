"""
Modified by Kim MinGyu
Last Modification : 2019.12.04.
"""

import os
import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 60 # desired framerate in frames per second. try out other values !
KEYBOARDX = 5   # Top left of the full keyboard
KEYBOARDY = 5   # Top left of the full keyboard
KEYBETWEEN = 0  # distance between the key
KEY_HEIGHT = 0 # height of white key (useful for put the text at the right distance
with open('computer_typewriter.kb', 'r') as f:
    KEY_ASCII = f.read().split('\n')
IS_PLAYING = {k: False for k in KEY_ASCII}


class Key(pygame.sprite.Sprite):
    keyobj_list = []

    def __init__(self, name, keyevent):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.color = self.name.split('_')[1]
        self.image = pygame.image.load(os.path.join('pythonpiano_pictures', self.name + '_unpressed.png'))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()  # need to be defined for the group updates!
        self.width = self.image.get_width()
        self.keyevent = keyevent  # name of the key returned by 'pygame.event.scancode' = Key code number
        self.pressed = False
        Key.keyobj_list.append(self)
        self.rect.x = 0  # temporary, the position of the key is '0'
        self.rect.y = KEYBOARDY
        self._layer = 0  # the order with which the key is drawn
        # Preloading of the key picture for faster load
        self._img_down = pygame.image.load(os.path.join('pythonpiano_pictures', self.name + '_pressed.png'))
        self._img_up = pygame.image.load(os.path.join('pythonpiano_pictures', self.name + '_unpressed.png'))

    def update(self):
        if self.pressed:
            self.image = self._img_down
        #             print("the key {} is being pressed".format(self.keyevent))
        else:
            self.image = self._img_up


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 250))  # set screensize of pygame window
        self.background = pygame.Surface(self.screen.get_size())  # create empty pygame surface
        self.background.fill((255, 255, 255))
        key_octave = ['key_white_Left', 'key_black', 'key_white_Middle', 'key_black',
                      'key_white_Right', 'key_white_Left', 'key_black', 'key_white_Middle', 'key_black', \
                      'key_white_Middle', 'key_black', 'key_white_Right']
        keyevent_idx = 0  # each key must have a reference to the keyboard ascii with their correct position:
        keyboardx_position = KEYBOARDX
        # assign groups for the Sprite:
        self.keysprites = pygame.sprite.LayeredUpdates()

        for i in range(4):
            for idx, key in enumerate(key_octave):
                key_obj = Key(key, KEY_ASCII[keyevent_idx])
                keyevent_idx += 1
                # Draw the keys:
                if key_obj.color == 'white':
                    key_obj.rect.x = keyboardx_position
                    keyboardx_position += key_obj.width + KEYBETWEEN
                elif key_obj.color == 'black':
                    key_obj.rect.x = keyboardx_position - key_obj.width / 4
                    key_obj._layer = 1  # move it to the front position (the bigger the number

                self.background.blit(key_obj.image, key_obj.rect)
                self.keysprites.add(key_obj)  # add the key sprite to the group

        self.screen.blit(self.background, (0, 0))  # draw the background on screen
        pygame.display.flip()  # then flip it

    def run(self):
        print("Starting Event loop")
        running = True

        while running:
            # handle pygame events -- if user closes game, stop running
            running = self.handlerEvents()

            # update our sprites
            for keysprite in self.keysprites:
                keysprite.update()

            # render our sprites
            self.keysprites.clear(self.screen,
                                  self.background)  # clear the window where the sprites currently are, using the background
            dirty = self.keysprites.draw(self.screen)  # calculates the 'dirty' rectangles that need to be redrawn

            # blit the dirty areas of the screen
            pygame.display.update(dirty)  # updates just the 'dirty' areas

        print("Good Bye!")
        sys.exit()

    def handlerEvents(self):
        # Event checker:
        for event in pygame.event.get():
            if event.type in (KEYDOWN, KEYUP):
                key = str(event.scancode)

            if event.type == QUIT:
                return False  # pygame window closed by user

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False  # user pressed ESC

                IS_PLAYING[key] = True
                for keyobj in Key.keyobj_list:
                    if keyobj.keyevent == key:
                        keyobj.pressed = True

            elif event.type == KEYUP:
                IS_PLAYING[key] = False
                for keyobj in Key.keyobj_list:
                    if keyobj.keyevent == key:
                        keyobj.pressed = False
        return True


if __name__ == "__main__":
    game = Game()
    game.run()
