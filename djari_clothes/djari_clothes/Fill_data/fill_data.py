from applications.gestorPolos.models import *
from applications.gestorPolos.views import *
from applications.gestorUsuarios.models import *
from applications.gestorUsuarios.views import *
from applications.gestorUsuarios.serializers import *
from applications.gestorVentas.models import *
from applications.gestorVentas.views import *

import json


def fill_admin(file):
    data = json.load(file)
    serializer = AdminSerializer(data)
    print(serializer)


if __name__ == '__main__':
    fill_admin("admins.json")
