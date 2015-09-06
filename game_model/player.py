__author__ = 'tri'
from utils.observer_pattern.observer import Observer
from utils.customer_waiter_pattern.customer import Customer
from game_model.hammer import Hammer
from game_model.drawable import Drawable

import pygame


class Player(Observer, Customer):

    def __init__(self, event_controller, waiter):

        # Constructor of base class
        Observer.__init__(self, event_controller)
        Customer.__init__(self, waiter)

        # Register to receive mouse event: Mouse click and motion
        self.register_mouse_down()
        self.register_mouse_motion()

        # Attributes

        # hammer
        self.hammer = Hammer(waiter)

    def update(self, event):
        """
        Handler mouse click
        :param event: Mouse click event and mouse motion
        :return: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.hammer.hit(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            # Just draw the one avatar in list avatars of hammer
            drawable_object = Drawable(self.hammer.get_avatar(), event.pos, 2)
            self.register('2_hammer', drawable_object)
