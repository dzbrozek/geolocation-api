from django.conf import settings
from django.test.runner import DiscoverRunner


class CustomDiscoverRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        """
        Save original settings state and override settings
        """
        super().setup_test_environment(**kwargs)

        setattr(settings, 'IS_TESTING', True)

    def teardown_test_environment(self):
        """
        Restore original settings state.
        """
        super().teardown_test_environment()

        setattr(settings, 'IS_TESTING', False)
