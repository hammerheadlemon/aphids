from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from passes.models import PassType


class DjangoRestFrameworkTests(TestCase):
    def setUp(self):

        User.objects.create_user(username='test_lemon', password='lemon')
        self.client = APIClient()
        self.client.login(username='test_lemon', password='lemon')

        PassType.objects.get_or_create(pass_type='The Gold Standard!')
        PassType.objects.get_or_create(pass_type='The Silver Standard!')

        self.create_read_url = reverse('pass-type-list')
        self.read_update_delete_url = reverse(
            'pass-type-detail', kwargs={'pk': 1})

    def test_list(self):
        response = self.client.get('/api/pass-type/')

        # Are both types in content?
        self.assertContains(response, 'The Gold Standard!')
        self.assertContains(response, 'The Silver Standard!')

    def test_detail(self):
        response = self.client.get('/api/pass-type/1/')
        self.assertContains(response, 'The Gold Standard!')

    def test_post_pass_type(self):
        self.client.post(
            '/api/pass-type/', {'pass_type': 'Mungler'}, format='json')
        response = self.client.get('/api/pass-type/')
        self.assertContains(response, 'Mungler')
