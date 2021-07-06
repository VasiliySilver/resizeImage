from django.test import SimpleTestCase

from django.urls import reverse, resolve
from django.views.generic.list import BaseListView

from app.views import HomePageView, image_details_view, add_image_view


class TestUrls(SimpleTestCase):
    def test_home_page_url_resolved(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.__name__, HomePageView.as_view().__name__)

    def test_add_image_url_resolved(self):
        url = reverse('add_image')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_image_view)

    def test_image_details_url_resolved(self):
        url = reverse('image_page', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, image_details_view)
