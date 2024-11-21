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
        place_id = request.GET.get('place_id')
        place = get_object_or_404(Place, id=place_id)
        one_time_pass = OneTimePass.objects.create(place=place)
        one_time_pass.code = one_time_pass.id
        one_time_pass.save()
        data = {
            'code': one_time_pass.code,
        }
        return JsonResponse(data, safe=False)
