class StringWriter(object):
    contents = ''

    def __init__(self, contents, extension='.txt'):
        self.contents = contents or ''
        self.extension_with_dot = extension

    def write_received_file(self, received_file):
        with open(received_file, 'w') as f:
            f.write(self.contents)
        return received_file
