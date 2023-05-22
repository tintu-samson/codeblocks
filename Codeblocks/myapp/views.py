from django.shortcuts import render
from .models import Domain,Events
# Create your views here.

def index(request):
    domain = Domain.objects.all()
    events = Events.objects.all()
    context = {'domain':domain,'events':events}
    return render(request,"myapp/index.html",context)