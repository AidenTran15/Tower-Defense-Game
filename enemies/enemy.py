from re import X
from tkinter import Y
import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgs = []
        self.animation_count = 0 
        self.health = 1
        self.path = []

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        : return: None
        """
        pass

    def collide(self, x, y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        return False