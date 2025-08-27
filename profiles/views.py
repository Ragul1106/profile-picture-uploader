from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm()
    profiles = UserProfile.objects.all()
    return render(request, 'profiles/profile.html', {'form': form, 'profiles': profiles})
