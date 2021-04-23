from django.shortcuts import render

def deals(request):
    """A view to display deals page """
    return render(request, 'deals/deals.html')
