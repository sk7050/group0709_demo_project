from django.db import models

# Create your models here.

class Occupations(models.Model):
    Occupation_Name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Occupation_Name

class Info_Class(models.Model):
  Name=models.CharField(max_length=50)
  Phone=models.CharField(max_length=14)
  SSC_Roll_No=models.IntegerField()
  SSC_Board=models.CharField(max_length=20)
  Email=models.EmailField()
  Blood_Group=models.CharField(max_length=3)
  Occupation=models.ForeignKey(Occupations, on_delete=models.CASCADE)
  Address=models.TextField(max_length=500)
  def __str__(self):
    return self.Name
