from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, create_oblast, oblast_details, city_create, house_create, delete_oblast

urlpatterns = [
    path('', home_page, name='home'),
    path('blogs/create/', create_oblast, name='create_oblast'),
    path('blogs/<int:pk>/', oblast_details, name='oblast_details'),
    path('blogs/<int:pk>/delete/', delete_oblast, name='delete_oblast'),
    path('blogs/<int:pk>/city-create', city_create, name='city_create'),
    path('blogs/<int:pk>/house-create', house_create, name='house_create')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

