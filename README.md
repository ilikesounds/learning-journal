# Learning Journal assignment for CF SEAPY401.

### The URL for this deployment is (https://aqueous-lowlands-12022.herokuapp.com/)[https://aqueous-lowlands-12022.herokuapp.com/]

#### Routes
- There are 4 routes currently active in this project.
    - A list_view route that functions as the home route and serves up my index.html page via the list_view function.
    - A detail_view route that functions as the home route and serves up my detail.html page via the detail_view function.
    - - A edit_view route that functions as the home route and serves up my edit.html page via the edit_view function.
    - - A entry_view route that functions as the home route and serves up my entry.html page via the entry_view function.
- All four view funtions follow the same format and concatenate the path that the html pages are located at.

#### testing

```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
learning_journal_basic/__init__.py                  8      0   100%
learning_journal_basic/routes.py                    6      0   100%
learning_journal_basic/tests.py                    30      0   100%
learning_journal_basic/views.py                    14      0   100%
-------------------------------------------------------------------
TOTAL                                              58      0   100%

5 passed in 0.59 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
learning_journal_basic/__init__.py                  8      0   100%
learning_journal_basic/routes.py                    6      0   100%
learning_journal_basic/tests.py                    30      0   100%
learning_journal_basic/views.py                    14      0   100%
-------------------------------------------------------------------
TOTAL                                              58      0   100%

5 passed in 3.36 seconds
```

*thanks to [Victor](https://github.com/vbenavente/learning-journal) for help with tests*
