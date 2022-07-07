from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import ProjectForm, ProjectFormSet
from next_prev import next_in_order, prev_in_order
from .models import Project, ProjectDetail, ProjectImages, Partner, Contact, Directie, SiteContent
import math

site_content = SiteContent.objects.all()


def new_project_form(request):
    if request.method == "POST":
        form = ProjectFormSet(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projecten')
    else:
        form = ProjectFormSet
    return render(request, 'admin/new_project_form.html', {'form': form})


def new_project(request):
    return render(request, 'admin/new_project.html', {})
    # return HttpResponse("Hello")


# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html', {'site_content': site_content})


def organisatie(request):
    return render(request, 'portfolio/organisatie.html', {'site_content': site_content})


def directie(request):
    directie = Directie.objects.all()
    return render(request, 'portfolio/directie.html', {'directie': directie, 'site_content': site_content})


def projecten(request):
    projects = Project.objects.filter(published=True).order_by('order_id')
    return render(request, 'portfolio/projecten.html', {'projects': projects, 'site_content': site_content})


def projecten_details(request, project_url):
    projects = Project.objects.filter(url=project_url)
    project_details = ProjectDetail.objects.filter(project=projects)
    project_images = ProjectImages.objects.filter(project=projects).order_by('order_id')

    qs = Project.objects.all().order_by('order_id')
    current = Project.objects.get(url=project_url)
    next = next_in_order(current, qs=qs)
    prev = prev_in_order(current, qs=qs)

    return render(request, 'portfolio/projecten_details.html', {'projects': projects,
                                                                'project_details': project_details,
                                                                'project_images': project_images,
                                                                'site_content': site_content,
                                                                'next': next,
                                                                'prev': prev
                                                                }
                                                                )


def investeren(request):
    return render(request, 'portfolio/investeren.html', {'site_content': site_content})


def contact(request):
    contact = Contact.objects.all()
    return render(request, 'portfolio/contact.html', {'contact': contact, 'site_content': site_content})


def disclaimer(request):
    return render(request, 'portfolio/disclaimer.html', {})

