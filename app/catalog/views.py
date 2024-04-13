from django.shortcuts import render

from app.catalog.models import Product, Contact


def home(request):
    last_products = Product.objects.all().order_by('-created_at')[:5]

    for product in last_products:
        print(product.title)
    return render(request, 'catalog/home.html')


def contacts(request):
    template = 'catalog/contacts.html'
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    if request.method == 'POST':
        context.update(request.POST.dict())

    return render(request, template, context)