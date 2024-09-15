from django.shortcuts import render

# Create your views here.
# _3mancap/views.py

from django.shortcuts import render
from .models import ActivityLog, Device, Incident, Event

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
    return render(request, '_3mancap/dashboard.html', context)
