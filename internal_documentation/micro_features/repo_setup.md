# Repo Setup

## Concept

These are the basic dev scripts that every repo should have.

The underlying tool that supports the uderlying tools and tasks will be Mise-en-Place, aka "Mise". See https://mise.jdx.dev/.

The idea here is that you can clone a repo on a clean machine, then run one of these scripts, and it will just work (assuming Mise is already installed).

## Prerequisites

1. Mise

Mise will verify that all the tools we're going to use in the script are already installed.
it installs the tools that take care of the dependancies
it will create a Virtual env
we need to be EXPLICIT about how the virtual env is configured.



## Basic functionality

1. build_and_test (builds, runs tests, any other thing that is associated with that process)
2. format_code
3. mdsnippets

## Scripts syntax

For a given script we'll have both a Bash script and a CMD script. The Bash script will be named `script`, and the CMD script will be named `script.cmd`. The script will be one line long, containing only `mise run ...`.

## What and Why

Mise is a task and tool manager, like tox.
Tools like adding a chocolatey, but not system installed, per repo

## Replacing
tox

## Adding
managing python and other tools

## Benefits

simplify build_and_test

speed

doesn't assume system-installed tools

## Entry Points
 * format code (black)
 * build_and_test
 * mdsnippets
 * lint (not used)



