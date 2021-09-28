from django.shortcuts import render, redirect
from core.models import Event
# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def events_list(request):
    event = Event.objects.all()
    data = {'events':event}
    return render(request, 'agenda.html', data)
