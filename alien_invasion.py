# -*- coding:utf-8 -*-
import sys
import pygame

from settings import Settings

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, \
	ai_settings.screen_height))
	pygame.display.set_caption('biubiubiu~~~')
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		#���Ӽ��̺�����¼�
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		#ÿ��ѭ��ʱ���ػ���Ļ
		screen.fill(ai_settings.bg_color)
				
		#��������Ƶ���Ļ�ɼ�
		pygame.display.flip()
		
run_game()
