from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePageView, name='homePage'),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls',namespace='home')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



