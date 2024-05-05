from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
