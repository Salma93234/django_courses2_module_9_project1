# from django.http import HttpResponse
# def contact(response):
#     return HttpResponse("this is contact page")

from django.http import HttpResponse


def home(request):
    return HttpResponse("This is home page")
def contact(request):
    return HttpResponse("This is contact page")
