import pytest

from approvaltests import (
    verify,
    verify_all_combinations_async,
    verify_all_combinations_with_labeled_input_async,
)


async def get_data() -> str:
    return "Apple1"


async def async_sum(*args: int) -> int:
    return sum(args) + 1


@pytest.mark.asyncio
async def test_can_verify_in_async_test_function() -> None:
    data = await get_data()
    verify(data)


@pytest.mark.asyncio
async def test_async_verify_all_combinations() -> None:
    await verify_all_combinations_async(async_sum, [(1, 2), (3, 4)])


@pytest.mark.asyncio
async def test_async_verify_all_combinations_with_labeled_input() -> None:
    await verify_all_combinations_with_labeled_input_async(
        async_sum,
        arg1=(1, 3),
        arg2=(2, 4),
    )


@pytest.mark.asyncio
async def test_async_combination_records_exceptions() -> None:
    async def raises(*args: object) -> None:
        raise Exception(args)

    await verify_all_combinations_async(raises, [(1, 2), (3, 4)])
