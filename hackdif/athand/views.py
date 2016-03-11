from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("map_basic.html")
    return HttpResponse(template.render())