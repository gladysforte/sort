from django.db import models
from django.utils import timezone
# Create your models here.


class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rank = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ranks'

