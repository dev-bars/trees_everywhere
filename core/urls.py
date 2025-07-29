from django.urls import path
from .views import (
    CustomLoginView,
    home,
    my_trees,
    planted_tree_detail,
    planted_trees_api,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('minhas-arvores/', my_trees, name='my_trees'),
    path('arvore/<int:pk>/', planted_tree_detail, name='planted_tree_detail'),
    path('api/minhas-arvores/', planted_trees_api, name='planted_trees_api'),
]
