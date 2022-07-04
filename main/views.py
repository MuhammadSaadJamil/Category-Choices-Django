from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView
from .form import *


class AddData(CreateView):
    form_class = DataForm
    template_name = 'index.html'
    success_url = reverse_lazy("data")


class ShowData(ListView):
    model = Data
    template_name = 'data.html'
