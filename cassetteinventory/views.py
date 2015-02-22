from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from cassetteinventory.forms import TapeForm, ArtistForm, LabelForm
from cassetteinventory.models import Artist, Tape, Label

# Create your views here.
# This the intermediate between the input data and the display information - think "controller"

def ViewTapes(request):
    tapes = Tape.objects.all()
    template = loader.get_template('ViewTapesTemplate.html')
    context = RequestContext(request, {'listOfTapes':tapes})
    return HttpResponse(template.render(context))

def AddTapeView(request):
    if request.method == 'POST':
        form = TapeForm(request.POST)

        if form.is_valid():
            #add form processing
            tape = Tape.objects.create(title=form.cleaned_data['title'], year=form.cleaned_data['year'])
            tape.artists.add(*form.cleaned_data['artists'])
            tape.labels.add(*form.cleaned_data['labels'])
            return HttpResponse("Hi bitch")
    else:
        form = TapeForm()

    return render(request, 'AddTapeTemplate.html', {'form':form})

def AddArtistView(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            #add form processing
            artist = Artist()
            artist.artistname = form.cleaned_data['artistname']
            artist.save()
            return HttpResponse("Hi bitch")
    else:
        form = ArtistForm()

    return render(request, 'AddArtistTemplate.html', {'form':form})


def AddLabelView(request):
    if request.method == 'POST':
        form = LabelForm(request.POST)

        if form.is_valid():
            #add form processing
            label = Label()
            label.labelname = form.cleaned_data['labelname']
            label.save()
            return HttpResponse("Hi bitch")
    else:
        form = LabelForm()

    return render(request, 'AddLabelTemplate.html', {'form':form})