# _3mancap/views.py
from django.shortcuts import render
from .models import ActivityLog, Device, Incident, Event
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    activity_logs = ActivityLog.objects.all().order_by('-timestamp')[:10]
    devices_connected = Device.objects.filter(connected=True).count()
    incidents_to_review = Incident.objects.filter(resolved=False).count()
    events_recorded = Event.objects.count()

    context = {
        'activity_logs': activity_logs,
        'devices_connected': devices_connected,
        'incidents_to_review': incidents_to_review,
        'events_recorded': events_recorded,
    }
    return render(request, '_3mancap/dashboard.html')

class CustomLoginView(LoginView):
    template_name = '_3mancap/login.html'
    redirect_authenticated_user = True

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '_3mancap/register.html'
