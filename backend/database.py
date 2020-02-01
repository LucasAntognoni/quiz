from mongoengine import connect
from models import Answer, Question, User

connect('quiz', host='mongomock://localhost')


def create_db():

    question = Question(
        text="Who is you father?",
        choices={
            "A": "Darth Vader",
            "B": "Emperor",
            "C": "Bail Organa",
            "D": "Obi-Wan Kenobi",
            "E": "None of the above"
        }
    )
    question.save()

    luke = User(name='Luke')
    luke.save()

    luke_answer = Answer(
        choice="A",
        question=question,
        submitted_by=luke
    )
    luke_answer.save()

    leia = User(name='Leia')
    leia.save()

    leia_answer = Answer(
        choice="C",
        question=question,
        submitted_by=leia
    )
    leia_answer.save()

