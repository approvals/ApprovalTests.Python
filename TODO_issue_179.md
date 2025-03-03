# Plan for 2024-11-03

SKIP 1 - Import latest approval test
WIP 2 - Run mypi

Jay - I want to work on projects that don't requre tribal knowledge.
Anti-pattern: Offer change (without test).  Assume Llewellyn will accept it.



WIP - Option
- Create a bash script (named 'test_issue_179') that exercises problem.
- Demonstrates the problem
- later... figure where to put it as a test


Diana
1 - Do not commit the tox changes in the starter project
   Good catch.  I did not commit them, but here is the diff to apply to a future starter project

```diff
diff --git a/tox.ini b/tox.ini
index b2c52fb..2c86f56 100644
--- a/tox.ini
+++ b/tox.ini
@@ -9,5 +9,8 @@ deps = -rrequirements.txt
 
 [testenv:dev]
 usedevelop = True
-commands =
-
+commands = 
+    mypy .
+deps = 
+    -rrequirements.txt
+    mypy

```
   
DONE 2 - Change python3 to be correct python for environment
	- Vote for don't care
