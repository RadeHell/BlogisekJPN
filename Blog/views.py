from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def Main(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())


def Map(request):
  template = loader.get_template('Map.html')
  return HttpResponse(template.render())


def TravelOrders(request):
  template = loader.get_template('TravelOrders.html')
  return HttpResponse(template.render())

def Registration(request):
  template = loader.get_template('Registration.html')
  return HttpResponse(template.render())

def Login(request):
  template = loader.get_template('Login.html')
  return HttpResponse(template.render())