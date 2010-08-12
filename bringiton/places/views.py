# Create your views here.

from django.template import Context, loader
from bringiton.places.models import Place
from bringiton.places.models import Post
from bringiton.places.models import PostForm
from bringiton.places.models import PlaceForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import modelformset_factory
import datetime

def index(request):
    places_list = Place.objects.all()
    return render_to_response('places/index.html', {'places_list': places_list})


def detail(request, place_id, post_offset = 0):
    try:
        p = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404

    numPosts = 10
    posts = Post.objects.filter(place=p.id)[post_offset:post_offset+numPosts]
    try:
        owner = p.owners.filter(id=request.user.id)
        is_owner = True
    except:
        owner = None
        is_owner = False
    if(is_owner):
        postForm = PostForm()
        #postForm = modelformset_factory(Post)
    else:
        postform = None

    if request.method == "POST" and is_owner:
        formset = PostForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.instance.pub_date = datetime.datetime.now()
            formset.instance.place_id = p.id
            formset.save()
            # Do something.
    return render_to_response('places/detail.html', {'place': p, 'posts' : posts, 'is_owner' : is_owner, 'postForm':postForm})


def edit(request, place_id, post_offset = 0):
    try:
        p = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404

    
    try:
        owner = p.owners.filter(id=request.user.id)
        is_owner = True
    except:
        owner = None
        is_owner = False
    if(is_owner):
        postForm = PlaceForm(p)
        #postForm = modelformset_factory(Post)
    else:
        postform = None

    if request.method == "POST" and is_owner:
        formset = PlaceForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # Do something.
    return render_to_response('places/edit.html', {'place': p, 'is_owner' : is_owner, 'postForm':postForm})


