from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Choice
from .models import Question


def index(request):
    '''Return the last 5 published questions.'''

    # Do not include questions set to be published in the future
    questions = Question.objects \
        .filter(pub_date__lte=timezone.now()) \
        .order_by('-pub_date')[:5]

    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    '''Return a form for the user to vote on the question.'''

    # Exclude any questions that aren't published yet.
    queryset = Question.objects.filter(pub_date__lte=timezone.now())

    context = {
        'question': get_object_or_404(queryset, pk=question_id),
    }

    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    '''Receive a submitted form and record the vote for the question.'''

    # Exclude any questions that aren't published yet.
    queryset = Question.objects.filter(pub_date__lte=timezone.now())
    question = get_object_or_404(queryset, pk=question_id)

    try:
        choice = question.choices.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a choice.",
        })

    else:
        choice.votes += 1
        choice.save()

        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    '''Display the voting results for the question.'''

    # Exclude any questions that aren't published yet.
    queryset = Question.objects.filter(pub_date__lte=timezone.now())
    question = get_object_or_404(queryset, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})
