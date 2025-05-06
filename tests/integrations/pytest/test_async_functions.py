import pytest

from approvaltests import verify


async def get_data() -> str:
    return "Apple1"


@pytest.mark.asyncio
async def test_can_verify_in_async_test_function() -> None:
    data = await get_data()
    verify(data)
