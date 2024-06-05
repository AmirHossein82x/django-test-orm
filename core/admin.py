from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import User, Profile, City
from urllib.parse import urlencode
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.







class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


@admin.register(User)
class AdminUser(UserAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email", "comments")
    inlines = (ProfileInline,)

    def comments(self, obj):
        comment_count = obj.comments.count()
        url = (reverse("admin:store_comment_changelist")
                        + "?" 
                        + urlencode({"user": str(obj.id)}))
        return format_html(
            '<a href="{}">{} comments</a>', url, comment_count

        )
    

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("comments")



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "users")


    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("profiles")


    def users(self, obj):
        user_count = obj.profiles.count()
        return user_count