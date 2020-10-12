from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from products.models import Product


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    context = {"name": "Anders"}
    return render(request, "home.html", context)


# Two different approaches "regular" and Json
def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # Renders html page, with HTTP status code 404

    # return HttpResponse(f"Product id {obj.pk}")
    return render(request, "products/detail.html", {"object": obj})

def product_list_view(request, *args, **kvargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    return JsonResponse({"id": obj.id})
