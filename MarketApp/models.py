# Create your models here.
from django.conf import settings
from django.db import models as db

class ItemDB(db.Model):
    item_id = db.AutoField(primary_key=True)
    title = db.CharField(max_length=120, null=False, unique=True)
    description = db.CharField(max_length=350, null=False)
    price = db.FloatField(null=False)
    quantity = db.IntegerField(null=False)
    image_url =  db.ImageField(upload_to='items/', null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "ItemDB"
        verbose_name = "Item"
        verbose_name_plural = "Items"

class CartItemDB(db.Model):
    id = db.AutoField(primary_key=True)
    user_id = db.ForeignKey(settings.AUTH_USER_MODEL, on_delete=db.CASCADE)
    item_id = db.ForeignKey('ItemDB', on_delete=db.CASCADE, null=False)
    quantity = db.IntegerField()


    def __str__(self) -> str:
        return self.item_id.title if isinstance(self.item_id.title, str) else str(self.item_id.title)
    
    class Meta:
        db_table = "CartItemDB"
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"


