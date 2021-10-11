from typing import cast

from django.conf import settings

from .ipstack import IPStack
from .mocks.ipstack import IPStackMock


def get_ipstack_client() -> IPStack:
    if settings.IS_TESTING:
        return IPStackMock(cast(str, settings.IPSTACK_ACCESS_KEY))
    return IPStack(cast(str, settings.IPSTACK_ACCESS_KEY))
