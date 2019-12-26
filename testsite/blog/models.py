from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    content=models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateTimeField()
    comment=models.CharField(max_length=500)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
