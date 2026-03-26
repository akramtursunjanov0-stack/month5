from django.db import models
from django.contrib.auth.models import User
import random 

class ConfiMationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='confirmation_code')
    code = models.CharField(max_length=6)
    creted_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_code():
        return "".join([str(random.randint(0,9)) for _ in range(6) ])