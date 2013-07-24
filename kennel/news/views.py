from django.shortcuts import render
from models import News

def news_page(request, news_id):
	news = News.objects.get(pk=news_id)
	return render(request, 'news/news.html', {'news': news})
