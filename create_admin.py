import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snicgroup.settings')
django.setup()

User = get_user_model()


def create_super_user():
    User.objects.create_superuser(username='snicgroup', email='entreprise.snicgroup@gmail.com', password='snicgroup',
                                  first_name='SNIC', last_name='GROUP')


if __name__ == '__main__':
    create_super_user()