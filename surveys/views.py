from django.shortcuts import render

from .models import Survey


def index(request):
    surveys = Survey.objects.all()

    context = {
        'surveys': surveys
    }

    return render(request, 'surveys/survey.html', context)


def survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)

    context = {
        'survey': survey
    }

    return render(request, 'surveys/survey.html', context)


def surveys(request):

    return render(request, 'surveys/surveys.html')
