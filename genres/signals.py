import os
from dotenv import load_dotenv
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from gemini_api.client import get_ai_genre
from genres.models import LiteraryGenre


load_dotenv()
api_key= os.getenv("API_KEY")

@receiver(pre_save, sender=LiteraryGenre)
def genre_pre_save(sender, instance, **kwargs):
    if not instance.description:
        if len(api_key) > 0:
            ai_genre = get_ai_genre(instance.name)
            instance.description = ai_genre