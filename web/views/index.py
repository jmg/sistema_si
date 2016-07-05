from shopify_app.views.base import BaseView
from django.conf import settings


class IndexView(BaseView):

    url = r"^$"

    def get(self, *args, **kwargs):

        return self.render_to_response({})
