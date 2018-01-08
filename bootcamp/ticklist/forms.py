from django import forms

from bootcamp.ticklist.models import TickList
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
import datetime
import calendar
dtnow=datetime.datetime.now()
num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
meal_choices=(('V','Veg'),('N','Non Veg'),('C','Cancel'))

class TickListForm(forms.ModelForm):
    
    start_date = forms.IntegerField(label="Starting Date ", required=True)
    end_date = forms.IntegerField(label="Ending Date ", required=True)
    dmeal_type=forms.ChoiceField(label="Type of meal for day", widget=forms.RadioSelect, choices=meal_choices)
    nmeal_type=forms.ChoiceField(label="Type of meal for night", widget=forms.RadioSelect, choices=meal_choices)
    def clean(self):
        cleaned_data = super(TickListForm, self).clean()
        if self.cleaned_data.get('start_date')<dtnow.day:
            self._errors['start_date'] = self.error_class(['Start date cannot be lesser than today.'])
        if not self.cleaned_data.get('start_date')<=self.cleaned_data.get('end_date') <=num_days+1:
            self._errors['end_date'] = self.error_class(['Invalid end date'])
        # and some more
        return cleaned_data
    class Meta:
        model = TickList
        fields = ['start_date','end_date','dmeal_type','nmeal_type']


class TickListSelectiveForm(forms.ModelForm):
    req_date = forms.IntegerField(label="Required Date ", required=True)
    dmeal_type=forms.ChoiceField(label="Type of meal for day", widget=forms.RadioSelect, choices=meal_choices)
    nmeal_type=forms.ChoiceField(label="Type of meal for night", widget=forms.RadioSelect, choices=meal_choices)
    def clean(self):
        cleaned_data = super(TickListSelectiveForm, self).clean()
        # do your custom validations / transformations here
        if dtnow.day>self.cleaned_data.get('req_date') or  self.cleaned_data.get('req_date')>num_days+1:
            self._errors['req_date'] = self.error_class(['Invalid date'])
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


