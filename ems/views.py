from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ems
from .forms import EmsForm


# Create your views here.

def index(request):
    ems = Ems.objects.all()
    context = {'ems': ems}
    return render(request, 'ems/index.html', context)


@login_required(login_url='login')
def single_tag(request, pk):
    ems = Ems.objects.get(id=pk)
    tags = ems.tag.all()
    context = {
        "ems": ems,
        'tags': tags
    }
    return render(request, 'ems/profile_details.html', context)


@login_required(login_url='login')
def create_enquiry(request):
    form = EmsForm()

    if request.method == 'POST':
        form = EmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'ems/add-update.html', context)


@login_required(login_url='login')
def update_enquiry(request, pk):
    enquiry = Ems.objects.get(id=pk)
    form = EmsForm(instance=enquiry)

    if request.method == 'POST':
        form = EmsForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'ems/add-update.html', context)


@login_required(login_url='login')
def delete_enquiry(request, pk):
    enquiry = Ems.objects.get(id=pk)
    if request.method == "POST":
        enquiry.delete()
        return redirect('index')

    context = {
        'enquiry': enquiry
    }
    return render(request, 'ems/delete.html', context)
