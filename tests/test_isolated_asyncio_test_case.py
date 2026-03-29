from unittest import IsolatedAsyncioTestCase

from approvaltests import verify
from approvaltests.namer.stack_frame_namer import StackFrameNamer


class TestIsolatedAsyncioTestCase(IsolatedAsyncioTestCase):
    async def test_namer_finds_correct_method_name(self) -> None:
        namer = StackFrameNamer()
        self.assertEqual(
            "test_namer_finds_correct_method_name", namer.get_method_name()
        )

    async def test_namer_finds_correct_class_name(self) -> None:
        namer = StackFrameNamer()
        self.assertEqual(self.__class__.__name__, namer.get_class_name())

    async def test_example(self) -> None:
        verify("something")
