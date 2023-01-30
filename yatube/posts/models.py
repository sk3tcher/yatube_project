from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.TextField()
    slug = models.TextField()
    description = models.TextField()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    def __str__(gr: Group):
        return gr.title

