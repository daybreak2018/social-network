from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
import datetime
import calendar

class TickList(models.Model):
    dtnow=datetime.datetime.now()
    num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
    meal_choices=(('V','Veg'),('N','Non Veg'),('C','Cancel'))
    time_choices=(('d','Day'),('n','Night'),('b','Both'))
    start_date = models.IntegerField(validators=[
            MaxValueValidator(num_days),
            MinValueValidator(dtnow)
        ])
    end_date = models.IntegerField(validators=[
            MaxValueValidator(num_days),
            MinValueValidator(start_date)
        ])
    meal_type = models.CharField(max_length=1)
    time_type = models.CharField(max_length=1)
    mess_user = models.ForeignKey(User)
    meal_arr=[[i,'c'] for i in range(1,num_days+1)]

    

