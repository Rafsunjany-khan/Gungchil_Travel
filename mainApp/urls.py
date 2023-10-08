from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('bus/', views.bus, name='bus'),
    path('viewSeat/', views.viewSeat, name='viewSeat'),
    path('book/', views.book, name='book'),
    path('payment/', views.payment, name='payment'),

]