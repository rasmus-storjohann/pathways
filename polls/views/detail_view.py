from django.views import generic
from django.utils import timezone
from .. import model

class DetailView(generic.DetailView):
    model = model.Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return model.Question.objects.filter(pub_date__lte = timezone.now())
