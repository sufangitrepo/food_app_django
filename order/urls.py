from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderView,OrderItemView

router = DefaultRouter()
router.register('order', OrderView, basename='order')
router.register('orderItem', OrderItemView, basename='orderitem')


urlpatterns = [
    path('', include(router.urls))
]