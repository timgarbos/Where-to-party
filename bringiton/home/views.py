# Create your views here.

from django.template import Context, loader
from bringiton.places.models import Place
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    return render_to_response('home/index.html')
