from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class Authen(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        print(username)
        UserModoel=get_user_model()
        try:
            user=UserModoel.objects.get(username = username)
        except UserModoel.DoesNotExist:
            return None
        
        else:
            if user.check_password(password):
                return user
        return None