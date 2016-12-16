import pytest
import oldpuppetdb


# Set up our API objects
@pytest.fixture(scope='session')
def api2():
    """Set up a connection to PuppetDB with API version 2."""
    return oldpuppetdb.connect(api_version=2)


@pytest.fixture(scope='session')
def api3():
    """Set up a connection to PuppetDB with API version 3."""
    return oldpuppetdb.connect(api_version=3)


@pytest.fixture
def baseapi():
    return oldpuppetdb.api.BaseAPI(3)


@pytest.fixture
def utc():
    """Create a UTC object."""
    return oldpuppetdb.utils.UTC()
