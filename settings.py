# -*- coding:utf-8 -*-
class Settings():
	#�洢��biubiubiu~~~�����������õ���
	
	def __init__(self):
		#��ʼ����Ϸ����
		#��Ļ����
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (137, 207, 240)
		
		#�ɴ�������
		self.ship_speed_factor = 1.5
		
		#�ӵ�����
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		#����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_directionΪ1��ʾ�����ƶ���Ϊ-1��ʾ������
		self.fleet_direction = 1
		
