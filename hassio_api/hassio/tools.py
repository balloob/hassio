"""Tools file for HassIO."""
import asyncio
import logging
import json
import re

import aiohttp
import async_timeout

from .const import URL_HASSIO_VERSION

_LOGGER = logging.getLogger(__name__)

_RE_VERSION = re.compile(r"VERSION=(.*)")


async def fetch_current_versions(websession):
    """Fetch current versions from github."""
    try:
        with async_timeout.timeout(10, loop=websession.loop):
            async with websession.get(URL_HASSIO_VERSION) as request:
                data = await request.text()
                return json.loads(data)

    except (ValueError, aiohttp.ClientError, asyncio.TimeoutError) as err:
        _LOGGER.warning("Can't fetch versions from github! %s", err)


def get_version_from_env(env_list):
    """Extract Version from ENV list."""
    for env in env_list:
        found = _RE_VERSION.match(env)
        if found:
            return found.group(1)

    _LOGGER.error("Can't find VERSION in env")
    return None
