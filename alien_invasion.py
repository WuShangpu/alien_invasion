# -*- coding:utf-8 -*-
import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, \
	ai_settings.screen_height))
	pygame.display.set_caption('biubiubiu~~~')
	
	#����һ�ҷɴ�
	ship = Ship(ai_settings, screen)
	
	#��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		

run_game()
