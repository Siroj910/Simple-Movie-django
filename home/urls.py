from django.urls import path
from .views import detail, category_list, subcriber

app_name='home'

urlpatterns = [
	path('category/<slug:slug>/',category_list , name='category_list'),
	path('movie/<int:id>/', detail, name='detail'),
	path('subcribes/', subcriber, name='subcribes')

]
