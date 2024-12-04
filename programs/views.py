from django.shortcuts import render, redirect
from .models import ProgrammingLanguage


def programs_list(request):
    programs = ProgrammingLanguage.objects.all()
    ctx = {'programs': programs}
    return render(request, 'programs/programs-list.html', ctx)

def program_create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if title and description:
        ProgrammingLanguage.objects.create(
            title = title,
            description = description
        )
        return redirect('programs:list')
    return render(request, 'programs/program-create.html')