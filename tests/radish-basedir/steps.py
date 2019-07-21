"""
radish
~~~~~~

The root from red to green. BDD tooling for Python.

:copyright: (c) 2019 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

from radish import given, when, then


@given("the webservice is started")
def start_webservice(step):
    """Start the Webservice"""
    pass


# @when("the {:str} route is queried")
@when("the {:S} route is queried")
def query_route(step, route):
    """Query the given route"""
    pass


# @then("the status code is {:int}")
@then("the status code is {:g}")
def assert_status_code(step, status_code):
    assert False, "This is a failure"
