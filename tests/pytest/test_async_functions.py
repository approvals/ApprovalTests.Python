import pytest

from approvaltests import verify


async def get_data():
    return "Apple1"

@pytest.mark.asyncio
async def test_can_verify_in_async_test_function():
    data = await get_data()
    verify(data)
