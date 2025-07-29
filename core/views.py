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
from .models import PlantedTree

@login_required
def planted_tree_detail(request, pk):
    tree = get_object_or_404(PlantedTree, pk=pk, user=request.user)
    return render(request, 'core/planted_tree_detail.html', {'tree': tree})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PlantedTree
from .serializers import PlantedTreeSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def planted_trees_api(request):
    user = request.user
    planted_trees = PlantedTree.objects.filter(user=user)
    serializer = PlantedTreeSerializer(planted_trees, many=True)
    return Response(serializer.data)




