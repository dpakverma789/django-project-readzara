from django.db import models


class Post(models.Model):
    post_image = models.ImageField(upload_to='images')
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_author = models.CharField(max_length=20)
    post_date = models.DateField()

    def __str__(self):
        info = f'{self.post_title} --- by {self.post_author}'
        return info
