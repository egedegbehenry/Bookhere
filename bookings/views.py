from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def my_blog(request):
return HttpResponse("Hello, Blog!")

@login_required
def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Check for existing bookings
            if Booking.objects.filter(event=event, guest_email=booking.guest_email).exists():
                messages.error(request, 'You have already booked this event.')
            else:
                booking.event = event
                booking.save()
                messages.success(request, 'Booking successful!')
                return redirect('event_detail', pk=event.pk)
    else:
        form = BookingForm()
    return render(request, 'events/book_event.html', {'form': form, 'event': event})