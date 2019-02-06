from django.shortcuts import render, redirect

from .models import TravelEntry

from .forms import EntryForm

def index(request):

	entries = TravelEntry.objects.order_by("-id")

	context = {"entries" : entries}

	return render(request, "travel_entries/index.html", context)

def add(request):

	form = EntryForm(request.POST)

	if form.is_valid():
		new_entry = form.save()
		return redirect('index')

	context = {"form": form}

	return render(request, "travel_entries/add.html", context)	