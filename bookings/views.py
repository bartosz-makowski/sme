from django.shortcuts import render


def bookings(request):
    """A view that displays booking
    page where a client can choose time
    and date of their appointment """

    return render(request, 'bookings/bookings.html')
