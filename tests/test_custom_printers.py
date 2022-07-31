import argparse

from approvaltests import verify
from approvaltests.verifiable_objects.verifiable_argparse_namespace import VerifiableArgparseNamespace


def test_argparse_namespace() -> None:
    args = argparse.ArgumentParser()
    args.add_argument("foo")
    args.add_argument("--foo2")
    result = args.parse_args(["bar", "--foo2=bar2"])
    verify(VerifiableArgparseNamespace(result))
