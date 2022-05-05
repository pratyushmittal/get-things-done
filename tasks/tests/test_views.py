from django.test import TestCase
from django.urls import reverse

from boards.tests.factory_boy import BoardFactory
from tasks.tests.factory_boy import TaskFactory


class TaskTestCases(TestCase):
    def test_task_update_status(self):
        board = BoardFactory()
        task = TaskFactory(
            category__board=board,
            title="foobar",
            description="description foobar",
            completed_at=None,
        )
        url = reverse(
            "boards:tasks:update_task",
            kwargs={"board_slug": board.slug, "task_id": task.id},
        )
        response = self.client.post(
            url,
            {
                "title": "foobar",
                "description": "desc foobaz",
                "is_completed": "true",
            },
        )
        self.assertEqual(response.status_code, 200, msg=response.json())

        task.refresh_from_db()
        self.assertEqual(task.title, "foobar")
        self.assertEqual(task.description, "desc foobaz")
        self.assertNotEqual(task.completed_at, None)
