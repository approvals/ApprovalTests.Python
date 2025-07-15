#! /usr/bin/env bash
mise --quiet task run install ::: test ::: mypy ::: integration_tests
