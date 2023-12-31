from django.shortcuts import render,HttpResponse,redirect
from .models import Service,ServiceSection,ServiceRoom,RoomChat,RoomFile,UserProfile,IpModel
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def home(request):
    all_service=Service.objects.all()

    user=request.user
    user_profile=[]
    if user.is_authenticated:
        user_profile = get_object_or_404(UserProfile,user=user)



    context={
        'all_service':all_service,
        'seller':user_profile.seller if user_profile else None
    }
    return render(request,'app/home.html',context)

def search_posts(request):
    query = request.GET.get('q')
    section = []

    if query:
        # __unaccent__lower__trigram_similar
        section = ServiceSection.objects.filter(Q(tags__name__icontains=query))


    context = {'query': query, 'section': section}
    return render(request, 'app/searched.html', context)

def services(request,pk):
    service=Service.objects.get(id=pk)
    section=ServiceSection.objects.filter(service_name=service)
    context={
        'section':section,
        'service':service
    }
    return render(request,'app/category.html',context)


def viewDetails(request,pk):
    context={
        'id':pk
    }
    return render(request,'app/banner-details.html',context)

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def createRoom(request,pk):
    service=ServiceSection.objects.get(id=pk)
    print(request.user)
    room=ServiceRoom.objects.create()
    
    room.creator=service.creator
    room.client=request.user
    room.service=service
    room.save()
    return redirect('viewRoom',pk=room.id)

from .form import LoginForm,YourModelForm,ProfileField
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})

def logoutV(request):
    logout(request)
    return redirect('home')

def profile(request,pk):
    user=User.objects.get(id=pk)
    
    user_profile,created=UserProfile.objects.get_or_create(user=user)
    services=ServiceSection.objects.filter(creator=user)

    createdRoom=ServiceRoom.objects.filter(creator=user)
    x=ServiceRoom.objects.filter(client=user)
    print(request.user)
    print(user)
    context={
        'username':user,
        'services':services,
    
        'your_room':createdRoom,
        'x':x,
        'profile_picture':user_profile.imageURL,
        'bio':user_profile.bio,
        'expart':user_profile.expart_at
    }
    return render(request,'app/profile.html',context)

def viewRoom(request,pk):
    room=ServiceRoom.objects.get(id=pk)
    messages=RoomChat.objects.filter(roomId=room.id)

    
    for message in messages:
        print('message: ',message.message)

 

    room_file=RoomFile.objects.filter(ServiceRoom=room)
    
    for i in room_file:
        print(i.file_name())
   
    context={
        'creator':room.creator,
        'service_name':room.service,
        'name':room.service.service_name,
        'room_id':room.id,
        'messages':messages,
    
        'room_file':room_file,

    }
    
    return render(request,'app/room.html',context)

from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            return redirect('/')  
    else:
        form = UserCreationForm()

    return render(request, 'app/register.html', {'form': form})


def upload_file(request,pk):
    room=ServiceRoom.objects.get(id=pk)
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            
           
            room_file=RoomFile.objects.create(ServiceRoom=room,sendby=request.user)
            room_file.file = form.cleaned_data['file'] 
            room_file.save()
            return redirect('viewRoom',pk=pk)
       
    else:
        form = YourModelForm()
    context={
        'room_id':pk,
        'form':form
    }
    return render(request, 'app/upload_file.html', context)

from django.shortcuts import get_object_or_404


def download_file(request, pk):

    my_model_instance = get_object_or_404(RoomFile, pk=pk)


    with my_model_instance.file.open('rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={my_model_instance.file.name}'

    return response


def updateProfile(request,pk):
    user=User.objects.get(id=pk)
    user_profile = get_object_or_404(UserProfile,user=user)

    if request.method == 'POST':
        form = ProfileField(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
    else:
        form = ProfileField(instance=user_profile)

    context = {
        'form': form,
        'id': pk,
    }
    return render(request, 'app/updateProfile.html', context)


from .form import SellerField,Dashboard

def createSeller(request,pk):
    user=User.objects.get(id=pk)
    user_profile = get_object_or_404(UserProfile,user=user)

    if request.method == 'POST':
        form = SellerField(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SellerField(instance=user_profile)
    
    context={
        'form':form
    }

    return render(request,'app/room_info.html',context)

from .form import Dashboard

def dashboard(request, pk):
    user=User.objects.get(id=pk)
    user_profile = get_object_or_404(UserProfile,user=user)
    services=ServiceSection.objects.filter(creator=user)



    if request.method == 'POST':
        form = Dashboard(request.POST, request.FILES)
        if form.is_valid():
            service_section = form.save(commit=False)
            service_section.user = user_profile
            service_section.creator = user 
            service_section.save()
            return redirect('dashboard',pk=pk)
    else:
        form = Dashboard()

    context = {
        'form': form,
        'section':services
    }
    return render(request, 'app/dashboard.html', context)


def deleteBanner(request,pk):
    userid=request.user.id
    banner=ServiceSection.objects.get(id=pk)
    bannersRoom=ServiceRoom.objects.filter(service=banner)
    bannersRoom.delete()
    banner.delete()

    return redirect('dashboard',pk=userid)

from django.views.generic import DetailView

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip

class PostDetailView(DetailView):
    model=ServiceSection
    context_object_name = 'post'
    template_name='app/pricing.html'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object
        context = self.get_context_data(object=self.object)
        ip=get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            print("ip is already present")
            service_id= request.GET.get('service-id')
            print('post id',service_id)

            service = ServiceSection.objects.get(id=service_id)

            service.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            service_id=request.GET.get('service-id')
            service = ServiceSection.objects.get(id=service_id)
            service.views.add(IpModel.objects.get(ip=ip))
        
        return self.render_to_response(context)
