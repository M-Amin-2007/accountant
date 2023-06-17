from django.shortcuts import render

# Create your views here.
def home(request):
    """home view."""
    return render(request, "main/home.html")
