from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'coffee/main.html', context)


def staff(request):
    context = {
        'title': 'Список сотрудников'
    }
    return render(request, 'coffee/staff.html', context)


def employer_of_the_month(request):
    context = {
        'title': 'Сотрудник месяца'
    }
    return render(request, 'coffee/empofthemonth.html', context)


def add_employer(request):
    context = {
        'title': 'Добавить сотрудника'
    }
    return render(request, 'coffee/addemploy.html', context)