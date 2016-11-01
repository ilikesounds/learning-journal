# Learning Journal assignment for CF SEAPY401.

## Step 4 of the Pyramid Learning Journal Assignment


### The URL for this deployment is (https://aqueous-lowlands-12022.herokuapp.com/)[https://aqueous-lowlands-12022.herokuapp.com/]

#### Routes
- There are 4 routes currently active in this project.
    - A list_view route that functions as the home route and serves up my index.html page via the list_view function.
    - A detail_view route that functions as the home route and serves up my detail.html page via the detail_view function.
    - - A edit_view route that functions as the home route and serves up my edit.html page via the edit_view function.
    - - A entry_view route that functions as the home route and serves up my entry.html page via the entry_view function.
- All four view funtions follow the same format and concatenate the path that the html pages are located at.

#### Testing Step 4

```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
learning_journal_basic/__init__.py                  12      9    25%
learning_journal_basic/models/__init__.py           22      0   100%
learning_journal_basic/models/entry.py               1      1     0%
learning_journal_basic/models/meta.py                5      0   100%
learning_journal_basic/models/mymodel.py             9      0   100%
learning_journal_basic/routes.py                     6      6     0%
learning_journal_basic/scripts/__init__.py           0      0   100%
learning_journal_basic/scripts/initializedb.py      32     32     0%
learning_journal_basic/views/__init__.py             0      0   100%
learning_journal_basic/views/default.py             50     19    62%
learning_journal_basic/views/notfound.py             4      4     0%
--------------------------------------------------------------------
TOTAL                                              141     71    50%

6 passed in 3.42 seconds
```

```
----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
learning_journal_basic/__init__.py                  12      9    25%
learning_journal_basic/models/__init__.py           22      0   100%
learning_journal_basic/models/entry.py               1      1     0%
learning_journal_basic/models/meta.py                5      0   100%
learning_journal_basic/models/mymodel.py             9      0   100%
learning_journal_basic/routes.py                     6      6     0%
learning_journal_basic/scripts/__init__.py           0      0   100%
learning_journal_basic/scripts/initializedb.py      32     32     0%
learning_journal_basic/views/__init__.py             0      0   100%
learning_journal_basic/views/default.py             50     19    62%
learning_journal_basic/views/notfound.py             4      4     0%
--------------------------------------------------------------------
TOTAL                                              141     71    50%

6 passed in 28.58 seconds
```
*thanks to [Victor](https://github.com/vbenavente/learning-journal) for help with tests*
