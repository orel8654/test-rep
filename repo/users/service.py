from repo.base_service import BaseService
from repo.models import User


class UserService(BaseService):
    model = User

