from repo.base_service import BaseService
from repo.models import User, UserGroup


class UserService(BaseService):
    model = User


class UserGroupsService(BaseService):
    model = UserGroup

