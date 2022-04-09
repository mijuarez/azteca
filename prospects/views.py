from django.shortcuts import render

# Create your views here.

def prospects_list(request):
    return render(request, 'prospects/prospects_list.html', {})