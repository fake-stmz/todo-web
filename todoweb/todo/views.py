from django.shortcuts import render
from .models import Task
from django.db.models import Q
from datetime import date

# Create your views here.
def index(request): # Обычная страница
    tasks = Task.objects.all() # Получение всех задач

    # Поиск
    search = request.GET.get('search', '')
    if search:
        tasks = tasks.filter(Q(name__icontains = search) | Q(description__icontains = search))

    # Контекст
    context = {
        'tasks': tasks,
        'search': search,
    }

    return render(request, 'index.html', context)

def advsrc(request): # Продвинутый поиск
    tasks = Task.objects.all() # Получение всех задач

    # Проверка фильтров / фильтрация
    name_search = request.GET.get('name', '')
    if name_search: tasks = tasks.filter(name__icontains=name_search)
    descr_search = request.GET.get('description', '')
    if descr_search: tasks = tasks.filter(description__icontains=descr_search)
    status_search = request.GET.get('status', '')
    if status_search: tasks = tasks.filter(status=status_search)
    creation_date_search = request.GET.get('creation_date', '')
    if creation_date_search: tasks = tasks.filter(creation_date=date.fromisoformat(creation_date_search))
    deadline_search = request.GET.get('deadline', '')
    if deadline_search: tasks = tasks.filter(deadline=date.fromisoformat(deadline_search))

    # Контекст
    context = {
        'tasks': tasks,
        'name': name_search,
        'description': descr_search,
        'status': status_search,
        'creation_date': creation_date_search,
        'deadline': deadline_search,
    }

    return render(request, 'search.html', context)
