# Build System Migration

## Problem

Build warnings are occurring due to deprecated `setup.py install` usage in the current build process.

## Warning Details

```
C:\Code\ApprovalTests.Python\.venv\lib\site-packages\setuptools\_distutils\cmd.py:66: 
SetuptoolsDeprecationWarning: setup.py install is deprecated.

********************************************************************************
Instead, use pypa/build, pypa/installer or other standards-based tools.

See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
********************************************************************************
```

## Current Setup Architecture

```
Repository Root (ApprovalTests.Python)
│
├── Source Packages (in repo root)
│   ├── approvaltests/          # Main testing library
│   └── approval_utilities/     # Production utilities
│
├── setup/ directory
│   ├── setup_utils.py          # Shared setup logic
│   │   └── do_the_setup()      # Common setup function
│   │
│   ├── setup.py                # Main: approvaltests (full)
│   │   ├── Includes: required + extras deps
│   │   └── Uses: setup_utils.do_the_setup()
│   │
│   ├── setup.minimal.py        # Variant: approvaltests-minimal
│   │   ├── Includes: required deps only
│   │   ├── Optional: extras via extras_require
│   │   └── Uses: setup_utils.do_the_setup()
│   │
│   ├── setup.publish.py        # Variant: approvaltests (for PyPI)
│   │   ├── Includes: required + extras deps
│   │   ├── Adds: approval_utilities dependency
│   │   └── Uses: setup_utils.do_the_setup()
│   │
│   └── setup.approval_utilities.py  # Separate: approval_utilities
│       └── Standalone setup (no shared utils)
│
├── Publishing Scripts
│   ├── publish_approvaltests.sh
│   │   └── Runs: setup.publish.py
│   │
│   ├── publish_minimal.sh
│   │   └── Runs: setup.minimal.py
│   │
│   └── publish_approval_utilities.sh
│       ├── Swaps: setup.py ↔ setup.approval_utilities.py
│       ├── Runs: setup.py (temporarily approval_utilities)
│       └── Restores: original setup.py
│
└── Dependency Files
    ├── requirements.prod.required.txt  # Core deps
    └── requirements.prod.extras.txt    # Optional features

Published Packages (to PyPI):
┌─────────────────────────────────────────────────────────┐
│ 1. approval_utilities     (standalone utility package)  │
│ 2. approvaltests          (full, depends on #1)         │
│ 3. approvaltests-minimal  (minimal, no #1 dependency)   │
└─────────────────────────────────────────────────────────┘
```

## PyPI Release Flowchart

```
                        ┌──────────────────────┐
                        │   Single Monorepo    │
                        │  (ApprovalTests.Py)  │
                        └──────────┬───────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
                ▼                  ▼                  ▼
    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
    │   RELEASE 1     │ │   RELEASE 2     │ │   RELEASE 3     │
    │                 │ │                 │ │                 │
    │   approval_     │ │  approvaltests  │ │ approvaltests-  │
    │   utilities     │ │     (full)      │ │    minimal      │
    └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
             │                   │                   │
             │                   │                   │
    ┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
    │ File Swapping   │ │ Direct Build    │ │ Direct Build    │
    │ (setup.py hack) │ │ (setup.publish) │ │ (setup.minimal) │
    └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
             <!-- │                   │                   │ -->
    ┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
    │ Source:         │ │ Source:         │ │ Source:         │
    │ approval_       │ │ approvaltests/  │ │ approvaltests/  │
    │ utilities/      │ │                 │ │ (same source!)  │
    │                 │ │ Deps: required  │ │                 │
    │ Deps: none      │ │     + extras    │ │ Deps: required  │
    │                 │ │     + approval_ │ │       only      │
    │                 │ │       utilities │ │                 │
    └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
             │                   │                   │
             │                   │                   │
             └─────────┬─────────┴─────────┬─────────┘
                       │                   │
                       ▼                   ▼
              ┌─────────────────┐ ┌─────────────────┐
              │  PyPI Package   │ │  PyPI Package   │
              │  approval_      │ │  approvaltests  │
              │  utilities      │ │  (2 variants)   │
              └─────────────────┘ └─────────────────┘

═══════════════════════════════════════════════════════════════════════
                         RELEASE CONSTRAINTS
═══════════════════════════════════════════════════════════════════════

Order Dependency:  approval_utilities  ──must publish before──►  approvaltests (full)

Same Source:       approvaltests (full)  ═══ same code ═══  approvaltests-minimal
                   (only dependency configuration differs)
```

## Complexity Factors

1. **Multiple Packages from Single Repo**: 3 PyPI packages from one codebase
2. **Shared Setup Logic**: `setup_utils.py` used by multiple setup files
3. **File Swapping**: `publish_approval_utilities.sh` temporarily renames files
4. **Dependency Variants**: Full vs minimal versions with different deps
5. **Cross-Package Dependencies**: `approvaltests` depends on `approval_utilities`

## Status

Investigating modern build system alternatives to resolve the deprecation warning.

## Decision

TBD