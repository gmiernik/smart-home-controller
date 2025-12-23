import pytest
from asyncua import Client

from smart_home_controller.main import main


@pytest.mark.asyncio
async def test_server():
    # This is not a real test, just a placeholder to check if the server starts
    # In a real-world scenario, we would mock the server and test the logic
    assert True
