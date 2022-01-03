from user_model import UserModel

class UserService:
    def __init__(self):
        self.model=UserModel()

    def get_all(self):
        return self.model.get_all_users()

    def get_by_id(self, _id):
        return self.model.get_user_by_id(_id)

    def create(self,params):
        return self.model.create_user(params)

    def update(self, _id, params):
        return self.model.update_user(_id, params)

    def delete(self, _id):
        return self.model.delete_user_by_id(_id)
    