from django import forms

from ep_190623.my_music_app.models import Profile, Album


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            # 'genre': forms.Select(attrs={'placeholder': 'Select the genre'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    # !!! different
    def __set_hidden_fields(self):
        for name, field in self.fields.items():
            field.widget = forms.HiddenInput()

    # !!! different
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
