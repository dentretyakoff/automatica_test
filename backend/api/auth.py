from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from core.models import Employee


class PhoneAuthentication(BaseAuthentication):
    """Авторизация по номеру телефона в заголовке.

    Authorization: Phone {номер телефона работника}
    """
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        header_parts = auth_header.split()

        if len(header_parts) != 2 or header_parts[0].lower() != 'phone':
            return None

        phone = header_parts[1]

        try:
            user = Employee.objects.get(phone=phone)
        except Employee.DoesNotExist:
            raise AuthenticationFailed(
                f'Пользователь с номером {phone} не зарегистрирован.'
                f'Укажите его в формате +79001112233.')

        return (user, None)
