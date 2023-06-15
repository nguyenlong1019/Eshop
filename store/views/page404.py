from django.shortcuts import render

def handling404(request, exception):
    return render(request, '404.html', {})