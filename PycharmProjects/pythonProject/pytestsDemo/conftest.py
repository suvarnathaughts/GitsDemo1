import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("firefox", "academy"), ("IE", "ss")])
def crossbrowser(request):
    return request.param
