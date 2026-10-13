TRANSACTION_STATUS = (
    ('p', 'کامل'), # posted
    ('d', 'در انتظار'), # drafted
    ('c', 'لغو شده') # cancelled
)

SECTION_STATUS = (
    ('in', 'موجود'), # in_stock
    ('low', 'موجودی کم'), # low_stock
    ('out', 'ناموجود') # out_of_stock
)

PRODUCT_STATUS = (
    ("a", "فعال"), # active
    ("d", "غیرفعال") # deactive
)