"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src import queue


class NodeTest(unittest.TestCase):
    def test_init(self):
        node = queue.Node('test_data', None)
        self.assertEqual(node.data, 'test_data')
        self.assertIsNone(node.next_node)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = queue.Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "1\n2")

    def test_dequeue(self):
        pass

    def test_dequeue_empty(self):
        self.assertEqual(self.queue.dequeue(), None)


if __name__ == "__main__":
    unittest.main()
