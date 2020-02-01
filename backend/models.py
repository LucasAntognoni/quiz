from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField, DictField, ListField, StringField, ReferenceField


class User(Document):
    name = StringField()
    meta = {'collection': 'user'}


class Question(Document):
    text = StringField()
    choices = DictField()
    meta = {'collection': 'question'}


class Answer(Document):
    choice = StringField()
    question = ReferenceField(Question)
    submitted_by = ReferenceField(User)
    submitted_at = DateTimeField(default=datetime.now())

    meta = {'collection': 'answer'}


