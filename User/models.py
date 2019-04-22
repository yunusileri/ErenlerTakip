from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False,
                    is_ogretmen_mi=False):
        if not username:
            raise ValueError('Geçerli bir kullanıcı adı giriniz!')
        if not password:
            raise ValueError('Geçerli bir Parola giriniz!')
        user_obj = self.model(username=username)
        user_obj.set_password(password)
        user_obj.ogretmen_mi = is_ogretmen_mi
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True)

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
            is_admin=True,
            is_staff=True
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=True)  # staff user non superuser
    admin = models.BooleanField(default=True)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    ogretmen_mi = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    object = UserManager()

    def __str__(self):
        return self.username

    def get_name(self):
        return self.username

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def is_ogretmen_mi(self):
        return self.ogretmen_mi
