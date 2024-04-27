from django.shortcuts import render
from apps.base.models import Settings,Rewards,Works,Experience,ExpModel,Journal,Research,Latest
# Create your views here.

def index(request):
    settings = Settings.objects.latest("id")
    rewards = Rewards.objects.all()
    works = Works.objects.all()
    experience = Experience.objects.latest("id")
    exp = ExpModel.objects.all()
    journal = Journal.objects.all()
    research = Research.objects.all()
    latest = Latest.objects.all()
    return render(request, "index.html",locals())
