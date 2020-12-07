from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import uuid

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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES =((LOGIN_EMAIL, "email"),
    (LOGIN_GITHUB, "github"),
    (LOGIN_KAKAO, "kakao"))


    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=34, default="", blank=True)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex
            self.email_secret = secret
            send_mail(
                "Verify Airbnb Account",
                f'To verify your account click <a href="http://127.0.0.1:8000/users/verify/{secret}"',
                settings.EMAIL_HOST_PASSWORD,
                [self.email],
                fail_silently=False,
            )
        return

