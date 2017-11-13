from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from bootcamp.ticklist.forms import TickListForm
from bootcamp.ticklist.models import TickList

'''def ticklist(request):
    all_tick = TickList.meal_arr()
    return render(request, all_tick)'''

@login_required
def ticklist(request):
    ticklist=TickList.meal_arr
    return render(request, 'ticklist/ticklist.html', {'ticklist': ticklist})


'''class EditTickList(LoginRequiredMixin, UpdateView):
    template_name = 'ticklist/edit.html'
    model = TickList
    form_class = TickListForm
    success_url = reverse_lazy('ticklist')
'''
