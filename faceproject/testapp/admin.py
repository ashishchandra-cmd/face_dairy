from django.contrib import admin
from testapp.models import face
# Register your models here.
class Adminface(admin.ModelAdmin):
    list_display=['title','body','img','publish']
admin.site.register(face ,Adminface)