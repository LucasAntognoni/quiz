from graphene import Field, ObjectType, Schema

from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import User as UserModel
from models import Question as QuestionModel
from models import Answer as AnswerModel


class User(MongoengineObjectType):

    class Meta:
        model = UserModel
        interfaces = (Node,)


class Question(MongoengineObjectType):

    class Meta:
        model = QuestionModel
        interfaces = (Node,)


class Answer(MongoengineObjectType):

    class Meta:
        model = AnswerModel
        interfaces = (Node,)


class Query(ObjectType):
    node = Node.Field()

    user = Node.Field(User)
    question = Node.Field(Question)
    answer = Node.Field(Answer)

    all_users = MongoengineConnectionField(User)
    all_questions = MongoengineConnectionField(Question)
    all_answers = MongoengineConnectionField(Answer)


schema = Schema(
    query=Query,
    types=[User, Question, Answer]
)
