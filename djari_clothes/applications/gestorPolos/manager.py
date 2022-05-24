from django.db import models


class PoloManager(models.Manager):
    def get_recent_polo(self):
        query = self.order_by('-created')[:10]
        return query

