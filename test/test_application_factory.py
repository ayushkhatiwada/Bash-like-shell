import unittest
from application_factory import ApplicationFactory, APPLICATIONS
from applications.application_unsafe import ApplicationUnsafe
from applications.application import ApplicationError


class TestApplicationFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ApplicationFactory()

    def test_valid_application_creation(self):
        for app_name, app_class in APPLICATIONS.items():
            with self.subTest(app_name=app_name):
                app_instance = self.factory.get_application(app_name)
                self.assertIsInstance(app_instance, app_class)

    def test_invalid_application_name(self):
        with self.assertRaises(ApplicationError):
            self.factory.get_application("nonexistent_app")

    def test_unsafe_application_creation(self):
        for app_name in APPLICATIONS.keys():
            with self.subTest(app_name=app_name):
                unsafe_app_name = f"_{app_name}"
                app_instance = self.factory.get_application(unsafe_app_name)

                self.assertTrue(
                    isinstance(app_instance, ApplicationUnsafe) and
                    isinstance(app_instance.safe_application,
                               APPLICATIONS[app_name])
                )
