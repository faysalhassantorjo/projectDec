from django.contrib import admin
from .models import Service,ServiceSection,ServiceRoom,RoomChat,RoomFile,UserProfile,IpModel

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceSection)
admin.site.register(ServiceRoom)
admin.site.register(RoomChat)
admin.site.register(RoomFile)
admin.site.register(UserProfile)
admin.site.register(IpModel)
