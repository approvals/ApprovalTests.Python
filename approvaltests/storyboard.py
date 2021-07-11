from typing import Any, Callable


class Storyboard:
    def __init__(self) -> None:
        self.frame_number = 0
        self.story = ""

    def add_frame(self, data: Any) -> "Storyboard":
        if self.frame_number == 0:
            self.story += "Initial:\n"
        else:
            self.story += f"\n\nFrame #{self.frame_number}:\n"
        self.story += str(data)
        self.frame_number += 1

        return self

    def add_frames(self, number_of_frames: int, function_for_frame: Callable) -> "Storyboard":
        for n in range(number_of_frames):
            self.add_frame(function_for_frame(n))
        return self

    def __str__(self) -> str:
        return self.story

    def iterate_frames(self, data, number_of_frames = -1) -> "Storyboard":
        if number_of_frames == -1:
            try:
                number_of_frames = len(data)
            except:
                raise RuntimeError("You must pass in the number of frames.")
        for _, frame in zip(range(number_of_frames), data):
            self.add_frame(frame)
        return self