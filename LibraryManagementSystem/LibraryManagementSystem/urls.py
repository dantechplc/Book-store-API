# backend/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from libraryfrontend import views
from . import settings
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'author', views.AuthorView, 'author')
router.register(r'publisher', views.PublisherView, 'publisher')
router.register(r'book', views.BookView, 'book')
router.register(r'category', views.CategoryView, 'category')
router.register(r'user', views.UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', obtain_jwt_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

