from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('bus/', views.bus, name='bus'),
    path('viewSeat/', views.viewSeat, name='viewSeat'),
    path('book/', views.book, name='book'),
   # path('payment/', views.payment, name='payment'),
    path('ticket/', views.ticket, name='ticket'),
    path('travel/', views.travel, name='travel'),
    path('test1/', views.test1, name='test1'),
    path('search/', views.search, name='search'),

]