from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return f"{self.title} — {self.author}"
