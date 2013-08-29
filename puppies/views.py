from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Puppies

def puppies(request):
	puppies = Puppies.objects.all().order_by('-pk')

	paginator = Paginator(puppies, 5)
	page = request.GET.get('page')
	try:
		page_puppies = paginator.page(page)
	except PageNotAnInteger:
		page_puppies = paginator.page(1)
	except EmptyPage:
		page_puppies = paginator.page(paginator.num_page)
	return render(request, 'puppies/puppies.html', {'page_puppies': page_puppies})

def litter(request, puppies_id):
	litter = Puppies.objects.get(id=puppies_id)
	return render(request, 'puppies/litter.html', {'litter': litter})