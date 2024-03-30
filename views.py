from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.
def apps(request):
    template = loader.get_template('public.html')
    # return HttpResponse("Hello world!")
    return HttpResponse(template.render())

def users(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
      'users': users,
    }
    return HttpResponse(template.render(context, request))
