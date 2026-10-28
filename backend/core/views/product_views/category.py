from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models.product import Category
from ...forms.product import CategoryCreateUpdateForm

class CategoryListView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "core/product_templates/category/category_list.html", {'categories':categories})


class CategoryCreateView(LoginRequiredMixin, View):
    form_class = CategoryCreateUpdateForm
    template_name = "core/product_templates/category/category_create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form":self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form": form})

    
class CategoryUpdateView(LoginRequiredMixin, View):
    form_class = CategoryCreateUpdateForm
    template_name = "core/product_templates/category/category_update.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.category_instance = get_object_or_404(Category, id=kwargs['category_id'])

    def get(self, request, *args, **kwargs):
        category = self.category_instance
        return render(request, self.template_name, {"form":self.form_class(instance=category)})

    def post(self, request, *args, **kwargs):
        category = self.category_instance
        form = self.form_class(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form":form} )


class CategoryDeleteView(View):
    template_name = "core/product_templates/category/category_list.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.category_instance = get_object_or_404(Category, id=kwargs['category_id'])

    def get(self, request, *args, **kwargs):
        return redirect('core:category_list')

    def post(self, request, *args, **kwargs):
        category = self.category_instance
        try:
            category.delete()
            messages.success(request, "Category deleted.")
        except ProtectedError:
            messages.error(
                request,
                "This category has subcategories or products. Move them first or deactivate the category.",
            )
        return redirect("core:category_list")