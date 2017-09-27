import datetime
from django.utils import timezone
from ... import model

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return model.Question.objects.create(question_text=question_text, pub_date=time)
