from rest_framework import serializers

SCAM_WORDS = ['Krypto','Börse', 'kaufe']

def validator_scam_words(value):
    if set(value.split()) & set(SCAM_WORDS):
        raise serializers.ValidationError('Not allowed words.')

