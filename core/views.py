from django.shortcuts import render
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'core/login.html'


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'core/home.html')

from .models import PlantedTree

@login_required
def my_trees(request):
    user = request.user
    planted_trees = PlantedTree.objects.filter(user=user)
    return render(request, 'core/my_trees.html', {'planted_trees': planted_trees})



