from django.shortcuts import render
from .models import Dish
from django.http import HttpResponse

# Create your views here.
def menu_view(request):
    # Fetching all items from the "Pantry"
    all_dishes = Dish.objects.all()
    
    # Handling the data to the "Plating Station"
    return render(request,  'menu.html', {'menu_items': all_dishes})

def home(request):
    bistro = "<h1>My Cool Bistro</h1>"
    return HttpResponse(bistro)