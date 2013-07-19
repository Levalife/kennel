from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news.models import News

def home(request):
	news = News.objects.all()
	paginator = Paginator(news, 10)
	page = request.GET.get('page')
	try:
		all_news = paginator.page(page)
	except PageNotAnInteger:
		all_news = paginator.page(1)
	except EmptyPage:
		all_news = paginator.page(paginator.num_page)
	return render(request, 'home.html', {'all_news': all_news})

