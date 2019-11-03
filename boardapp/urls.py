from django.urls import path
from . views import signupfunc
from .views import loginfunc
from .views import listfunc
from .views import logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate
from django.conf.urls.static import static
from django.conf import settings

app_name = 'boardapp'
urlpatterns = [
    path('signup/', signupfunc, name = 'signup'),
    path('login/', loginfunc, name = 'login'),
    path('list/', listfunc, name = 'list'),
    path('logout/', logoutfunc, name = 'logout'),
    path('detail/<int:pk>', detailfunc, name = 'detail'),
    path('good/<int:pk>', goodfunc, name = 'good'),
    path('read/<int:pk>', readfunc, name = 'read'),
    path('create/', BoardCreate.as_view(), name = 'create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
