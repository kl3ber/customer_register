
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Person, Py_Log_mssql
from .forms import PersonForm
from datetime import date as dt

# Create your views here.

@login_required
def person_list(request):
    nome = request.GET.get('pesquisa_nome', None)
    sobrenome = request.GET.get('pesquisa_sobrenome', None)
    checkbox = request.GET.get('meu-checkbox', None)

    persons = Person.objects.all()

    if checkbox == 'on':
        persons = persons.filter(doc__isnull=True)

    if nome:        persons = persons.filter(Q(first_name__icontains=nome))
    if sobrenome:   persons = persons.filter(Q(last_name__icontains=sobrenome))

    return render(request, 'person.html', {'persons': persons})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


def dw_log_atualizacao(request):
    logs = Py_Log_mssql.objects.filter(pylog_datetime__date=dt.today()).order_by('-pylog_datetime')
    n = logs.count()

    return render(request, 'logs.html', {'logs': logs, 'n': n})