from django.shortcuts import render, get_object_or_404

from home.models import Event
from blog.models import Entry

# Create your views here.


def home_display(request):
    entries = Entry.get_top_three_entries()
    events = Event.get_events()
    entries_length = len(entries)
    events_length = len(events)

    return render(request,
                  'home/home_display.html',
                  {'events': events,
                   'entries': entries,
                   'entries_length': entries_length,
                   'events_length': events_length
                   }
                  )


def event_display(request, slug):
    event = get_object_or_404(Event, slug=slug)

    return render(request, 'home/event_display.html', {'event': event})
