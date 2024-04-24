from django.shortcuts import render
import os
from PIL import Image
from django.conf import settings

# Create your views here.
def upload_image(request):
    if request.method == "GET":
        return render (request, "upload_image/upload_image.html")
    elif request.method == "POST":
        file = request.FILES.get('the_file')
        img = Image.open(file)
        path = os.path.join(settings.BASE_DIR, f'media/{file.name}')
        img = img.save(path)

        print(file)
        return render(request, "upload_image/upload_image_concluded.html")
