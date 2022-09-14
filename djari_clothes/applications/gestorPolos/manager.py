from django.db import models
from django.db.models import Count


class PoloManager(models.Manager):
    def get_recent_polo(self):
        query = self.order_by('-created')[:10]
        return query

    def get_polos_from_list(self, list_pk):
        query = self.filter(pk__in=list_pk)
        return query

    def get_polos_to_filter(self, data):
        query = self.all()
        list_colors = data['list_colors']
        range_price = data['range_price']
        list_tallas = data['list_tallas']
        list_marcas = data['list_marcas']

        if len(list_colors):
            query = query.filter(color__in=list_colors)
        if len(range_price):
            query = query.filter(price__gte=range_price[0], price__lte=range_price[1])
        if len(list_tallas):
            query = query.filter(talla__in=list_tallas)
        if len(list_marcas):
            query = query.filter(marcas__in=list_marcas)

        return query


class PoloFavoriteManager(models.Manager):
    def get_list_most_popular(self):
        # https://stackoverflow.com/questions/22124549/django-models-get-list-of-id
        # list_favorites_polos = self.values("polo").annotate(count_favorite=Count("client")).order_by(
        #     '-count_favorite')[:10].values_list('polo', flat=True)

        list_favorites_polos = self.values("polo").annotate(count_favorite=Count("client")).order_by(
            '-count_favorite')
        list_favorites_polos = list_favorites_polos[:10].values_list('polo', flat=True)

        return list_favorites_polos
