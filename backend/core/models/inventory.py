from django.db import models
from django.core.exceptions import ValidationError

from .product import Product
from .warehouse import WarehouseSection
from .stock_document import InOutDocument, TransferDocument
from config import settings

from .constants import SECTION_STATUS, TRANSACTION_STATUS
# Create your product's models here.

class InventorySection(models.Model):
    quantity = models.DecimalField(max_digits=12, decimal_places=3)
    status = models.CharField(max_length=3, choices=SECTION_STATUS)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, related_name="inventory_sections", on_delete=models.PROTECT)
    warehouse_section = models.ForeignKey(WarehouseSection, related_name="inventory_sections", on_delete=models.PROTECT)

    @property
    def from_warehouse(self):
        return self.warehouse_section.warehouse

    def __str__(self):
        return f'{self.warehouse_section} : {self.quantity} : {self.product}'

class InventoryTransaction(models.Model):
    transaction_type = models.CharField()
    status = models.CharField(max_length=1, choices=TRANSACTION_STATUS, default='d')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inventory_transactions", on_delete=models.SET_NULL, null=True)
    in_out_document = models.ForeignKey(InOutDocument, related_name="inventory_transactions", on_delete=models.PROTECT, null=True, blank=True)
    transfer_document = models.ForeignKey( TransferDocument, related_name="inventory_transactions", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.transaction_type

    def clean(self):
        super().clean()
        if not self.in_out_document_id and not self.transfer_document_id:
            raise ValidationError('تراکنش باید به یک سند وصل باشد.')
        if self.in_out_document_id and self.transfer_document_id:
            raise ValidationError('تراکنش نمی‌تواند همزمان به دو سند وصل باشد.')