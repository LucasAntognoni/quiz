from graphene import ObjectType, Schema
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField

from types_ import AnswerType, QuestionType, UserType
from mutations import CreateUser, UpdateUser, DeleteUser, \
                      CreateQuestion, UpdateQuestion, DeleteQuestion,\
                      CreateAnswer, UpdateAnswer, DeleteAnswer


class Mutations(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_question = CreateQuestion.Field()
    update_question = UpdateQuestion.Field()
    delete_question = DeleteQuestion.Field()

    create_answer = CreateAnswer.Field()
    update_answer = UpdateAnswer.Field()
    delete_answer = DeleteAnswer.Field()


class Query(ObjectType):
    node = Node.Field()

    user = Node.Field(UserType)
    question = Node.Field(QuestionType)
    answer = Node.Field(AnswerType)

    all_users = MongoengineConnectionField(UserType)
    all_questions = MongoengineConnectionField(QuestionType)
    all_answers = MongoengineConnectionField(AnswerType)


schema = Schema(
    query=Query,
    mutation=Mutations,
    types=[AnswerType, QuestionType, UserType]
)
