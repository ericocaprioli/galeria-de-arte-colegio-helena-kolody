from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Art
from django.contrib.auth.decorators import login_required


@login_required(login_url="/../auth/")
def inclusion(request):
    if request.method == 'GET':
        return render(request, 'art_gallery/inclusion_of_artwork.html', {})
    elif request.method == 'POST':
        user_art = request.user
        form_art = request.POST
        image_art = request.FILES.get('image_art')
        object_art = Art(user=user_art, title=form_art['title'], teacher=form_art['professor'], date_at=form_art['year'], arq=image_art)
        object_art.save()
        return render(request, 'art_gallery/inclusion_concluded.html')
    

class ArtListView(ListView):
    model = Art
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
