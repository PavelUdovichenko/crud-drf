from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Movies(models.Model):
    name = models.CharField(verbose_name='Name', db_index=True,unique=True, max_length=64)
    year = models.IntegerField(verbose_name='Year')
    author = models.CharField(verbose_name='author', max_length=128)
    RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    rate = models.IntegerField(verbose_name='rate', choices=RATE)
    user = models.ForeignKey(User, verbose_name='user,=', on_delete=models.CASCADE)
