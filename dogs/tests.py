import json

from rest_framework import status
from rest_framework.reverse import reverse
from  rest_framework.test import APITestCase

from dogs.models import Breed, Dog


class DogTestCase(APITestCase):

    def setUp(self) -> None:
        self.breed = Breed.objects.create(
            name='test'
        )
        self.dog = Dog.objects.create(
            name='test',
            breed=self.breed
        )

    def test_get_list(self):
        """ test dog list """
        response = self.client.get(
            reverse('dog_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": self.dog.name,
                        "breed": self.dog.breed.name
                    }
                ]
            }
        )

    def test_dog_create(self):
        """ test create dog """

        data = {
                "name": "TEst dog",
                "breed": self.dog.breed.id
                }
        response = self.client.post(
            reverse('dog_list'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Dog.objects.all().count(),
            2
        )