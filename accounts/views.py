from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# Create your views here.
class ProfileDetailView (LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'