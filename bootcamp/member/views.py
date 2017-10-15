# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from bootcamp.decorators import ajax_required
from django.shortcuts import get_object_or_404
@login_required
def member(request,username):
	page_user = get_object_or_404(User, username=username)
	data = {
        'page_user': page_user,
        }
	return render(request, 'member/member.html', data)