from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Poroda')
    description = models.TextField(**NULLABLE, verbose_name='Opisanie')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'poroda'
        verbose_name_plural = 'porody'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Klichka')
    breed = models.ForeignKey("dogs.Breed", on_delete=models.CASCADE, verbose_name='Poroda')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Foto')
    birth_day = models.DateTimeField(**NULLABLE, verbose_name='Data Rozhdenie')
    price = models.PositiveIntegerField(null=True)

    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, **NULLABLE, verbose_name='Owner')
    is_public = models.BooleanField(default=False)
    likes = models.ManyToManyField("users.User", related_name="user_likes")

    def __str__(self):
        return f'{self.name} ({self.breed})'

    class Meta:
        verbose_name = 'sobaka'
        verbose_name_plural = 'sobaki'
