from django.core.exceptions import ValidationError


class UniqueNameFormMixin:
    """
    Case-insensitive unique validation for a single field.
    Set `unique_field` on the form class (e.g. "title" or "name").
    """
    unique_field = "name"
    unique_error_message = ("An item with this value already exists.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.unique_field].validators.append(self._validate_unique_value)

    def _validate_unique_value(self, value):
        model = self._meta.model
        qs = model.objects.filter(**{f"{self.unique_field}__iexact": value.strip()})
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError(self.unique_error_message)