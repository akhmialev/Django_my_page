from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title