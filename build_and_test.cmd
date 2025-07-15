@echo off
call mise task run install && call mise task run test ::: mypy ::: integration_tests
