def format_list(alist, formatter, header):
    if formatter is None:
        formatter = FormatLineItem().print_item
    text = header + '\n\n'
    for i in alist:
        text += formatter(i) + '\n'
    return text


class FormatLineItem(object):
    def __init__(self):
        self.index = 0

    def print_item(self, x):
        text = str(self.index) + ') ' + str(x)
        self.index += 1
        return text