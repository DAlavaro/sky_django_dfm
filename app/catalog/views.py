from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    template = 'catalog/contacts.html'
    context = {}
    if request.method == 'POST':
        context.update(request.POST.dict())

    return render(request, template, context)