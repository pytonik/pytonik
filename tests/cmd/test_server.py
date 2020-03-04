from unittest import TestCase
import pytonik.cmd.server as server

class TestServer(TestCase):
    def test_nonempty(self):
        self.assertEqual("something", server.nonempty("something"))
        self.assertRaises(server.ValidationError, server.nonempty, "")