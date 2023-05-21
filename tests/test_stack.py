"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from unittest import TestCase, main
from src import stack


class NodeTest(TestCase):
    def test_init(self):
        node = stack.Node('test_data', None)
        self.assertEqual(node.data, 'test_data')
        self.assertIsNone(node.next_node)


class StackTest(TestCase):
    def setUp(self):
        self.stack = stack.Stack()

    def test_push(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')
        self.assertIsNone(self.stack.top.next_node)

    def test_pop(self):
        self.stack.push('test_data1')
        self.stack.push('test_data2')
        self.assertEqual(self.stack.pop(), 'test_data2')
        self.assertEqual(self.stack.pop(), 'test_data1')


if __name__ == '__main__':
    main()
