import qrcode
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
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

def payment_page(request, id):
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

def qr_handler(request, id):
    one_time_pass = get_object_or_404(OneTimePass, id=id)
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if user.role == 'staff':
            return render(request, 'app/approve_qr')
        else:
            return HttpResponse('Unauthorized', status=401)