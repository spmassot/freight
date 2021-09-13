from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class User(Model):
    class Meta:
        table_name = 'voxx-users'
        region = 'us-east-1'
        read_capacity_units = 1
        write_capacity_units = 1

    username = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()

    @classmethod
    def is_valid_user(cls, username):
        if cls.get(username):
            return True
        else:
            return False

    @classmethod
    def is_valid_login(cls, username, password):
        try:
            user = cls.get(username)
            if user.password == password:
                return True
        except User.DoesNotExist as e:
            pass
        except:
            pass
        return False

    @classmethod
    def initialize_users(cls):
        if not cls.exists():
            cls.create_table()
