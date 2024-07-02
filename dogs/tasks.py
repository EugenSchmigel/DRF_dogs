from datetime import datetime

from celery import shared_task

from dogs.models import Dog


@shared_task
def send_message_about_like(chat_id):
    print(f"message send to telegram to the Chat {chat_id}")



def send_birthday_mail():
    dog_list = Dog.objects.filter(birth_day=datetime.date.today())
    for dog in dog_list:
        print(f"Send mail to {dog.owner.username}")