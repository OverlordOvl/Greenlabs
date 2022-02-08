from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main.models import Resident, City


class MainPage(View):

    def get(self, request: WSGIRequest, *args, **kwargs) -> HttpResponse:
        residents = Resident.objects.all()
        top_cities = City.objects.all().annotate(residents=Count('resident')).order_by("-residents")[:5]
        return render(request, 'index.html', context={"page_title": "Main page", "residents": residents, "top_cities": top_cities})


class CityDetail(View):

    def get(self, request: WSGIRequest, *args, **kwargs) -> HttpResponse:
        city_id = kwargs.get('city_id')
        city = City.objects.get(id=city_id)
        residents = city.resident_set.all()
        return render(request, 'city_detail.html', context={"page_title": "Main page", "residents": residents, "city_name": city.name})
