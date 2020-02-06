from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

from models import User, Question, Answer


class UserType(MongoengineObjectType):

    class Meta:
        model = User
        interfaces = (Node,)


class QuestionType(MongoengineObjectType):

    class Meta:
        model = Question
        interfaces = (Node,)


class AnswerType(MongoengineObjectType):

    class Meta:
        model = Answer
        interfaces = (Node,)
