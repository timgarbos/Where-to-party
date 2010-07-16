# Create your views here.

from django.template import Context, loader
from bringiton.places.models import Place
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    places_list = Place.objects.all()
    return render_to_response('places/index.html', {'places_list': places_list})


def detail(request, place_id):
    try:
        p = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404
    return render_to_response('places/detail.html', {'place': p})
