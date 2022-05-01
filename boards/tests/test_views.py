from django.test import TestCase

from tasks.tests.factory_boy import TaskFactory

from .factory_boy import BoardFactory


class ViewTestCases(TestCase):
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_tasks(self):
        board = BoardFactory()
        TaskFactory(board=board)
        TaskFactory(board=board, title="Add authentication")

        response = self.client.get(board.get_absolute_url())
        self.assertEqual(response.status_code, 200)
