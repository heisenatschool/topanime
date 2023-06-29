from django.http import HttpResponse
from django.template import loader
from .models import Anime

def topanime(request):
    animes = Anime.objects.all().values()
    template = loader.get_template('home.html')

    return HttpResponse(template.render({
        'animes': [x for x in animes if x['SHOWN'] == True][:4]
    }, request))
