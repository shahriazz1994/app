from django.shortcuts import render, get_object_or_404
from food.models import FoodCategory, FoodDetails
from django.views.generic import ListView, DetailView


class FoodCategoryView(ListView):
    model = FoodCategory
    template_name = 'food/food-category.html'
    context_object_name = 'food'


class FoodListView(ListView):
    model = FoodDetails
    template_name = 'food/food-list.html'
    context_object_name = 'food'

    ordering = ['-additiondate']


class FoodDetailsView(DetailView):
    model = FoodDetails
    template_name = 'food/FoodDetails_detail.html'
