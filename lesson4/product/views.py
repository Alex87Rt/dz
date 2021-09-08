
from django.shortcuts import render
from product.forms import ProductForm
from product.models import Product


def index(request):
    return render(request, 'product/goods-list.html', {'products': Product.objects.all()})


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product/goods-list.html', {'products': Product.objects.all()})
        else:
            pass
    else:
        form = ProductForm()
    content = {'form': form}
    return render(request, 'product/good-create.html', content)

