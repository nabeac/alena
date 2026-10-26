from django.forms import ModelForm
from django.core.exceptions import ValidationError

from ..models.product import Category

class CategoryCreateUpdateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'is_active', 'sub_cat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Field-level uniqueness validation for 'title'
        self.fields['title'].validators.append(self.validate_unique_title)

        # Remove the record itself from the sub_cat options (only in edit mode)
        if self.instance and self.instance.pk:
            self.fields['sub_cat'].queryset = Category.objects.exclude(
                pk=self.instance.pk
            )
    
    def validate_unique_title(self, value):
        qs = Category.objects.filter(title__iexact=value.strip())
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("A category with this title already exists.")