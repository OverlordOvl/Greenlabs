from django.urls import path
from main import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('city-detail/<str:city_id>', views.CityDetail.as_view(), name='city_detail'),
]
