from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Domain(models.Model):
    domain=models.CharField(max_length=100)
    def __str__(self):
        return self.domain
    '''def order_by_category(self):
        category=self.order_by_category['category']
        for i in domain:'''

class Notes(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to= 'uploads', default='related_post_no_available_image.png')
    category=models.ForeignKey(Domain, on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
    posted=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    object=models.Manager


