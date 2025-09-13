from django.shortcuts import render
from .models import Task
from django.db.models import Q

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(Q(name__icontains = search) | Q(description__icontains = search))

    context = {
        'tasks': tasks,
        'search': search,
    }

    return render(request, 'index.html', context)