from django.db import models
from django.db.models import Count


class PoloManager(models.Manager):
    def get_recent_polo(self):
        query = self.order_by('-created')[:10]
        return query

    def get_polos_from_list(self, list_pk):
        query = self.filter(pk__in=list_pk)
        return query


class PoloFavoriteManager(models.Manager):
    def get_list_most_popular(self):
        # https://stackoverflow.com/questions/22124549/django-models-get-list-of-id
        list_favorites_polos = self.values("id_polo").annotate(count_favorite=Count("id_client")).order_by(
            '-count_favorite')[:10].values_list('id_polo', flat=True)

        return list_favorites_polos
