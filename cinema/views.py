from django.views.generic import TemplateView, ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import *
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = "home.html"

class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user"


class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ['full_name', 'phone']
    success_url = reverse_lazy("user_list")

class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ['full_name', 'phone']
    success_url = reverse_lazy("user_list")

class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")


class JanreListView(ListView):
    model = Janre
    template_name = "janre_list.html"
    context_object_name = "janres"

class JanreDetailView(DetailView):
    model = Janre
    template_name = "janre_detail.html"
    context_object_name = "janre"


class JanreCreateView(CreateView):
    model = Janre
    template_name = "janre_create.html"
    fields = ['name']
    success_url = reverse_lazy("janre_list")

class JanreUpdateView(UpdateView):
    model = Janre
    template_name = "janre_update.html"
    fields = ['name']
    success_url = reverse_lazy("janre_list")

class JanreDeleteView(DeleteView):
    model = Janre
    template_name = "janre_delete.html"
    success_url = reverse_lazy("janre_list")


class TeatrListView(ListView):
    model = Teatr
    template_name = "teatr_list.html"
    context_object_name = "teatrs"

class TeatrDetailView(DetailView):
    model = Teatr
    template_name = "teatr_detail.html"
    context_object_name = "teatr"


class TeatrCreateView(CreateView):
    model = Teatr
    template_name = "teatr_create.html"
    fields = ['name', 'address', 'image']
    success_url = reverse_lazy("teatr_list")

class TeatrUpdateView(UpdateView):
    model = Teatr
    template_name = "teatr_update.html"
    fields = ['name', 'address', 'image']
    success_url = reverse_lazy("teatr_list")

class TeatrDeleteView(DeleteView):
    model = Teatr
    template_name = "teatr_delete.html"
    success_url = reverse_lazy("teatr_list")


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    context_object_name = "films"

class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"
    context_object_name = "film"


class FilmCreateView(CreateView):
    model = Film
    template_name = "film_create.html"
    fields = ['name', 'janre', 'created_on', 'image', 'trailer', 'description']
    success_url = reverse_lazy("film_list")

class FilmUpdateView(UpdateView):
    model = Film
    template_name = "film_update.html"
    fields = ['name', 'janre', 'created_on', 'image', 'trailer', 'description']
    success_url = reverse_lazy("film_list")

class FilmDeleteView(DeleteView):
    model = Film
    template_name = "film_delete.html"
    success_url = reverse_lazy("film_list")


class ShowListView(ListView):
    model = Show
    template_name = "show_list.html"
    context_object_name = "shows"

class ShowDetailView(DetailView):
    model = Show
    template_name = "show_detail.html"
    context_object_name = "show"


class ShowCreateView(CreateView):
    model = Show
    template_name = "show_create.html"
    fields = ['film', 'date', 'time', 'teatr', 'price_bil']
    success_url = reverse_lazy("show_list")

class ShowUpdateView(UpdateView):
    model = Show
    template_name = "show_update.html"
    fields = ['film', 'date', 'time', 'teatr', 'price_bil']
    success_url = reverse_lazy("show_list")

class ShowDeleteView(DeleteView):
    model = Show
    template_name = "show_delete.html"
    success_url = reverse_lazy("show_list")
    success_url = reverse_lazy("film_list")


class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"


class OrderCreateView(CreateView):
    model = Order
    template_name = "order_create.html"
    fields = ['show', 'amount', 'payment', 'total', 'user']
    success_url = reverse_lazy("order_list")

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "order_update.html"
    fields = ['show', 'amount', 'payment', 'total', 'user']
    success_url = reverse_lazy("order_list")

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "order_delete.html"
    success_url = reverse_lazy("order_list")


