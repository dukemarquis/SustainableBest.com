from django.db import models

class Sustainable_Products(models.Model):
    product_name = models.CharField(max_length=200)
    recommend_reason = models.CharField(max_length=500)
    reference_link = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

