from django.urls import path 

from . import views

urlpatterns = [
	path('',views.index , name="index"),
	path('hotel.html',views.hotel, name="hotel"),
	path('payment.html',views.payment),
	path('success.html',views.success),
]
