from django.shortcuts import render, redirect
from django.http import HttpResponse,StreamingHttpResponse
from recognizer.models import UserDetails
from django.views.decorators import gzip

from .src.camera import *

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def next_view(request):
    name = request.GET.get('name')
    email = request.GET.get('email')

    if name and email:
        user_details = UserDetails(name=name, email=email)
        user_details.save()

        return redirect('success')

    return render(request, 'registeration.html')

@gzip.gzip_page
def success(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass



