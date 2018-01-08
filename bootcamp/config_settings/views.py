# -*- coding: utf-8 -*-
from __future__ import unicode_literals, with_statement

from django.shortcuts import render
from bootcamp.settings import PROJECT_DIR
import re
import shutil
from tempfile import mkstemp
from bootcamp.config_settings.forms import ChangeSignupForm, ChangeMenuForm, EditBillForm
from .models import Bills

import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def sed(pattern, replace, source, dest=None, count=0):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    Args:
        pattern (str): pattern to match (can be re.pattern)
        replace (str): replacement str
        source  (str): input filename
        count (int): number of occurrences to replace
        dest (str):   destination filename, if not given, source will be over written.        
    """

    fin = open(source, 'r')
    num_replaced = count

    if dest:
        fout = open(dest, 'w')
    else:
        fd, name = mkstemp()
        fout = open(name, 'w')

    for line in fin:
        out = re.sub(pattern, replace, line)
        fout.write(out)

        if out != line:
            num_replaced += 1
        if count and num_replaced > count:
            break
    try:
        fout.writelines(fin.readlines())
    except Exception as E:
        raise E

    fin.close()
    fout.close()

    if not dest:
        shutil.move(name, source)

# Create your views here.
def config_settings(request):
	
	return render(request, 'config_settings/config_settings.html')

def change_signup(request):
	f=open(PROJECT_DIR+'/urls.py','r')
	s=f.readline()
	current_url=s.split("'")[1]
	f.close()
	form=ChangeSignupForm()
	if request.method=='GET':
		form=ChangeSignupForm()
	else:
		form=ChangeSignupForm(request.POST)
		if(form.is_valid()):
			new_url=form.cleaned_data["new_url"]
			f=open(PROJECT_DIR+'/urls.py','r')
			s=f.readline()
			try:
			    sed(s.split("'")[1], new_url, PROJECT_DIR+"/urls.py")
			except shutil.WindowsError:
			    print("[%] Changing Url")
		
	f=open(PROJECT_DIR+'/urls.py','r')
	s=f.readline()
	current_url=s.split("'")[1]
	f.close()
	return render(request, "config_settings/change_signup.html",{'form':form, 'current_url':current_url})

def change_menu(request):
	
	form=ChangeMenuForm()
	if request.method=='GET':
		form=ChangeMenuForm()
	else:
		form=ChangeMenuForm(request.POST)
		if(form.is_valid()):
			new_url=form.cleaned_data["new_url"]
			new_url=make_tiny(new_url)
			f=open(PROJECT_DIR+'/ticklist/templates/ticklist/ticklist.html','r')
			s=""
			while("<img" not in s):
				s=f.readline()
			print(s)
			print(s.split("'")[1])

			try:
				sed(s.split("'")[1], new_url, PROJECT_DIR+"/ticklist/templates/ticklist/ticklist.html")
				sed(s.split("'")[1], new_url, PROJECT_DIR + "/ticklist/templates/ticklist/edit.html")
				sed(s.split("'")[1], new_url, PROJECT_DIR + "/ticklist/templates/ticklist/editSelective.html")
			except shutil.WindowsError:
			    print("[%] Changing Url")
		return render(request, 'config_settings/config_settings.html')
	return render(request, 'config_settings/change_menu.html',{'form':form})

def reset_list(request):
	f=open(PROJECT_DIR+'/ticklist/data.json','w')
	f.write("{}")
	return render(request, 'config_settings/config_settings.html')

def edit_bill(request):
	form=EditBillForm()
	if request.method=='GET':
		form=EditBillForm()
	else:
		form=EditBillForm(request.POST)
		if(form.is_valid()):
			form_month=form.cleaned_data["month"]
			form_bill=form.cleaned_data["bill"]
			if Bills.objects.filter(month = form_month).exists():
				billobj=Bills.objects.get(month = form_month)
				billobj.bill=form_bill
				billobj.save()
			else:
				billobj=Bills.objects.create(month = form_month, bill= form_bill)
				billobj.save()
		show_bill(request)		
	return render(request, 'config_settings/edit_bill.html',{'form':form})

def show_bill(request):
	data=Bills.objects.all()
	mo=[["",""] for i in range(len(data))]
	if(len(data)!=0):
		for i in range(len(data)):
			print (data[i].month)
			a,b=data[i].month,data[i].bill
			mo[i][0]=a
			mo[i][1]=b

	return render(request, 'config_settings/show_bill.html', {'arr':mo})
