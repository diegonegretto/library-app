import os
from dotenv import load_dotenv
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from gemini_api.client import get_author_ai_bio
from authors.models import Author


load_dotenv()
api_key= os.getenv("API_KEY")


@receiver(pre_save, sender=Author)
def author_pre_save(sender, instance, **kwargs):
    if not instance.biography:
        if len(api_key) > 0:
            ai_biography= get_author_ai_bio(instance.name)
            instance.biography = ai_biography


@receiver(post_delete, sender=Author)
def author_post_delete(sender, instance, **kwargs):
    delete_photo(instance)


def delete_photo(instance):
    if instance.photo:
        instance.photo.delete(save=False)