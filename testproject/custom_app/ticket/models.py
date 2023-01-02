from django.db import models

from ticket import constants
from plugins import models as plugin_models
# Create your models here.

class Ticket(plugin_models.BaseModel):
    agent = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, related_name='agent')
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, related_name='client')
    status = models.CharField(plugin_models.enum_to_choices(constants.Status), default=1, max_length=1)
    title = models.CharField(max_length=30, db_index=True)
    description = models.TextField(null=False)
