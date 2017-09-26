import os
import sys

# TODO make this into a function call
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import polls

# in each test file do
# from .context import polls

# An application may use common Django conventions, such as having models, tests,
# urls, and views submodules. Test files by default are test*.py, so test files 
# can be placed next to the files they test.

# polls
# polls/urls.py
# polls/views/detail_view.py contains DetailView
# polls/models/question.py contains Question
# polls/tests/urls/test_foo.py
# polls/tests/views/test_question_detail_view.py contains TestQuestionDetailView
# polls/tests/models/test_question.py
