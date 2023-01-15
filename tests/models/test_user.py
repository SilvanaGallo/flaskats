import pytest
from flaskats.models import User


class TestUser:

    @pytest.mark.unit
    def test_user_creation_and_print(self):
        created_user = User(username="Silvana Gallo",
                              email="mail@gmail.com",
                              password="123456")
        str_version = str(created_user)
        assert "User" in str_version
        assert created_user.email in str_version
        assert created_user.username in str_version


    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)
