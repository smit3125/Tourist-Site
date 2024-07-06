from django.shortcuts import render
from django.http import HttpResponse
from homepage.form import UserSignupForm
from homepage.models import place
from django.conf import settings
from .models import place

# Create your views here.
def home(request):
    return render(request,'home.html')
def cart(request):
    return render(request,'cart.html')
def blog(request):
    return HttpResponse(request,'blog.html')
def about(request):
    return render(request,'about.html')

# def explorenearplaces(request):
#     data_from_database = place.objects.all()
#     return render(request, 'explorenearplaces.html', {'data_from_database': data_from_database})


def explorenearplaces(request):
    places_with_images = []
    data_from_database = place.objects.all()
    for place_obj in data_from_database:
        place_data = {
            'place_name': place_obj.place_name,
            'place_type': place_obj.place_type,
            'address': place_obj.address,
            'pin_code': place_obj.pin_code,
            'official_site_link' : place_obj.official_site_link,
            'ticket_price': place_obj.ticket_price,
            'description': place_obj.description,
            'open_time': place_obj.open_time,
            'close_time': place_obj.close_time,

            'image_url': None  # Placeholder for the image URL
            
        }
        if place_obj.image:  # Check if the place has an associated image
            # Construct the image URL using MEDIA_URL and the image filename
            place_data['image_url'] = settings.MEDIA_URL + str(place_obj.image)
        places_with_images.append(place_data)
        

    return render(request, 'explorenearplaces.html', {'places_with_images': places_with_images})



#------------LOGIN & SIGN UP FUNCTION--------------------------------------------------------------
# LOGIN / SIGN UP

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if pass1!=pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
#         else:

#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')
        
def SignupPage(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})       



    # return render (request,'signup.html')

def LoginPage(request):
    if  request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')




# ----------------------- CART -------------------------

# views.py

from django.shortcuts import render, redirect
from .models import place, Cart

def place_list(request):
    places = place.objects.all()
    return render(request, 'explorenearplaces.html', {'places': places})

def add_to_cart(request, place_pid):
    if request.method == 'POST':
        selected_places = request.POST.getlist('selected_places')
        
        # Create a new Cart object
        cart = Cart.objects.create()
        
        # Save selected places to the cart
        cart.places.add(selected_places)
        cart.places.add(place_pid)
    return redirect('cart')
      # Assuming you have a view named 'cart_view'
    
    
def remove_from_cart(request, place_pid):
    # Place = place.objects.get(id=place_pid)
    if request.method == 'POST':
        Place = request.POST.getlist('Place')
    cart = Cart.objects.first()  # Assuming there's only one cart for simplicity
    cart.places.remove(Place)
    return redirect('cart')

def cart(request):
    cart = Cart.objects.first()  # Assuming there's only one cart for simplicity
    return render(request, 'cart.html', {'cart': cart})












