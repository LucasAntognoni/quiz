from uuid import uuid4
from datetime import datetime

from graphene import InputObjectType, Mutation, Field, String, Boolean, JSONString
from mongoengine import DoesNotExist

from models import Answer, Question, User
from types_ import AnswerType, QuestionType, UserType


class UserInput(InputObjectType):
    old_name = String()
    new_name = String()


class CreateUser(Mutation):
    user = Field(UserType)

    class Arguments:
        name = String(required=True)

    def mutate(self, info, name):
        user = User(
            name=name
        )
        user.save()

        return CreateUser(user=user)


class UpdateUser(Mutation):
    user = Field(UserType)

    class Arguments:
        data = UserInput(required=True)

    @staticmethod
    def get_object(name):
        return User.objects.get(name=name)

    def mutate(self, info, data):
        user = UpdateUser.get_object(data.old_name)
        user.name = data.new_name
        user.save()

        return UpdateUser(user=user)


class DeleteUser(Mutation):
    deleted = Boolean()

    class Arguments:
        name = String(required=True)

    def mutate(self, info, name):
        try:
            User.objects.get(name=name).delete()
            deleted = True
        except DoesNotExist:
            deleted = False

        return DeleteUser(deleted=deleted)


class QuestionInput(InputObjectType):
    text = String()
    choices = JSONString()


class CreateQuestion(Mutation):
    question = Field(QuestionType)

    class Arguments:
        data = QuestionInput(required=True)

    def mutate(self, info, data):
        question = Question(
            key=str(uuid4()),
            text=data.text,
            choices=data.choices
        )
        question.save()

        return CreateQuestion(question=question)


class UpdateQuestion(Mutation):
    question = Field(QuestionType)

    class Arguments:
        key = String()
        data = QuestionInput(required=True)

    @staticmethod
    def get_object(key):
        return Question.objects.get(key=key)

    def mutate(self, info, key, data):
        question = UpdateQuestion.get_object(key)

        if data.text:
            question.text = data.text
        if data.choices:
            question.choices = data.choices

        question.save()

        return UpdateQuestion(question=question)


class DeleteQuestion(Mutation):
    deleted = Boolean()

    class Arguments:
        key = String(required=True)

    def mutate(self, info, key):
        try:
            Question.objects.get(key=key).delete()
            deleted = True
        except DoesNotExist:
            deleted = False

        return DeleteQuestion(deleted=deleted)


class AnswerInput(InputObjectType):
    choice = String()
    question = String()
    submitted_by = String()


class CreateAnswer(Mutation):
    answer = Field(AnswerType)

    class Arguments:
        data = AnswerInput(required=True)

    @staticmethod
    def get_question_object(key):
        return Question.objects.get(key=key)

    @staticmethod
    def get_user_object(name):
        return User.objects.get(name=name)

    def mutate(self, info, data):

        user = CreateAnswer.get_user_object(data.submitted_by)
        question = CreateAnswer.get_question_object(data.question)

        answer = Answer(
            key=str(uuid4()),
            choice=data.choice,
            question=question,
            submitted_by=user
        )
        answer.save()

        return CreateAnswer(answer=answer)


class UpdateAnswer(Mutation):
    answer = Field(AnswerType)

    class Arguments:
        key = String()
        choice = String()

    @staticmethod
    def get_object(key):
        return Answer.objects.get(key=key)

    def mutate(self, info, key, choice):
        answer = UpdateAnswer.get_object(key)

        if choice:
            answer.choice = choice

        answer.updated_at = datetime.now()
        answer.save()

        return UpdateAnswer(answer=answer)


class DeleteAnswer(Mutation):
    deleted = Boolean()

    class Arguments:
        key = String(required=True)

    def mutate(self, info, key):
        try:
            Answer.objects.get(key=key).delete()
            deleted = True
        except DoesNotExist:
            deleted = False

        return DeleteAnswer(deleted=deleted)
