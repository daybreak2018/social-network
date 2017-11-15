# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def config_settings(request):
	return render(request, 'config_settings/config_settings.html')

def change_signup(request):
	return render(request, 'config_settings/config_settings.html')

def upload_menu(request):
	return render(request, 'config_settings/config_settings.html')

def reset_list(request):
	return render(request, 'config_settings/config_settings.html')
