
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


# Create your views here.

@login_required
def person_list(request):
    termo_pesquisa = request.GET.get('pesquisa', None)

    if termo_pesquisa:
        persons = Person.objects.all()
        persons = persons.filter(first_name=termo_pesquisa)
    else:
        persons = Person.objects.all()

    return render(request, 'person.html', {'persons': persons})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    print(form)

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