import unittest

from applications.application import Application, FlagError


class TestApplication(unittest.TestCase):
    def setUp(self):
        class MockApplication(Application):
            allowed_flags = {"-a", "-s", "-r"}

            def exec(self, args, input, output):
                super().exec(args, input, output)

        self.mock_app = MockApplication()

    def test_abstract_application_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Application()

    def test_parse_flags(self):
        args = ["-a", "temp", "-s"]
        flags, clean_args = self.mock_app.parse_flags(
            args, self.mock_app.allowed_flags
        )
        self.assertEqual(flags, {"-a", "-s"})
        self.assertEqual(clean_args, ["temp"])

    def test_parse_flags_invalid_flag(self):
        args = ["-a", "temp", "-s", "-z"]
        with self.assertRaises(FlagError):
            self.mock_app.parse_flags(args, self.mock_app.allowed_flags)

    def test_parse_flags_no_flags(self):
        args = ["temp"]
        flags, clean_args = self.mock_app.parse_flags(
            args, self.mock_app.allowed_flags
        )
        self.assertEqual(flags, set())
        self.assertEqual(clean_args, ["temp"])
