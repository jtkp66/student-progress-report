from django.shortcuts import render


def index(request):

    return render(request, 'surveys/surveys.html')


def surveys(request):

    return render(request, 'surveys/surveys.html')
