from django.shortcuts import render,get_object_or_404
from .models import Videos, Category, SubscribeHistory,Subcribe, TopUpBalance
from django.core.paginator import Paginator




def homePageView(request):
	videos = Videos.objects.all()
	search = request.GET.get('search')
	category = Category.objects.all()
	balance = TopUpBalance.objects.order_by('cost')


	if search is None:
		videos = Videos.objects.all()		
	
	else:
		videos = Videos.objects.filter(name__icontains=search)

	# set up pagination 
	pagination = Paginator(videos, 6)
	page = request.GET.get('page')

	videos_paginator = pagination.get_page(page)
	# end pagination
	
	context = {
		'videos':videos,
		'videos_paginator':videos_paginator,
		'category':category,
		'balance':balance
		}

	return render(request, "home.html", context)





#har bir film uchun page, shu film haqida malumot olish (batafsil)
def detail(request, id):
	video = Videos.objects.filter(id=id)

	context = {
		"video":video,
	}
	return render(request,"detail.html", context)



def category_list(request, slug):

	category = get_object_or_404(Category, slug=slug) 
	films = Videos.objects.filter(category=category)

	pagination = Paginator(films, 6)
	page = request.GET.get('page')


	films_paginator = pagination.get_page(page)
	
	context = {
		'films':films,
		'film_paginator':films_paginator
		}

	return render(request,"category_list.html", context)


def subcriber(request):
	subHistory = Subcribe.objects.all()
	context = {"subHistory":subHistory}

	return render(request, "subcribe.html", context)









"""	регистрация/авторизация пользователей через номер телефона и смс код
	каталог - фильмы/сериалы/мультфильмы/мультсериалы
	видеофайлы - может быть один видеофайлов, так и несколько, а так же по сезонам
	подписки (тарифы) - доступ к фильмам и прочим по подписке
"""