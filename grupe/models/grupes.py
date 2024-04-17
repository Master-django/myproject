
from django.db import models

# Create your models here.


class Grupe(models.Model):
    name = models.CharField("Name", max_length=100, blank= True, null= True)
    address = models.CharField("Suroga", max_length = 100)
    number_phone = models.IntegerField("Raqami_telefon")
    burth_day = models.DateField("soli_tavalud")
    nation = models.CharField("Millat", max_length = 100)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Груп'
        verbose_name_plural = 'групы'

        def __str__(self) -> str:
            return self.name 