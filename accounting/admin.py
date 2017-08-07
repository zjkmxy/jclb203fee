from django.contrib import admin
from accounting.models import Category, Label, Trade

# Register your models here.
admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Trade)