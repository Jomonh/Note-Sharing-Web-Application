from django.contrib import admin
from .models import semFour,semOne,semThree,semTwo,notificationsLive
# Register your models here.

class adminOrdering(admin.ModelAdmin):
    model = semOne,semTwo,semThree,semFour
    list_display = ['select_sub', 'module_name','pdf_module']

    def get_name(self, obj):
        return obj.author.name

class notiOrdering(admin.ModelAdmin):
    model = notificationsLive
    list_display = ['title', 'dt']

    def get_name(self, obj):
        return obj.author.name

admin.site.register(semOne, adminOrdering)
admin.site.register(semTwo, adminOrdering)
admin.site.register(semThree, adminOrdering)
admin.site.register(semFour, adminOrdering)

admin.site.register(notificationsLive,notiOrdering)
