from django.db import models

from .warehouse import WarehouseSection
from .product import Product, Unit
from .constants import TRANSACTION_STATUS
# Create your product's models here.

class DocumentItem(models.Model):
    document_id = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField()

    product = models.ManyToManyField(Product)
    unit = models.ForeignKey(Unit, related_name="document_items", on_delete=models.PROTECT)


class InOutDocument(models.Model):
    document_type = models.CharField(max_length=60)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=TRANSACTION_STATUS, default='d')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    warehouse_section = models.ForeignKey(WarehouseSection, related_name="inout_documents", on_delete=models.PROTECT)
    document_items = models.ForeignKey(DocumentItem, related_name="inout_documents", on_delete=models.PROTECT)

    @property
    def from_warehouse(self):
        return self.warehouse_section.warehouse


    def __str__(self):
        return self.document_type
    
class TransferDocument(models.Model):
    document_type = models.CharField(max_length=60)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=TRANSACTION_STATUS, default='d')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    from_section = models.ForeignKey(WarehouseSection, related_name="transfers_out", on_delete=models.PROTECT)
    to_section = models.ForeignKey(WarehouseSection, related_name="transfers_in", on_delete=models.PROTECT)
    document_items = models.ForeignKey(DocumentItem, related_name="transfer_documents", on_delete=models.PROTECT)

    # join with section to show them
    @property
    def from_warehouse(self):
        return self.from_section.warehouse

    @property
    def to_warehouse(self):
        return self.to_section.warehouse
    
    def __str__(self):
        return self.document_type