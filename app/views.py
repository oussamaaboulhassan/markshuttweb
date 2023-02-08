from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request=request, template_name="app/index.html")

def contact(request):
    return render(request=request, template_name="app/contact.html")