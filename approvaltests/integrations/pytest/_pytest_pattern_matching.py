import fnmatch


## This duplicates the logic in PyCollector._matches_prefix_or_glob_option() which unfortunately
## is not callable here because it its call to `self.config.getini()`.
#
## https://github.com/pytest-dev/pytest/blob/3422c67a3a46ccb4b5549c88821d5d768843418e/src/_pytest/python.py#L385
##
## Avoid editing this function, so we can manually compare it to the original pytest implementation.
def matches_prefix_or_glob(name: str, patterns: list[str]) -> bool:
    for option in patterns:
        if name.startswith(option):
            return True
        # Check that name looks like a glob-string before calling fnmatch
        # because this is called for every name in each collected module,
        # and fnmatch is somewhat expensive to call.
        elif ("*" in option or "?" in option or "[" in option) and fnmatch.fnmatch(
            name, option
        ):
            return True
    return False

