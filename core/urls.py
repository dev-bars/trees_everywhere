from django.urls import path
from .views import CustomLoginView, home

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
]


from .views import my_trees

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('minhas-arvores/', my_trees, name='my_trees'),
]