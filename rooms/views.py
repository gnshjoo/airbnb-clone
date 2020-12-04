from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    # page_kwarg = "potato"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = "hello"
        return context


class RoomDetail(DetailView):
    """ RoomDeatil Definition """

    model = models.Room


def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})
