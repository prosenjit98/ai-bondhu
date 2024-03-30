from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from users.models import User

# Create your views here.
def users_index(request):
    users = User.objects.all()
    template = loader.get_template('users/index.html')
    context = {
        "users": users
    }
    return HttpResponse(template.render(context, request))

def users_show(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('users/show.html')
    context = {
        "user": user
    }
    return HttpResponse(template.render(context, request))
