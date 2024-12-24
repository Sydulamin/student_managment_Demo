from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
<<<<<<< HEAD
    image = models.ImageField(upload_to='profile_image/', default='def.png', max_length=255, null=True, blank=True)
=======
    image = models.ImageField(upload_to='profile_image/', default='def.png',max_length=255, null=True, blank=True)
>>>>>>> 5b4fadeb83ccad2dcf8c139071b63e812db12624
    otp = models.PositiveIntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


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


class Counter(models.Model):
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)
<<<<<<< HEAD


class address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    house_no = models.TextField(null=True, blank=True)
    road_no = models.TextField(null=True, blank=True)
    thana = models.TextField(null=True, blank=True)
    post_code = models.PositiveIntegerField(null=True, blank=True)
    district = models.TextField(null=True, blank=True)
    division = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}"s Address'
=======
>>>>>>> 5b4fadeb83ccad2dcf8c139071b63e812db12624
