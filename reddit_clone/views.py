from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "index.html"


class TestPageView(TemplateView):
    template_name = "test.html"


class ThanksPageView(TemplateView):
    template_name = "thanks.html"
