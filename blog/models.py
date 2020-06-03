from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=128)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)
    user_email = models.EmailField()

    def __str__(self):
        return self.title
