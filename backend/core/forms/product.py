from django.forms import ModelForm

from ..models.product import Category, Unit, Product
from ..mixins import UniqueNameFormMixin

class CategoryCreateUpdateForm(UniqueNameFormMixin, ModelForm):
    unique_field = "title"
    unique_error_message = ("A category with this title already exists.")

    class Meta:
        model = Category
        fields = ['title', 'description', 'is_active', 'sub_cat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the record itself from the sub_cat options (only in edit mode)
        if self.instance and self.instance.pk:
            self.fields['sub_cat'].queryset = Category.objects.exclude(
                pk=self.instance.pk
            )


class UnitCreateUpdateForm(UniqueNameFormMixin, ModelForm):
    unique_field = "name"
    unique_error_message = ("A unit with this title already exists.")
    class Meta:
        model = Unit
        fields = ['name', 'symbol', 'description', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class ProductCreateUpdateForm(UniqueNameFormMixin, ModelForm):
    unique_field = "name"
    unique_error_message = ("A product with this name already exists.")

    class Meta:
        model = Product
        fields = ['code', 'name', 'category', 'unit', 'description', 'barcode', 'min_stock', 'is_active', 'thumbnail', 'attributes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
