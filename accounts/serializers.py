from djoser.serializers import UserCreateSerializer, UserCreatePasswordRetypeSerializer


class UserCreate(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'password', 're_password'
        ]