from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title