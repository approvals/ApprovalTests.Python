from typing import Optional

from approvaltests.core import Namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer


def get_default_namer(extension: Optional[str] = None) -> Namer:
      return StackFrameNamer(extension)
