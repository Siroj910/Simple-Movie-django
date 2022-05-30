from django.urls import path

from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('check/', views.GetSms, name='check-sms')

]