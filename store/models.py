from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# validatorsの設定
def check_age(value):
    if value < 10 or value > 100:
        raise ValidationError('10〜100歳が範囲です')


# validatorsの設定
def check_weight(value):
    if value < 10 or value > 200:
        raise ValidationError('10から200kgの値を入れてください')


class Member(models.Model):
    day = models.DateTimeField(default=timezone.now)
    weight = models.IntegerField(default=0, validators=[check_age])
    fat_percentage = models.IntegerField(default=0)



