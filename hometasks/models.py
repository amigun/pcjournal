from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Subjects(models.Model):
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject


class HomeTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата')
    subject = models.ForeignKey('Subjects', on_delete=models.PROTECT, verbose_name='Предмет')
    homework = models.CharField(max_length=255, verbose_name='Домашнее задание')
    next_controlwork = models.IntegerField(default=0, verbose_name='Следующая к\р')


class Files(models.Model):
    title = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
