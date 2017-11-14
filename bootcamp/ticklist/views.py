from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from bootcamp.ticklist.forms import TickListForm, TickListSelectiveForm
from bootcamp.ticklist.models import TickList
from django.contrib.auth.models import User
import json
from pprint import pprint
import datetime
import calendar
from django.core.files import File

@login_required
def ticklist(request):
    data = json.load(open('bootcamp/ticklist/data.json'))
    username=str(request.user.username)
    ticklist=list()
    if username in data:
    	ticklist=data[username]
    else:
        dtnow=datetime.datetime.now()
    	num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
    	data[username]=['C']*(num_days)
        ticklist=data[username]
        with open('bootcamp/ticklist/data.json', 'w') as fp:
        	json.dump(data, fp)
    return render(request, 'ticklist/ticklist.html', {'ticklist': ticklist})


def edit(request):
    if request.method == 'GET':
        form = TickListForm()
    else:
	form=TickListForm(request.POST)
	if form.is_valid():
		start=form.cleaned_data["start_date"]
		end=form.cleaned_data["end_date"]
		meal=form.cleaned_data["meal_type"]
		time_type=form.cleaned_data.get("time_type")
		data = json.load(open('bootcamp/ticklist/data.json'))
		for i in range(start,end+1):
			data[str(request.user.username)][i-1]=meal
		print(data)
		with open('bootcamp/ticklist/data.json', 'w') as fp:
        		myfile=File(fp)
			json.dump(data, myfile)
		myfile.closed
		fp.closed
    	success_url = reverse_lazy('ticklist')
    	slug_field = 'ticklist_slug'
    	foo=1
	return render(request, 'ticklist/edit.html', {'form': form})
    return render(request, 'ticklist/edit.html', {'form': form})
   

def editSelective(request):
    if request.method == 'GET':
        form = TickListSelectiveForm()
    else:
	form=TickListSelectiveForm(request.POST)
	if form.is_valid():
		req_date=form.cleaned_data["req_date"]
		meal=form.cleaned_data["meal_type"]
		time_type=form.cleaned_data.get("time_type")
		data = json.load(open('bootcamp/ticklist/data.json'))
		data[str(request.user.username)][req_date-1]=meal
		with open('bootcamp/ticklist/data.json', 'w') as fp:
        		myfile=File(fp)
			json.dump(data, myfile)
		myfile.closed
		fp.closed
		
    	success_url = reverse_lazy('ticklist')
    	slug_field = 'ticklist_slug'
    	foo=1
	return render(request, 'ticklist/editSelective.html', {'form': form})
    return render(request, 'ticklist/editSelective.html', {'form': form})
   
