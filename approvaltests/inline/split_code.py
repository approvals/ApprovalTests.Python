class SplitCode:
    def __init__(self, before_method, after_method, tab):
        self.before_method = before_method
        self.after_method = after_method
        self.tab = tab

    def __str__(self):
        return f"before:\n{self.before_method}\nafter:\n{self.after_method}"

    @staticmethod
    def on_method(code, method_name) -> "SplitCode":
        lines = code.split("\n")
        before = []
        after = []
        inside_method = False
        inside_doc_string = False
        tab = "    "
        after_method = False
        state = 0

        for line in lines:
            stripped_line = line.strip()

            if state == 0:
                before.append(line)
            if stripped_line.startswith(f"def {method_name}("):
                state = 1
                continue
            if state == 1:
                tab = line[: line.find(stripped_line)]
                if stripped_line.startswith('"""'):
                    state = 2
                    continue
                else:
                    state = 3
            if state == 2:
                if stripped_line.startswith('"""'):
                    state = 3
                continue
            if state == 3:
                after.append(line)

        return SplitCode("\n".join(before), "\n".join(after), tab)

    def indent(self, received_text):
        lines = received_text.split("\n")
        indented_lines = [f"{self.tab}{line}" for line in lines]
        return "\n".join(indented_lines)
