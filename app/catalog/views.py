from django.shortcuts import render, get_object_or_404

from app.catalog.models import Product, Contact


def home(request):
    last_products = Product.objects.all().order_by('-created_at')[:5]
    context = {
        'last_products': last_products
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    template = 'catalog/contacts.html'
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    if request.method == 'POST':
        context.update(request.POST.dict())

    return render(request, template, context)


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {
        'object': prod
    }
    return render(request, 'catalog/product.html', context)