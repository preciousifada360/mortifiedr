# Core Django imports.
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import reverse

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.article_models import Article
from blog.models.minister_models import Profile


class MinisterListViewTestCase(TestCase):
    """
    Class to test the list of all ministers
    """

    def setUp(self):
        """
         Set up all the test using django client

         Model mommy creates three users and store them in a
          list called ministers and you can access each of them using indices.

         In the view, it returns all the users and you can access every users
         profile details through the user's model.
        """
        self.client = Client()
        self.ministers = mommy.make(User, _quantity=3)

    def test_ministers_list_view_status_code(self):
        response = self.client.get(reverse('blog:ministers_list'))
        self.assertEqual(response.status_code, 200)

    def test_ministers_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:ministers_list'))
        self.assertEqual(response.status_code, 200)

    def test_if_ministers_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:ministers_list'))
        self.assertTemplateUsed(response, 'blog/ministers/ministers_list.html')

    def test_if_minister_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>Mortified</title>")

    def test_if_minister_list_view_returns_the_right_number_of_ministers(self):
        response = self.client.get(reverse('blog:ministers_list'))
        self.assertEqual(len(response.context_data['ministers']), 3)

    # def test_if_minister_list_view_returns_the_right_minister_details(self):
    #     response = self.client.get(reverse('blog:ministers_list'))
    #     self.assertEqual(response.context_data['ministers'][0].profile,
    #                      self.ministers[0].profile)
    #     self.assertEqual(response.context_data['ministers'][0].first_name,
    #                      self.ministers[0].first_name)
    #     self.assertEqual(response.context_data['ministers'][0].last_name,
    #                      self.ministers[0].last_name)
    #     self.assertEqual(response.context_data['ministers'][0].email,
    #                      self.ministers[0].email)
    #     self.assertEqual(response.context_data['ministers'][0].username,
    #                      self.ministers[0].username)
    #     self.assertEqual(response.context_data['ministers'][0].profile.image,
    #                      self.ministers[0].profile.image)


class MinisterArticlesListViewTestCase(TestCase):
    """
      Class to test a particular minister's articles.
    """

    def setUp(self):
        """
        Setup all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.minister = mommy.make(User)
        self.articles = mommy.make(Article, body="Test", minister=self.minister, _quantity=5)

    def test_minister_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:minister_articles',
                                           kwargs={
                                               'username':
                                                   self.minister.username}
                                           )
                                   )
        self.assertEqual(response.status_code, 200)

    def test_if_minister_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:minister_articles',
                                           kwargs={
                                               'username':
                                                   self.minister.username}
                                           )
                                   )
        self.assertTemplateUsed(response, 'blog/ministers/minister_articles.html')

    # def test_if_minister_article_list_view_returns_the_right_minister_details(self):
    #     response = self.client.get(reverse('blog:minister_articles',
    #                                        kwargs={
    #                                            'username':
    #                                                self.minister.username}
    #                                        )
    #                                )
    #
    #     self.assertEqual(response.context_data["articles"][0].minister.id,
    #                      self.minister.id)
    #     self.assertEqual(response.context_data["articles"][0].minister.first_name,
    #                      self.minister.first_name)
    #     self.assertEqual(response.context_data["articles"][0].minister.last_name,
    #                      self.minister.last_name)
    #     self.assertEqual(response.context_data["articles"][0].minister.email,
    #                      self.minister.email)
    #     self.assertEqual(response.context_data["articles"][0].minister.username,
    #                      self.minister.username)
    #     self.assertEqual(response.context_data["articles"][0].minister.profile.image,
    #                      self.minister.profile.image)

    # def test_if_minister_article_list_view_returns_the_right_article_details(self):
    #     """
    #     This test checks if the view returns the right articles according to the
    #     date they were published.
    #
    #     In the setup, model mommy creates five articles and store
    #     them in a list called articles. So the last article in the list will
    #     be the first article in the list view since it was created last by model
    #     mommy.
    #     The list view orders articles according to the time they were published
    #     so the last article in the articles list will be displayed first in the
    #     view.
    #     """
    #     response = self.client.get(reverse('blog:minister_articles',
    #                                        kwargs={
    #                                            'username':
    #                                                self.minister.username}
    #                                        )
    #                                )
    #
    #     self.assertEqual(response.context_data['articles'][0].minister,
    #                      self.articles[4].minister)
    #     self.assertEqual(response.context_data['articles'][0].title,
    #                      self.articles[4].title)
    #     self.assertEqual(response.context_data['articles'][0].slug,
    #                      self.articles[4].slug)
    #     self.assertEqual(response.context_data['articles'][0].minister,
    #                      self.articles[4].minister)
    #     self.assertEqual(response.context_data['articles'][0].image,
    #                      self.articles[4].image)
    #     self.assertEqual(response.context_data['articles'][0].body,
    #                      self.articles[4].body)
    #     self.assertEqual(response.context_data['articles'][0].date_published,
    #                      self.articles[4].date_published)
    #     self.assertEqual(response.context_data['articles'][0].date_created,
    #                      self.articles[4].date_created)
    #     self.assertEqual(response.context_data['articles'][0].status,
    #                      self.articles[4].status)