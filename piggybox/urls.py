from django.urls import path
from . import views

app_name = 'piggybox'

urlpatterns = [
    path('', views.index, name='index'),
    path('mypage/', views.WishListView.as_view(), name="mypage"),
    path('mypage/calendar/', views.CalendarByUserView.as_view(), name='calendar'),
    path('mypage/calendar/create/', views.DealCreate.as_view(), name='deal-create'),
    path('mypage/calendar/<int:pk>/delete/', views.DealDelete.as_view(), name='deal-delete'),
    path('mypage/calendar/<int:pk>/update/', views.DealUpdate.as_view(), name='deal-update'),
    path('mypage/calendar/<int:year>/<int:month>/', views.CalendarByUserView.as_view(), name='calendar'),
    path('mypage/wishlist/create/', views.WishlistCreate.as_view(), name="wishlist-create"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
]