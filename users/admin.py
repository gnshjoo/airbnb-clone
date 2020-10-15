from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from rooms/models import models as room_models
from . import models


# class PhotoInline(admin.StackedInline):
#     model = room_models.Photo


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    # inlines = (PhotoInline, )

    list_filter = UserAdmin.list_filter + (
        "currency",
        "superhost",
        "language"
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "gender",
        "language",
        "currency",
        "is_staff",
        "is_superuser",
    )