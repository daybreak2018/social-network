# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bills(models.Model):
	month = models.CharField(max_length = 20)
	bill = models.CharField(max_length=10)
	
	def __unicode__(self):
        	return self.month+":"+self.bill
		
	class Meta:
		db_table = "bill"

