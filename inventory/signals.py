from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction, Product

def _apply_delta(product: Product, delta):
    product.qty_on_hand = (product.qty_on_hand or 0) + delta
    product.save(update_fields=["qty_on_hand", "updated_at"])

@receiver(post_save, sender=Transaction)
def on_trx_saved(sender, instance: Transaction, created, **kwargs):
    # hitung delta dibanding record lama bila update
    delta = instance.quantity if instance.trx_type == Transaction.IN else -instance.quantity
    if not created:
        old = sender.objects.get(pk=instance.pk)
        old_delta = old.quantity if old.trx_type == Transaction.IN else -old.quantity
        delta = delta - old_delta
    if delta:
        _apply_delta(instance.product, delta)

@receiver(post_delete, sender=Transaction)
def on_trx_deleted(sender, instance: Transaction, **kwargs):
    delta = -(instance.quantity) if instance.trx_type == Transaction.IN else instance.quantity
    _apply_delta(instance.product, delta)
