from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shortner/index.html")

# Shorten the url 5 with only 5 stirngs   
def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)