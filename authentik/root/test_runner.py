"""Integrate ./manage.py test with pytest"""
from django.conf import settings

from authentik.lib.config import CONFIG
from tests.e2e.utils import get_docker_tag


class PytestTestRunner:  # pragma: no cover
    """Runs pytest to discover and run tests."""

    def __init__(self, verbosity=1, failfast=False, keepdb=False, **_):
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb
        settings.TEST = True
        settings.CELERY_TASK_ALWAYS_EAGER = True
        CONFIG.y_set("authentik.avatars", "none")
        CONFIG.y_set("authentik.geoip", "tests/GeoLite2-City-Test.mmdb")
        CONFIG.y_set(
            "outposts.container_image_base",
            f"goauthentik.io/dev-%(type)s:{get_docker_tag()}",
        )

    def run_tests(self, test_labels):
        """Run pytest and return the exitcode.

        It translates some of Django's test command option to pytest's.
        """
        import pytest

        argv = ["-vv"]
        if self.failfast:
            argv.append("--exitfirst")
        if self.keepdb:
            argv.append("--reuse-db")

        if any("tests/e2e" in label for label in test_labels):
            argv.append("-pno:randomly")

        argv.extend(test_labels)
        return pytest.main(argv)
