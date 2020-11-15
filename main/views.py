from django.shortcuts import render
from .models import Region, Measure

def home(request):
    regions = Region.objects.all()
    for region in regions:
        region.items = Measure.objects.filter(region=region.id)
    return render(request, 'main/home.html', { 'regions': regions })
