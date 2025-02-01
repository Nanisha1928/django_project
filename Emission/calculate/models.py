from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class Register(models.Model):
    UserName = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    message = models.TextField()

    def set_password(self, raw_password):
        self.Password = make_password(raw_password)

    def check_password(self, raw_password):

        return check_password(raw_password, self.Password)

    def _str_(self):
        return self.UserName


class Carbon(models.Model):
    # Fields to store input values
    electricity = models.FloatField(help_text="Electricity usage in kWh")
    travel = models.FloatField(help_text="Travel distance in km")
    meat = models.FloatField(help_text="Meat consumption in kg")

    # Calculated total footprint
    total = models.FloatField(help_text="Total carbon footprint in kg CO₂")

    # Timestamp for when the record is created
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Carbon Record (Total: {self.total_carbon} kg CO₂)"
