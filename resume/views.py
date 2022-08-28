from django.shortcuts import render
from .models import Experiance, Projects, Intern


# Create your views here.
def index(request):

    exps = Experiance.objects.all()
    pros = Projects.objects.all()
    intr = Intern.objects.all()
    contact = None
    meta = {'exps': exps, 'pros': pros, 'intr': intr, 'cont': contact}
    return render(request, "index.html", meta)
