from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from products.models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # Renders html page, with HTTP status code 404

    return HttpResponse(f"Product id {obj.pk}")

def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    return JsonResponse({"id": obj.id})