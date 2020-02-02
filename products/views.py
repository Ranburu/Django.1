from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForms


# def product_create_view(request):
#     my_form = RawProductForms()
#     if request.method == "POST":
#         my_form = RawProductForms(request.POST)
#         if my_form.is_valid:
#             print(my_form.data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)
def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('')
    context = {
        "object": obj,
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'price': 199.99
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    initial_data = {
        'price': 199.99
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #    'title': obj.title,
#     #    'description': obj.description,
#     # }
#     context = {
#         'object': obj,
#     }
#     return render(request, "products/product_detail.html", context)
