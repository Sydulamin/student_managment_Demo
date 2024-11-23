from django.db import models


# Create your models here.

class Main_test(models.Model):
    Father_name = models.CharField(max_length=10)
    Mother_name = models.CharField(max_length=10)
    Nationality = models.CharField(max_length=10)

    def __str__(self):
        return self.Father_name


class test_table(models.Model):
    CHOICE = [
        ('Male', 'Male',),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    name = models.CharField(max_length=10)
    parents = models.ForeignKey(Main_test, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(choices=CHOICE, default='Female', max_length=6)

    def __str__(self):
        if not self.parents:
            return self.name
        else:
            return f"{self.parents.Father_name}'s Sons and nationality is {self.parents.Nationality} "
