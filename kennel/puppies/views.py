from django.shortcuts import render

from models import Puppies

def puppies(request):
	puppies = Puppies.objects.all()
	return render(request, 'puppies/puppies.html', {'puppies': puppies})

def litter(request, puppies_id):
	litter = Puppies.objects.get(id=puppies_id)
	return render(request, 'puppies/litter.html', {'litter': litter})