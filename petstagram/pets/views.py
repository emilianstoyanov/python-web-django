from django.shortcuts import render, redirect

# Create your views here.
from pets.models import Pet, Like


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),

    }

    return render(request, 'pets/pet_list.html', context)


def show_pet_details(request, pk):
    context = {
        'pet': Pet.objects.get(pk=pk),

    }
    return render(request, 'pets/pet_details.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('list pets', pk)
