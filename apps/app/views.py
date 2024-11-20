from django.shortcuts import render, get_object_or_404
from .models import Place

def main_page(request):
    places = Place.objects.all()
    for place in places:
        place.description = (place.description[:50] + '...') if len(place.description) > 50 else place.description
    return render(request, 'app/main.html', {'places': places})


    return render(request, 'main.html', {'places': places})
def detail_page(request, id):
    place = get_object_or_404(Place, id=id)
    return render(request, 'app/detail.html', {'place': place})
