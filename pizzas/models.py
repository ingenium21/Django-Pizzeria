"""import models from django db"""
from django.db import models

# Create your models here.
class Pizza(models.Model):
    """The types of pizzas that exist"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.name)

class Topping(models.Model):
    """Specific toppings on the type of pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) < 25:
            return f"{self.text}"
        else:
            return f"{self.text[:25]}..."
