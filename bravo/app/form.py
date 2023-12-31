from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import RoomFile, UserProfile,ServiceSection

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class YourModelForm(forms.ModelForm):
    class Meta:
        model = RoomFile
        fields = ['file']

class ProfileField(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

class SellerField(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'expart_at', 'seller']

class Dashboard(forms.ModelForm):
    class Meta:
        model = ServiceSection
        fields = ['service_name','bannerPicture','description','tags']
