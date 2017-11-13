from django import forms

from bootcamp.ticklist.models import TickList
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
import datetime
import calendar


class TickListForm(forms.ModelForm):
    dtnow=datetime.datetime.now()
    num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
    meal_choices=(('V','Veg'),('N','Non Veg'),('C','Cancel'))
    time_choices=(('d','Day'),('n','Night'),('b','Both'))
    start_date = forms.IntegerField(label="Starting Date ", required=True, validators=[MinValueValidator(dtnow.date),MaxValueValidator(num_days)])
    end_date = forms.IntegerField(label="Starting Date ", required=True, validators=[MinValueValidator(dtnow.date),MaxValueValidator(num_days)])
    meal_type=forms.ChoiceField(label="Type of meal", widget=forms.RadioSelect, choices=meal_choices,required='True')
    time_type=forms.ChoiceField(label="Enter meal times", widget=forms.RadioSelect, choices=time_choices,required='True')

    class Meta:
        model = TickList
        fields = ['start_date','end_date','meal_type','time_type']
