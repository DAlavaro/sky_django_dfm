from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.blog.models import Blog
from django.urls import reverse_lazy
from pytils.translit import slugify

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)  # Сохраняем форму, но пока не записываем объект в базу данных
            self.object.slug = slugify(self.object.title)  # Генерируем slug
            self.object.save()  # Сохраняем объект с уже сгенерированным slug в базу данных
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('blog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')