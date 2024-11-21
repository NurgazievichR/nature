import qrcode
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from lxml.parser import filename

from utils.generate_qr import generate_qr
from .models import Place, OneTimePass
from ..users.models import User


def main_page(request):
    places = Place.objects.all()
    for place in places:
        place.description = (place.description[:50] + '...') if len(place.description) > 50 else place.description
    return render(request, 'app/main.html', {'places': places})


    return render(request, 'main.html', {'places': places})
def detail_page(request, id):
    place = get_object_or_404(Place, id=id)
    return render(request, 'app/detail.html', {'place': place})

def place_page(request, id):
    place = get_object_or_404(Place, id=id)
    one_time_pass = OneTimePass.objects.create(place=place)
    one_time_pass.code = one_time_pass.id
    one_time_pass.save()

    data = "qr/" + str(id)
    filename = "temp_qr.png"
    img = qrcode.make(data)
    img.save(filename)

    img_resp = open(filename, 'rb')
    return FileResponse(img_resp)