# Create your models here.
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


