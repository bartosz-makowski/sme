from django.shortcuts import render


def basket(request):
    """A view to display basket page """

    return render(request, 'basket/basket.html')
