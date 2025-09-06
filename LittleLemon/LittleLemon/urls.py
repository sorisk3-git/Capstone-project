from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Restaurant.urls')),
    path('booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('api/booking/', include(router.urls)),
    #path('restaurant/menu/', include('Restaurant.urls'))
]
