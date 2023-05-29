from django.shortcuts import render


def home(request):
    return render(request, 'test_app/home.html')


def search_events(request):
    return render(request, 'test_app/search_events.html')


def browse_events(request):
    return render(request, 'test_app/browse_events.html')


def event_info(request):
    return render(request, 'test_app/event_info.html')