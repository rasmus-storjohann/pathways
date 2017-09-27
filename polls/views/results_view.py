from django.views import generic
from .. import model

class ResultsView(generic.DetailView):
    model = model.Question
    template_name = 'polls/results.html'
