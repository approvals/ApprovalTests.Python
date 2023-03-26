pylint approvaltests --disable=C0103,W0703,C0415,W1514,R0913,R1705,E0401,W0212

:: W1514 - Unsure how to fix this, as google answer breaks code ( https://stackoverflow.com/questions/54835232/python-codec-error-during-file-write-with-utf-8-string )
:: R0913 - at some point break back compatibility and clean up API
:: pylint --disable=all --enable=C0412 .\approvaltests\
E0602
W0613
W0231
W0237
W0613
W0611
C0412
R0205
W0125
W0707
R0201