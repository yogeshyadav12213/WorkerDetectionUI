from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
import json
from .models import Camera


# --- Public Views ---

def landing_view(request):
    if request.user.is_authenticated:
        return redirect('overview')
    return render(request, 'landing.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('overview')

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('overview')
        else:
            error_message = "Invalid username or password."

    context = {
        'form_type': 'login',
        'error_message': error_message
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('overview')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('overview')
    else:
        form = CustomUserCreationForm()

    context = {
        'form_type': 'signup',
        'form': form
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('landing')


# --- Protected Dashboard Views ---

@login_required(login_url='/login/')
def overview_view(request):
    return render(request, 'overview.html')


@login_required(login_url='/login/')
def camera_management_view(request):
    cameras = Camera.objects.all()
    cameras_list = []
    for cam in cameras:
        cameras_list.append({
            "id": cam.id,
            "camera_id": cam.camera_id,
            "name": cam.name,
            "ip": cam.stream_url,
            "status": cam.status,
            "resolution": cam.resolution,
            "fps": str(cam.fps)
        })

    cameras_json = json.dumps(cameras_list)

    context = {
        'cameras_json': cameras_json,
    }
    return render(request, 'camera_management.html', context)


@login_required(login_url='/login/')
def zone_configuration_view(request):
    return render(request, 'zone_configuration.html')


@login_required(login_url='/login/')
def reports_view(request):
    return render(request, 'reports.html')


@login_required(login_url='/login/')
def data_archive_view(request):
    # This view will render your new data archive page
    return render(request, 'data_archive.html')


@login_required(login_url='/login/')
def placeholder_view(request):
    # This view is for links that are not yet created
    return render(request, 'overview.html')
