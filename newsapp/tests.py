from django.test import TestCase
from django.urls import reverse
import uuid


class NewsTests(TestCase):
    def test_create_and_get_news(self):
        news_title = f'test-{uuid.uuid4()}'

        create_news = self.client.post(reverse('create_news'), data={"title": news_title, "text": str(uuid.uuid4())})
        self.assertEqual(create_news.status_code, 200)

        get_news = self.client.get(reverse('get_news'))
        self.assertEqual(get_news.status_code, 200)
        self.assertContains(get_news, news_title)
