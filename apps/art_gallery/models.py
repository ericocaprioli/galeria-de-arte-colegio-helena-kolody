from django.db import models
from django.conf import settings
    
class Art(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=30)
    teacher = models.CharField(max_length=20)
    date_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    arq = models.ImageField(upload_to='data/')

    def __str__(self):
        return f'{self.title}'
