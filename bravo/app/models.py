from django.db import models
from django.contrib.auth.models import User
import uuid

from taggit.managers import TaggableManager
from django.utils.timezone import now

# Create your models here.

class IpModel(models.Model):
    ip=models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    bio=models.TextField()
    profile_picture=models.ImageField(upload_to='user_profile_picture/')
    expart_at=models.CharField(max_length=20,null=True,blank=True)
    seller=models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url=self.profile_picture.url
        except:
            url=''
        return url
    def __str__(self) -> str:
        return str(self.user)


class Service(models.Model):
    service_name=models.CharField(max_length=100)
    iconLink=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.service_name)


class ServiceSection(models.Model):
    creator=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    service_name=models.ForeignKey(Service,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    service_tags=models.CharField(max_length=200,blank=True,null=True)
    bannerPicture=models.ImageField(upload_to='banner/',blank=True,null=True)
    user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
    views = models.ManyToManyField(IpModel,related_name='post_views', blank=True)
    timestamp = models.DateTimeField(default=now, blank=True)
    tags = TaggableManager()

    @property
    def imageURL(self):
        try:
            url=self.bannerPicture.url
        except:
            url=''
        return url
    def __str__(self):
        return str(self.creator)
    
    def total_views(self):
        return self.views.count()
    
class ServiceRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(ServiceSection, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_servicerooms')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_servicerooms')

    def __str__(self):
        return str(self.id)


class RoomChat(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='host')
    creator=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creator')
    message=models.TextField()
    roomId=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.message



class RoomFile(models.Model):
    ServiceRoom=models.ForeignKey(ServiceRoom,on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='uploads/')
    sendby=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.sendby
    
    def file_name(self):
        main_file=str(self.file)
        outputfile=main_file.replace('uploads/','')
        return outputfile
    
    def __str__(self) -> str:
        return str(self.sendby)
