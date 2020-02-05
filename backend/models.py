from uuid import uuid4
from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField, DictField, StringField, ReferenceField


class User(Document):
    name = StringField()
    meta = {'collection': 'user'}


class Question(Document):
    key = StringField(default=str(uuid4()))
    text = StringField()
    choices = DictField()
    meta = {'collection': 'question'}


class Answer(Document):
    choice = StringField()
    question = ReferenceField(Question)
    submitted_by = ReferenceField(User)
    submitted_at = DateTimeField(default=datetime.now())

    meta = {'collection': 'answer'}
