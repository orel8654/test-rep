from repo.base_service import BaseService
from repo.models import User, UserGroup, UserSending


class UserService(BaseService):
    model = User


class UserGroupsService(BaseService):
    model = UserGroup


class UserSendingService(BaseService):
    model = UserSending

