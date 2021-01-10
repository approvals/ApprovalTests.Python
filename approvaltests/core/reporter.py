class Reporter(object):
    """
    Super class of all reporters in ApprovalTests.Python

    The only necessary function to implement for a
    reporter is 'report', which takes the absolute
    paths of the received- and approved files, and
    returns a truthy value on success.

    Whether the reporter is blocking or not is determined
    by the reporter itself.
    """

    def report(self, received_path, approved_path):
        """
        Apply the reporter to pair of files given
        as absolute paths parameters.

        A truthy return value from report means ???
        A falsy return value from report means ???
        """
        raise Exception("Interface member not implemented")
