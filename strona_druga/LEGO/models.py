from django.db import models
from django.utils import timesince, timezone

# Create your models here.


class Set(models.Model):
    set_number = models.CharField(max_length=10, primary_key=True)
    min_price = models.FloatField()
    avg_price = models.FloatField()
    max_price = models.FloatField()
    brickprice = models.FloatField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.set_number


class Brick(models.Model):
    brick_number = models.CharField(max_length=20)
    color_id = models.CharField(max_length=10)
    category_id = models.IntegerField()
    type = models.CharField(max_length=15)
    min_price = models.FloatField()
    avg_price = models.FloatField()
    max_price = models.FloatField()
    notes = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.type} {self.brick_number} {self.color_id}"


class SetBricks(models.Model):
    set_number = models.CharField(max_length=100)
    brick_number = models.CharField(max_length=100)
    type = models.CharField(max_length=15)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def calculate_price(self):
        try:
            part = Brick.objects.get(
                brick_number=self.brick_number, color_id=self.color
            )
            return part.avg_price * self.quantity
        except Brick.DoesNotExist:
            return 0

    def save(self, *args, **kwargs):
        self.parts_price = self.calculate_price()
        super().save(*args, **kwargs)
