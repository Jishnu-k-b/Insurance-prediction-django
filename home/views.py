from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("This is the homepage")


def about(request):
    return HttpResponse("This is the about us page")
