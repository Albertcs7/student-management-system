from django.db import models

class faculty(models.Model):
    fname = models.CharField(max_length=15)
    

    def __str__(self):
        return self.user.username