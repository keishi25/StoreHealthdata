from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# validatorsの設定
def check_age(value):
    if value < 10 or value > 100:
        raise ValidationError('10〜100歳が範囲ですよ!')


class Member(models.Model):
    day = models.DateTimeField(default=timezone.now)
    weight = models.IntegerField(default=0)
    fat_percentage = models.IntegerField(default=0)

    """
    original　
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100,
                                validators=[MinLengthValidator(5, '5文字以上です！'),
                                            RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！')])
    age = models.IntegerField(
        default=0, validators=[check_age])
    """

