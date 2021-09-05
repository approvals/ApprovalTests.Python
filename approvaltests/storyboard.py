from typing import Any, Callable, Optional, Iterable, Sized, Collection


class Storyboard:
    def __init__(self) -> None:
        self.frame_number = 0
        self.story = ""
        self.add_new_line = False

    def add_frame(self, data: Any, title: Optional[str] = None) -> "Storyboard":
        if self.add_new_line:
            self.story += "\n"
            self.add_new_line = False
        if title:
            self.story += f"{title}:\n"
        elif self.frame_number == 0:
            self.story += "Initial:\n"
        else:
            self.story += f"Frame #{self.frame_number}:\n"
        self.story += f"{data}\n\n"
        self.frame_number += 1

        return self

    def add_frames(
        self, number_of_frames: int, function_for_frame: Callable[[int], Any]
    ) -> "Storyboard":
        for n in range(number_of_frames):
            self.add_frame(function_for_frame(n))
        return self

    def __str__(self) -> str:
        return self.story

    def iterate_frames(
        self, data: Collection[Any], number_of_frames: int = -1
    ) -> "Storyboard":
        if number_of_frames == -1:
            try:
                number_of_frames = len(data)
            except:
                raise RuntimeError(
                    "You must pass in the number of frames for this iterable."
                )
        for _, frame in zip(range(number_of_frames), data):
            self.add_frame(frame)
        return self

    def add_description(self, description):
        self.story += f"{description}\n\n"
        return self

    def add_description_with_data(self, description: str, data: Any) -> "Storyboard":
        self.story += f"{description}: {data}\n"
        self.add_new_line = True
        return self

StoryBoard = Storyboard