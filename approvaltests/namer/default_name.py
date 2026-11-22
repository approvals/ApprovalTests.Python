from approvaltests.namer.stack_frame_namer import StackFrameNamer


def get_default_namer(extension: str | None = None) -> StackFrameNamer:
    return StackFrameNamer(extension)
