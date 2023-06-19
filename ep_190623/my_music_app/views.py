from django.shortcuts import render, redirect

from ep_190623.my_music_app.forms import AddProfileForm, AddAlbumForm, DeleteProfileForm, DeleteAlbumForm
from ep_190623.my_music_app.models import Album, Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index_with_profile(request):
    template = 'home-with-profile.html'

    # redirect if no profile
    profile = get_profile()
    if profile is None:
        return redirect('index no profile')
    # -----------------------

    all_objects = Album.objects.all()

    context = {
        'all_objects': all_objects,
    }
    return render(request, template, context)


def index_no_profile(request):
    template = 'home-no-profile.html'

    # just on case ----------
    if get_profile() is not None:
        return redirect('index with profile')
    # -----------------------

    if request.method == 'POST':
        form = AddProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddProfileForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def add_album(request):
    template = 'add-album.html'

    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddAlbumForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def album_details(request, pk):
    template = 'album-details.html'
    current_object = Album.objects.get(pk=pk)

    context = {
        'current_object': current_object,
    }
    return render(request, template, context)


def edit_album(request, pk):
    template = 'edit-album.html'
    current_object = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddAlbumForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddAlbumForm(instance=current_object)

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)


def delete_album(request, pk):
    template = 'delete-album.html'
    current_object = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = DeleteAlbumForm(instance=current_object)

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)


def profile_details(request):
    template = 'profile-details.html'
    profile = get_profile()

    # get the albums for this profile
    albums_count = Album.objects.all().count()

    context = {
        'current_object': profile,
        'albums_count': albums_count,
    }
    return render(request, template, context)


def delete_profile(request):
    template = 'profile-delete.html'
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index no profile')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'current_object': profile,
    }
    return render(request, template, context)
