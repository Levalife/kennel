from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm

from models import * 

def albums(request):
	albums = Album.objects.all()
	paginator = Paginator(albums, 5)
	try:
		page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		albums = paginator.page(page)
	except (InvalidPage, EmptyPage):
		albums = paginator.page(paginator.num_pages)

	return render(request,'gallery/albums.html', {'albums': albums})

def album(request, album_id, view="full"):
	num_pages = 30
	print view
	if view == "full":

		num_pages = 10
	album = Album.objects.get(pk=album_id)
	images = album.image_set.all()
	paginator = Paginator(images, num_pages)
	try: page = int(request.GET.get('page', '1'))
	except ValueError: page = 1

	try:
		images = paginator.page(page)
	except (InvalidPage, EmptyPage):
		images = pagination.page(paginator.num_pages)

	return render(request, 'gallery/album.html', {'album': album, 'images': images, 'view': view})
