from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models.product import Unit
from ...forms.product import UnitCreateUpdateForm


class UnitListView(LoginRequiredMixin, View):
    def get(self, request):
        units = Unit.objects.all()
        return render(request, "core/product_templates/unit/unit_list.html", {'units':units})

    
class UnitCreateView(LoginRequiredMixin, View):
    form_class = UnitCreateUpdateForm
    template_name = "core/product_templates/unit/unit_create.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form":self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:unit_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form": form})

    
class UnitUpdateView(LoginRequiredMixin, View):
    form_class = UnitCreateUpdateForm
    template_name = "core/product_templates/unit/unit_update.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.unit_instance = get_object_or_404(Unit, id=kwargs['unit_id'])

    def get(self, request, *args, **kwargs):
        unit = self.unit_instance
        return render(request, self.template_name, {"form":self.form_class(instance=unit)})

    def post(self, request, *args, **kwargs):
        unit = self.unit_instance
        form = self.form_class(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect("core:unit_list")
        
        # Invalid form: The form is re-rendered with the data and errors.
        return render(request, self.template_name, {"form":form} )

    
class UnitDeleteView(LoginRequiredMixin, View):
    template_name = "core/product_templates/unit/unit_list.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.unit_instance = get_object_or_404(Unit, id=kwargs['unit_id'])

    def get(self, request, *args, **kwargs):
        return redirect("core:unit_list")
    
    def post(self, request, *args, **kwargs):
        unit = self.unit_instance
        try:
            unit.delete()
            messages.success(request, "Unit deleted.")
        except ProtectedError:
            messages.error(
                request,
                "This unit Move them first or deactivate the unit.",
            )
        return redirect("core:unit_list")

    
