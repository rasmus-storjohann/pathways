# An application may use common Django conventions, such as having models, tests,
# urls, and views submodules. Test files by default are test*.py, so test files 
# can be placed next to the files they test.

# polls
# polls/urls.py
# polls/views/detail_view.py contains DetailView
# polls/models/question.py contains Question
# polls/tests/views/test_question_detail_view.py contains TestQuestionDetailView
# polls/tests/models/test_question.py

from django.conf.urls import url

from .views import IndexView
from .views import DetailView
from .views import ResultsView
from .views import vote

# TODO rework it so that the namespaces are included below, so views.IndexView.as_view()
app_name = 'polls'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]
