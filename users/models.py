from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ CustomeUserModel """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDLER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDLER_OTHER, "Other"),
    )

    LANGUAGE_ENGLUSH = "eng"
    LANGUAGE_KOREAN = "kor"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLUSH, "eng"), (LANGUAGE_KOREAN, "kor"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_KRW, "KRW"), (CURRENCY_USD, "USD"))
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)