from django.shortcuts import render
from models import Gender, Dog

def our_dogs(request):

	#males = Dog.objects.get(Dog.sex.gender = 'Male')
	#females = Dog.objects.get(Dog.sex.gender = 'Female')
	return render(request, 'dogs/our_dogs.html')

def males(request):
	gender = Gender.objects.get(gender="Male")
	males = gender.dog_set.all()
	return render(request, 'dogs/males.html', {'males': males})

def females(request):
	gender = Gender.objects.get(gender="Female")
	females = gender.dog_set.all()
	return render(request, 'dogs/females.html', {'females': females})

def dog_page(request, dog_id):
	dog = Dog.objects.get(id=dog_id)
	print dog.photo
	return render(request, 'dogs/dog_page.html', {'dog': dog})
