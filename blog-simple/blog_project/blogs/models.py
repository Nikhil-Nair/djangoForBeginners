from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title