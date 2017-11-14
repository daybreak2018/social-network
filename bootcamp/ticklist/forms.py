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
    start_date = forms.IntegerField(label="Starting Date ", required=True)
    end_date = forms.IntegerField(label="Ending Date ", required=True)
    dmeal_type=forms.ChoiceField(label="Type of meal for day", widget=forms.RadioSelect, choices=meal_choices)
    nmeal_type=forms.ChoiceField(label="Type of meal for night", widget=forms.RadioSelect, choices=meal_choices)
    def clean(self):
        cleaned_data = super(TickListForm, self).clean()
        # do your custom validations / transformations here
        # and some more
        return cleaned_data
    class Meta:
        model = TickList
        fields = ['start_date','end_date','nmeal_type']


class TickListSelectiveForm(forms.ModelForm):
    dtnow=datetime.datetime.now()
    num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
    meal_choices=(('V','Veg'),('N','Non Veg'),('C','Cancel'))
    time_choices=(('d','Day'),('n','Night'),('b','Both'))
    req_date = forms.IntegerField(label="Required Date ", required=True)
    dmeal_type=forms.ChoiceField(label="Type of meal for day", widget=forms.RadioSelect, choices=meal_choices)
    nmeal_type=forms.ChoiceField(label="Type of meal for night", widget=forms.RadioSelect, choices=meal_choices)
    def clean(self):
        cleaned_data = super(TickListSelectiveForm, self).clean()
        # do your custom validations / transformations here
        # and some more
        return cleaned_data
    class Meta:
        model = TickList
        fields = ['req_date','dmeal_type','nmeal_type']

class ViewAllForm(forms.ModelForm):
    req_date = forms.IntegerField(label="Required Date ", required=True)
    time_choices=(('d','Day'),('n','Night'))
    time_type=forms.ChoiceField(label="Day/Night?", widget=forms.RadioSelect, choices=time_choices)
    def clean(self):
        cleaned_data = super(ViewAllForm, self).clean()
        # do your custom validations / transformations here
        # and some more
        return cleaned_data
    class Meta:
        model = TickList
        fields = ['req_date','time_type']


