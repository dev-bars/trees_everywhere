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

from django.shortcuts import get_object_or_404

@login_required
def planted_tree_detail(request, pk):
    tree = get_object_or_404(PlantedTree, pk=pk, user=request.user)
    return render(request, 'core/planted_tree_detail.html', {'tree': tree})



