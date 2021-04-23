from django.shortcuts import render
from .models import Deal


def deals(request):
    """A view to display deals page """

    deals = Deal.objects.all()

    context = {
        'deals': deals,
    }
    return render(request, 'deals/deals.html', context)
