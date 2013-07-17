from django.shortcuts import render

from models import Offspring

def offsprings(request):
	offsprings = Offspring.objects.all()
	return render(request, 'offsprings/offsprings.html', {'offsprings': offsprings})

def offspring_page(request, offspring_id):
	offspring = Offspring.objects.get(id=offspring_id)
	return render(request, 'offsprings/offspring_page.html', {'offspring': offspring})