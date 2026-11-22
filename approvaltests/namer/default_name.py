from approvaltests.namer.stack_frame_namer import StackFrameNamer


def get_default_namer(additional_information: str = "") -> StackFrameNamer:
    return StackFrameNamer(additional_information)
