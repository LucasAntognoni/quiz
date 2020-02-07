from graphene import ObjectType, Schema, Field, ID
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
    id = ID(required=True)
    node = Node.Field()
    viewer = Field(lambda: Query)

    user = Node.Field(UserType)
    question = Node.Field(QuestionType)
    answer = Node.Field(AnswerType)

    all_users = MongoengineConnectionField(UserType)
    all_questions = MongoengineConnectionField(QuestionType)
    all_answers = MongoengineConnectionField(AnswerType)

    def resolve_viewer(self, args, context, info):
        return info.parent_type

    def resolve_id(self, args, context, info):
        return 1

    class Meta:
        interfaces = (Node,)


schema = Schema(
    query=Query,
    mutation=Mutations,
    types=[AnswerType, QuestionType, UserType]
)
