# -*- coding:utf-8 -*-
import sys
import pygame

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption('biubiubiu~~~')
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		#���Ӽ��̺�����¼�
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		#��������Ƶ���Ļ�ɼ�
		pygame.display.flip()
		
run_game()