# -*- coding:utf-8 -*-
import sys
import pygame

def check_events():
	#��Ӧ����������¼�
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
			
def update_screen(ai_settings, screen, ship):
	#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
	#ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_settings.bg_color)
	ship.blitme()
				
	#��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
