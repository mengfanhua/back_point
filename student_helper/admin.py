from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.Users)  # models 中你要注册的表 不注册不会显示
admin.site.register(models.ClassPlan)
