from approvaltests.scrubbers import create_regex_scrubber


class DateScrubber:
    @staticmethod
    def get_supported_formats():
        return [("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}", ["Tue May 13 16:30:00"]),
                ("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2} [a-zA-Z]{3,4} \\d{4}", ["Wed Nov 17 22:28:33 EET 2021"]),
                ("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{4} \\d{2}:\\d{2}:\\d{2}.\\d{3}", ["Tue May 13 2014 23:30:00.789"]),
                ("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2} -\\d{4} \\d{4}", ["Tue May 13 16:30:00 -0800 2014"]),
                ("\\d{2} [a-zA-Z]{3} \\d{4} \\d{2}:\\d{2}:\\d{2},\\d{3}", ["13 May 2014 23:50:49,999"]),
                ("[a-zA-Z]{3} \\d{2}, \\d{4} \\d{2}:\\d{2}:\\d{2} [a-zA-Z]{2} [a-zA-Z]{3}", ["May 13, 2014 11:30:00 PM PST"]),
                ("\\d{2}:\\d{2}:\\d{2}", ["23:30:00"]),
                ("\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{2}\\d",["2014/05/13 16:30:59.786"]),
                ("\\d{4}-\\d{1,2}-\\d{1,2}T\\d{1,2}:\\d{2}Z", ["2020-9-10T08:07Z","2020-09-9T08:07Z","2020-09-10T8:07Z","2020-09-10T08:07Z"]),
                ("\\d{4}-\\d{1,2}-\\d{1,2}T\\d{1,2}:\\d{2}:\\d{2}Z", ["2020-09-10T08:07:89Z"]),
                ("\\d{4}-\\d{1,2}-\\d{1,2}T\\d{1,2}:\\d{2}\\:\\d{2}\\.\\d{3}Z",["2020-09-10T01:23:45.678Z"]),
                ("\\d{8}T\\d{6}Z", ["20210505T091112Z"])
                ]

    def __init__(self, date_regex: str):
        self.supported_formats = []
        self.date_regex = date_regex

    def scrub(self, date_str: str):
        return create_regex_scrubber(
            self.date_regex, lambda t: f"<date{t}>")(date_str)
