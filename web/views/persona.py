from shopify_app.views.base import BaseView
from django.conf import settings
from web.models import Persona
from dateutil.parser import parse


class CargarView(BaseView):

    def get(self, *args, **kwargs):

        personas = Persona.objects.all()

        return self.render_to_response({"personas": personas})


class GuardarView(BaseView):

    def post(self, *args, **kwargs):

        persona = Persona(
            nombre=self.request.POST.get("nombre"),
            apellido=self.request.POST.get("apellido"),
            dni=self.request.POST.get("dni"),
            fecha_de_nacimiento=parse(self.request.POST.get("fecha_de_nacimiento")),
        )
        persona.save()

        return self.redirect("/persona/cargar/?guardado=1")
