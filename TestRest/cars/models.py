from django.db import models
from django.contrib.auth import get_user_model
Dealer = get_user_model()

# Create your models here.

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    ENGINES = (
        (1, '183'),
        (2, '249'),
        (3, '245'),
        (4, '330'),
        (5, '565'),
    )
    engine = models.IntegerField(verbose_name='Engine', choices=ENGINES)
    dealer = models.ForeignKey(Dealer, verbose_name='Дилер', on_delete=models.CASCADE)

