from django.shortcuts import render

def index(request):
    return render(request, 'art_gallery/art_gallery.html', {})

def inclusion(request):
    return render(request, 'art_gallery/inclusion_of_artwork.html')