from django.db import models
from uuid import uuid4

class School(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    code_inep = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'schools'

    def __str__(self):
        return self.name