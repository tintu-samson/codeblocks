from django.contrib import admin
from .models import Domain,Events,Topic,Message,Room
# Register your models here.
admin.site.register(Domain)
admin.site.register(Events)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Room)
