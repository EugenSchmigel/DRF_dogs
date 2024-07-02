import requests
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField

from dogs.models import Dog
from dogs.serializers.breed import BreedDetailSerializer
from dogs.validators import validator_scam_words


class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validator_scam_words])

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(serializers.ModelSerializer):
    breed = BreedDetailSerializer()
    dog_with_same_breed = SerializerMethodField()
    price_eur = SerializerMethodField()
    price_usd = SerializerMethodField()

    def get_dog_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    def get_price_eur(self, dog):

        print(dog.price)

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "xKXrA65sVZO8oyu83DS4PIDvDKxGuTRu"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        print(result)
        return result.get("result")


    def get_price_usd(self, dog):

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount={dog.price}"

        payload = {}
        headers = {
            "apikey": "xKXrA65sVZO8oyu83DS4PIDvDKxGuTRu"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        return result.get("result")


    class Meta:
        model = Dog
        fields = ("name", "breed", "dog_with_same_breed", "price_eur", "price_usd")