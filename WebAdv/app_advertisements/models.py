from django.db import models

class Advertisements(models.Model):
    title=models.CharField("заголовок",max_lenght=128)
    discription=models.TextField("описание")
    price=models.DecimalField("цена",max_digits=10,decimal_places=2)
    auction=models.BooleanField("торг",help_text="отметьте,если торг уместен.")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    