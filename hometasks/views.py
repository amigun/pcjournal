from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AddTaskForm
from .models import HomeTask, Subjects, Files

from .schedule_parsing import get, get_date_by_weekday
from .to_pdf import generate


def ending(number):
    if number <= 0:
        return ''
    elif number == 1:
        return 'Контрольная работа на следующей паре'
    elif number % 10 == 2:
        return f'Контрольная работа через {number - 1} пару'
    elif number % 10 == 3:
        return f'Контрольная работа через {number - 1} пары'
    elif number % 10 == 4:
        return f'Контрольная работа через {number - 1} пары'
    elif number % 10 == 5:
        return f'Контрольная работа через {number - 1} пары'
    else:
        return f'Контрольная работа через {number - 1} пар'


def index(request):
    schedule = {}

    schedule_parse = get()

    for day_of_week in schedule_parse:
        subjects = {}

        for subject in schedule_parse[day_of_week][1]:
            try:
                tasks = {}

                for task in HomeTask.objects.filter(date=schedule_parse[day_of_week][0], subject=Subjects.objects.get(subject=subject).pk):
                    tasks[task.user.last_name] = [task.homework, ending(task.next_controlwork)]

                subjects[subject] = tasks
            except IndexError:
                pass

        schedule[day_of_week] = subjects

    docs = Files.objects.all()

    files = {}

    for doc in docs:
        files[doc.title] = doc.path[6:]

    return render(request, context={'title': 'Главная - pc.journal', 'schedule': schedule, 'files': files}, template_name='hometasks/index.html')


class AddTaskPage(LoginRequiredMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'hometasks/add_task.html'
    success_url = ''

    def form_valid(self, form):
        inst = form.instance
        inst.user = self.request.user
        inst.save()

        return HttpResponseRedirect(reverse_lazy('add_task'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить домашнее задание'

        return context


def save(request):
    date = get_date_by_weekday('Понедельник') if request.GET.get('date') is None else request.GET.get('date')

    schedule = []

    for day in range(6):
        ht = []
        for task in HomeTask.objects.filter(date=datetime.strptime(date, '%Y-%m-%d')+timedelta(days=day)):
            ht.append((Subjects.objects.filter(id=task.subject_id)[0], task.user.last_name, task.homework, ending(task.next_controlwork)))
            print(f'{datetime.strptime(date, "%Y-%m-%d")+timedelta(days=day)} {Subjects.objects.filter(id=task.subject_id)[0]}:\n\t{task.user.last_name=} {task.homework=} {ending(task.next_controlwork)=}')
        schedule.append((datetime.strptime(date, "%Y-%m-%d")+timedelta(days=day), ht))

    generate(date, schedule)

    return HttpResponse('Successful added!')


def download(request):
    return FileResponse(open('files/' + request.GET.get('file'), 'rb'))
