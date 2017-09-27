from django.shortcuts import get_object_or_404
from .. import models

class ChoiceRepository:
    def get_choice_by_question_id_and_choice_id(self, question_id, choice_id):
        question = get_object_or_404(models.Question, pk = question_id)
        return question.choice_set.get(pk = choice_id)

    # TODO assuming argument is the right type here...
    def save_choice(self, choice):
        choice.save()
