import unittest
from unittest import mock
from django.test import Client, RequestFactory

from django.core.files.uploadedfile import SimpleUploadedFile

from app.models import Image
from app.views import HomePageView


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

        # Create Image obj
        image = SimpleUploadedFile("image.jpg", content=b'', content_type="image/jpg")
        self.image_obj = Image.objects.create(title='test_image', image=image, original_image=image)

    def test_image_object(self):
        # check that object in all
        self.assertIn(self.image_obj, Image.objects.all())

        # Название title = test_image
        self.assertEqual(self.image_obj.title, 'test_image')

    def test_response_from_add_image(self):
        response = self.client.get('/add_image/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('app.views.HomePageView.get', return_value=mock_data) as mock_data_:
            print(mock_data_)
            factory = RequestFactory()
            request = factory.get('')
            response = HomePageView.as_view()(request)
            self.assertEqual(response.status_code, 444)
