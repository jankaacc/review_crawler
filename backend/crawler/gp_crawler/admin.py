from django.contrib import admin

from crawler.gp_crawler.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "score")
