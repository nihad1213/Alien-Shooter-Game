#This file contain settings
import pygame

class Settings:
    def __init__(self):
        #Settings of screen part
        self.screen_width = 800
        self.screen_height = 600
        #Background color
        self.bg_color = (3, 0, 53)
        #Speed of Player
        self.player_speed = 2
        #Bullet Settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

