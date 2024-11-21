from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from apps.app.models import Place, OneTimePass


class PlacesAPIView(APIView):

    @staticmethod
    def get(request):
        places = Place.objects.all()

        data = list()
        for place in places:
            place_data = {
                'id': place.id,
                'name': place.name,
                'description': place.description,
                'price': place.price,
                'location': place.location,
            }
            data.append(place_data)
        return JsonResponse(data, safe=False)

class GenerateQRCodeAPIView(APIView):

    @staticmethod
    def get(request):
        place = request.GET.get('place')
        place_obj = get_object_or_404(Place, id=place.id)
        one_time_pass = OneTimePass.objects.create(place=place_obj)
        one_time_pass.code = one_time_pass.id
        one_time_pass.save()
        data = {
            'code': one_time_pass.code,
            'place': place.name,
        }
        return JsonResponse(data, safe=False)
