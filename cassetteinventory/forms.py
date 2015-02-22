#Create the form class

from django.forms import ModelForm
from cassetteinventory.models import Tape, Artist, Label

class TapeForm(ModelForm):
    class Meta:
        model = Tape
        fields = '__all__'

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'