def format_list(alist, formatter, header):
    if formatter is None:
        formatter = FormatLineItem().print_item
    text = header + '\n\n'
    for i in alist:
        text += formatter(i) + '\n'
    return text


class FormatLineItem(object):
    index = 0

    @classmethod
    def print_item(cls, x):
        text = str(cls.index) + ') ' + str(x)
        cls.index += 1
        return text