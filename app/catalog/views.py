from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.catalog.forms import ProductForm, ConfirmDeleteForm, VersionForm
from app.catalog.models import Product, Contact, Version


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.prefetch_related('version_set').all()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ConfirmDeleteForm
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.delete(request, *args, **kwargs)

        else:
            return self.form_invalid(form)


def contacts(request):
    template = 'catalog/contacts.html'
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    if request.method == 'POST':
        context.update(request.POST.dict())

    return render(request, template, context)


class VersionListView(ListView):
    model = Version

    def get_queryset(self):
        return Version.objects.filter(product_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return context

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:product_versions', kwargs={'pk': self.object.product.pk})


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

    def form_valid(self, form):
        print('form_valid вызвана')
        form.instance.product_id = self.kwargs['product_pk']
        return super().form_valid(form)


    def get_object(self, queryset=None):
        return Version.objects.get(pk=self.kwargs['version_pk'])

    def get_success_url(self):
        return reverse('catalog:product_versions', kwargs={'pk': self.object.product.pk})



