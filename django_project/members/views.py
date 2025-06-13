from django.http import HttpResponse
from django.template import loader
from .models import Member

def main(request):
  template = loader.get_template('main.html')

  return HttpResponse(template.render())

def members(request):
  allMembers = Member.objects.all()
  template = loader.get_template('list.html')
  context = {
    'members': allMembers,
  }

  return HttpResponse(template.render(context, request))

def details(request, id):
  member = Member.objects.get(id=id)
  template = loader.get_template('detail.html')
  context = {
    'member': member,
  }

  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('testing.html')
  data = {
    'fruits': ['Apple', 'Orange', 'Banana'],
  }

  return HttpResponse(template.render(data, request))