from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models import Count
from urllib.parse import urlencode
from django.urls import reverse
from django.utils.html import format_html
from .models import Category, Product, Promotion, Comment, Order, OrderItem
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "title")

    # def products_c(self, obj):
    #     product_counts = obj.products.count()
    #     url = (reverse("admin:store_product_changelist")
    #                     + "?"
    #                     + urlencode({"category": str(obj.id)}))
    #     return format_html(
    #         '<a href="{}">{} products</a>', url, product_counts

    #     )


@admin.register(Promotion)
class AdminPromotion(admin.ModelAdmin):
    list_display = ("id", "discount",)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("id", "title", "get_categories", "promotion",
                    "price", "final_price", "is_active", "comments")
    list_select_related = ("promotion",)

    def get_categories(self, obj):
        return ", ".join([str(item) for item in obj.categories.all()])

    def final_price(self, obj):
        return f"{((1 - ((obj.promotion and obj.promotion.discount )or 0)) * obj.price):.0f}"

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("categories").prefetch_related("comments")

    def comments(self, obj):
        comment_count = obj.comments.count()
        url = (reverse("admin:store_comment_changelist")
               + "?"
               + urlencode({"product": str(obj.id)}))
        return format_html(
            '<a href="{}">{} comments</a>', url, comment_count

        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "text", "created", "is_show")


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "shipping", "created", "is_delivered")
    inlines = (OrderItemInline, )
