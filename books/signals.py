import os
from dotenv import load_dotenv
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from gemini_api.client import get_book_ai_synopsis
from books.models import Book


load_dotenv()
api_key= os.getenv("API_KEY")

@receiver(pre_save, sender=Book)
def book_pre_save(sender, instance, **kwargs):
    if not instance.synopsis:
        if len(api_key) > 0:
            ai_synopsis = get_book_ai_synopsis(instance.title)
            instance.synopsis = ai_synopsis


@receiver(post_delete, sender=Book)
def book_post_delete(sender, instance, **kwargs):
    delete_photo(instance)


def delete_photo(instance):
    if instance.photo:
        instance.photo.delete(save=False)