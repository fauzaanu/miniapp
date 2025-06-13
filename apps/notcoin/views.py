from django.views.generic import TemplateView


# Create your views here.
class ClickerView(TemplateView):
    template_name = "notcoin/clicker.html"
