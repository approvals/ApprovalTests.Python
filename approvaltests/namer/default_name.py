from approvaltests.namer.stack_frame_namer import StackFrameNamer


def get_default_namer(
    extension: str | None = None, additional_information: str = ""
) -> StackFrameNamer:
    return StackFrameNamer(extension, additional_information)
