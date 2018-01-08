from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.shortcuts import render
from bootcamp.ticklist.forms import TickListForm, TickListSelectiveForm, ViewAllForm
from bootcamp.ticklist.models import TickList
from django.contrib.auth.models import User
import json
from pprint import pprint
import datetime
import calendar
from django.core.files import File

dtnow=datetime.datetime.now()
num_days=calendar.monthrange(dtnow.year,dtnow.month)[1]
days = [datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, day).ctime().strip() for day in range(1, num_days+1)]
for i in range(num_days):
	day=days[i].split()
	days[i]=day[0]+": "+day[2]+"-"+day[1]+"-"+day[4]

@login_required
def ticklist(request):
    
    data = json.load(open('bootcamp/ticklist/data.json'))
    username=str(request.user.username)
    ticklist=list()

    viewAll(request)
    if username in data:
    	ticklist=data[username]
    else:
        data[username]=[[days[i],'C','C'] for i in range(num_days)]
        ticklist=data[username]
        with open('bootcamp/ticklist/data.json', 'w') as fp:
            json.dump(data, fp)

    return render(request, 'ticklist/ticklist.html', {'ticklist': ticklist,'today':ticklist[dtnow.day-1]})


def edit(request):
    if request.method == 'GET':
        form = TickListForm()
    else:
        form=TickListForm(request.POST)
        if form.is_valid():
            start=form.cleaned_data["start_date"]
            end=form.cleaned_data["end_date"]
            dmeal=form.cleaned_data["dmeal_type"]
            nmeal=form.cleaned_data["nmeal_type"]
            data = json.load(open('bootcamp/ticklist/data.json'))
            for i in range(start,end+1):
                data[str(request.user.username)][i-1]=[days[i-1],dmeal,nmeal]
            print(data)
            with open('bootcamp/ticklist/data.json', 'w') as fp:
                myfile=File(fp)
                json.dump(data, myfile)
            myfile.closed
            fp.closed
        success_url = reverse_lazy('ticklist')
        slug_field = 'ticklist_slug'
        foo=1
    return render(request, 'ticklist/edit.html', {'form': form,})
   

def editSelective(request):
    if request.method == 'GET':
        form = TickListSelectiveForm()
    else:
        form=TickListSelectiveForm(request.POST)
        if form.is_valid():
            req_date=form.cleaned_data["req_date"]
            dmeal=form.cleaned_data["dmeal_type"]
            nmeal=form.cleaned_data["nmeal_type"]
            time_type=form.cleaned_data.get("time_type")
            data = json.load(open('bootcamp/ticklist/data.json'))
            data[str(request.user.username)][req_date-1]=[days[req_date-1],dmeal,nmeal]
            with open('bootcamp/ticklist/data.json', 'w') as fp:
                myfile=File(fp)
                json.dump(data, myfile)
            myfile.closed
            fp.closed
        success_url = reverse_lazy('ticklist')
        slug_field = 'ticklist_slug'
        foo=1
        return render(request, 'ticklist/editSelective.html', {'form': form})
    return render(request, 'ticklist/editSelective.html', {'form': form, })

def viewAll(request):
    if request.method == 'GET':
        form = ViewAllForm()
    else:
        form=ViewAllForm(request.POST)
        users_list = User.objects.filter(is_active=True).order_by('username')
        if form.is_valid():
            req_date=form.cleaned_data["req_date"]
            time_type=form.cleaned_data["time_type"]
            data = json.load(open('bootcamp/ticklist/data.json'))
            Nmeal=list()
            Vmeal=list()
            if(time_type=='d'):
                for d in data:
                    if(data[d][dtnow.day-1][1]=='N'):
                        for user in users_list:
                            if str(user.username)==d:
                                Nmeal.append(user)
                                break
                    elif(data[d][dtnow.day-1][1]=='V'):
                        for user in users_list:
                            if str(user.username)==d:
                                Vmeal.append(user)
                                break
                nl=len(Nmeal)
                vl=len(Vmeal)
                return render(request, 'ticklist/viewAll.html', {'Nmeal': Nmeal,'Vmeal':Vmeal,'nl': nl,'vl':vl})
            elif(time_type=='n'):
                for d in data:
                    if(data[d][dtnow.day-1][2]=='N'):
                        for user in users_list:
                            if str(user.username)==d:
                                Nmeal.append(user)
                                break
                    elif(data[d][dtnow.day-1][2]=='V'):
                        for user in users_list:
                            if str(user.username)==d:
                                Vmeal.append(user)
                                break
                nl=len(Nmeal)
                vl=len(Vmeal)
                return render(request, 'ticklist/viewAll.html', {'Nmeal': Nmeal,'Vmeal':Vmeal,'nl': nl,'vl':vl })
    return render(request, 'ticklist/viewAllEdit.html', {'form': form})



