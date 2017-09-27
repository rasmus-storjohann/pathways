from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .. import models

def vote(post_request, question_id):
    question = get_object_or_404(models.Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = post_request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(post_request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        # race condition here
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
