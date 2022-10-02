from approvaltests.scrubbers import create_regex_scrubber


class DateScrubber:
    @staticmethod
    def get_supported_formats():
        return [("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}", ["Tue May 13 16:30:00"]),
                ("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2} [a-zA-Z]{3,4} \\d{4}", ["Wed Nov 17 22:28:33 EET 2021"])]

    def __init__(self, date_regex: str):
        self.supported_formats = []
        self.date_regex = date_regex

    def scrub(self, date_str: str):
        return create_regex_scrubber(
            self.date_regex, lambda t: f"<date{t}>")(date_str)
