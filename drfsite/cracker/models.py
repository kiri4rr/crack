from django.db import models


# Create your models here.
class Cracker(models.Model):
    question_id = models.CharField(max_length=255)
    question = models.TextField(blank=True)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    answer_5 = models.CharField(max_length=255)
    true_answer = models.CharField(max_length=255)
    picture = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.question


class Category(models.Model):
    picture = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.picture


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.login