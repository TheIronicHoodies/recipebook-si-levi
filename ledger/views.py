from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage

class RecipesList(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipesDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = '/accounts/login'


class RecipesAdd(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'


class RecipesUpload(CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = "recipe_upload.html"

    def get_success_url(self):
        return reverse_lazy("ledger:recipe", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return ctx
