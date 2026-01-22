import os
import unittest
from main import hello_world, read_file, write_file, append_file


class TestFileUtilities(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_temp.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_file(self):
        write_file(self.test_file, 'test content')
        self.assertTrue(os.path.exists(self.test_file))

    def test_read_file(self):
        write_file(self.test_file, 'hello world')
        content = read_file(self.test_file)
        self.assertEqual(content, 'hello world')

    def test_append_file(self):
        write_file(self.test_file, 'line1')
        append_file(self.test_file, '\nline2')
        content = read_file(self.test_file)
        self.assertEqual(content, 'line1\nline2')

    def test_write_overwrites(self):
        write_file(self.test_file, 'first')
        write_file(self.test_file, 'second')
        content = read_file(self.test_file)
        self.assertEqual(content, 'second')


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        # Just verify it runs without error
        hello_world()


if __name__ == '__main__':
    unittest.main()
