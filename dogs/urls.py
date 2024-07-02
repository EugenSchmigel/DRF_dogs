from django.urls import path
from rest_framework import routers

from dogs.views.dog import DogListView, DogDetailView, DogUpdateView, DogCreateView, DogDeleteView, SetLikeToDog
from dogs.views.breed import BreedViewSet

urlpatterns = [

    path('set_like/', SetLikeToDog.as_view()),

    path('', DogListView.as_view(), name='dog_list'),
    path('<int:pk>/', DogDetailView.as_view()),
    path('<int:pk>/update/', DogUpdateView.as_view()),
    path('create/', DogCreateView.as_view(), name='dog_list'),
    path('<int:pk>/delete', DogDeleteView.as_view()),


]

router = routers.SimpleRouter()
router.register('breed', BreedViewSet)

urlpatterns += router.urls
