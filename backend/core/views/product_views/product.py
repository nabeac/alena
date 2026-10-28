from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models.product import Product
from ...forms.product import ProductCreateUpdateForm


class ProductListView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "core/product_templates/product/product_list.html", {'products':products})

    
class ProductCreateView(LoginRequiredMixin, View):
    form_class = ProductCreateUpdateForm
    template_name = "core/product_templates/product/product_create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form":self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("core:product_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form": form})

    
class ProductUpdateView(LoginRequiredMixin, View):
    form_class = ProductCreateUpdateForm
    template_name = "core/product_templates/product/product_update.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.product_instance = get_object_or_404(Product, id=kwargs['product_id'])

    def get(self, request, *args, **kwargs):
        product = self.product_instance
        return render(request, self.template_name, {"form":self.form_class(instance=product)})

    def post(self, request, *args, **kwargs):
        product = self.product_instance
        form = self.form_class(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("core:product_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form":form} )

    
class ProductDeleteView(LoginRequiredMixin, View):
    template_name = "core/product_templates/product/product_list.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.product_instance = get_object_or_404(Product, id=kwargs['product_id'])

    def get(self, request, *args, **kwargs):
        return redirect("core:product_list")
    
    def post(self, request, *args, **kwargs):
        product = self.product_instance
        try:
            product.delete()
            messages.success(request, "Product deleted.")
        except ProtectedError:
            messages.error(
                request,
                "This product Move them first or deactivate the product.",
            )
        return redirect("core:product_list")

    
