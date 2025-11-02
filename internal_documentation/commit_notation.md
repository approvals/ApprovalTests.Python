# Arlo's Git notation

| code | intention |
| - | - |
| F | feature |
| B | bugfix |
| r | refactoring |
| t | test-only |
| e | development environment |
| d | documentation   |

| code | risk |
| - | - |
| . | We are completely certain that it can't break production |
| - | **Whole system** is verified with comprehensive (unit) testing, before and after this change |
| ! | **This behavior change** is verified with automated tests |
| @ | No verification |

## NOTES

Official name is Risk Aware Commit Notation (RACN); formerly called "Arlo's Commit Notation" (ACN).

Llewellyn uses `-` in situations where  RACN recommends `^`.
