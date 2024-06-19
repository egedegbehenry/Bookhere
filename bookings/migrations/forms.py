from django import forms
from .models import Booking, Event

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email']

class EventForm(forms.ModelForm):
    class Meta:
        