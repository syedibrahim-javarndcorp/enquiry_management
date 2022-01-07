from django.shortcuts import render
from .models import Ems


# Create your views here.

def index(request):
    ems = Ems.objects.all()
    context = {'ems': ems}
    return render(request, 'ems/index.html', context)


def single_tag(request, pk):
    ems = Ems.objects.get(id=pk)
    tags = ems.tag.all()
    context = {
        "ems": ems,
        'tags': tags
    }
    return render(request, 'ems/profile_details.html', context)
