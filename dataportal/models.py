# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):

	p_id = models.IntegerField()
	p_description = models.TextField(
		max_length = 1024,
		blank = True,
		null = True)
	p_datetime = models.DateTimeField(
		db_index = True,
		)
	p_longitude = models.DecimalField(
		max_digits = 15,
		decimal_places =10
		)
	p_latitude = models.DecimalField(
		max_digits = 15,
		decimal_places = 10)
	p_elevation = models.IntegerField()

class Meta:
	verbose_name_plural = 'products'

def __unicode__(self):
	return 'Product: %s %s ' % (str(self.p_id),str(self.p_datetime))		
