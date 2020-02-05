from graphene import InputObjectType, Mutation, Field, String, Boolean
from mongoengine import DoesNotExist

from models import Answer, Question, User
from types_ import UserType


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
