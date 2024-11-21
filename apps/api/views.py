from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from apps.app.models import Place


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