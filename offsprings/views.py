from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Offspring

def offsprings(request):
	offsprings = Offspring.objects.all()

	paginator = Paginator(offsprings, 5)
	page = request.GET.get('page')
	try:
		page_offsprings = paginator.page(page)
	except PageNotAnInteger:
		page_offsprings = paginator.page(1)
	except EmptyPage:
		page_offsprings = paginator.page(paginator.num_page)
	return render(request, 'offsprings/offsprings.html', {'page_offsprings': page_offsprings})

def offspring_page(request, offspring_id):
	offspring = Offspring.objects.get(id=offspring_id)
	return render(request, 'offsprings/offspring_page.html', {'offspring': offspring})