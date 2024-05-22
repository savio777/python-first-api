from .models import Users


def verifyIfEmailExist(email: str):
    try:
        user = Users.objects.get(email=email)

        if user:
            return True
        else:
            return False
    except:
        return False
