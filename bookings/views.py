from django.shortcuts import render

from .models import Day, Time


def bookings(request):
    """A view that displays booking
    page where a client can choose time
    and date of their appointment """
    days = Day.objects.all()

    context = {
        'days': days
    }

    return render(request, 'bookings/bookings.html',context)
