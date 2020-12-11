from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import ProductModelForm

from products.models import Product

# # This is the WRONG way of doing it
# # Everyone can create objects in the databases
# def bad_view(request, *args, **kwargs):
#     # print(dict(request.GET))
#     my_request_data = dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == "true":
#         print("new product")        
#     return HttpResponse("Dont do this")


# Create your views here.
def search_view(request):
    # return HttpResponse("<h1>Hello World</h1>")
    # context = {"name": "Anders"}    

    query = request.GET.get('q') # q is refered as query
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs) # qs is query set
    context = {"name": "abc", "query": query}
    return render(request, "home.html", context)


# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
            
#             # Data is being validated by a Django Form
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get("title"))
#                 title_from_input = my_form.cleaned_data.get("title")
#                 Product.objects.create(title=title_from_input)
#                 # print("post_data", post_data)

#     return render(request, "forms.html", {})

# from django.contrib.auth.decorators import login_required
# @login_required
@staff_member_required
def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():

        obj = form.save(commit=False)
        # do some stuff
        obj.user = request.user
        obj.save()

        # print(form.cleaned_data) # Cleaned data is Validated data
        # data = form.cleaned_data
        # Product.objects.create(**data)        
        
        form = ProductModelForm()

        # Redirect options
        # return HttpResponceRedirect("/succes")
        # return redirect("/succes")
    return render(request, "forms.html", {"form": form})

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
