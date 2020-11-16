from django.urls import path

from pets.views import list_pets, like_pet, show_pet_details

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('details/<int:pk>/', show_pet_details, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),

]
