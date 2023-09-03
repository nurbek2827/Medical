from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=128)


class Position(models.Model):
    name = models.CharField(max_length=128)


class Customusermanager(UserManager):
    def create_user(self, ):


class User(AbstractBaseUser, PermissionMixin):
    name = models.CharField("Ismi", max_length=128)
    surname = models.CharField("Familiyasi", max_length=128)
    phone = models.CharField("Tel:", max_length=128)
    profession = models.ForeignKey(Profession, verbose_name="Mutaxassisligi", on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, verbose_name="Lavozimi", on_delete=models.SET_NULL, null=True)
    img = models.ImageField("Rasmi", upload_to="doctor_img")
    info = models.TextField("Doctor haqida qisqacha")
    email = models.EmailField("Email manzili")
    gender = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1. Doctors"
        verbose_name = "Doctor"


class Doctime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    free = models.BooleanField(default=True)


class Services(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    icon = models.ImageField(upload_to="icon_img")


class Price(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    price = models.CharField(max_length=128)
    pr = models.IntegerField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        pr = self.price.replace(" ", "")
        for i in ["uzs", "usd", "rub"]:
            pr = pr.lower().replace(i, "")
        self.pr = int(pr)
        return super(Price, self).save(*args, **kwargs)
