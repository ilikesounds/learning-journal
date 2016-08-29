# Learning Journal assignment for CF SEAPY401.

## Step 4 is a work in progress. Once step-3 is complete, I will update the step-4 assignment.


### The URL for this deployment is (https://aqueous-lowlands-12022.herokuapp.com/)[https://aqueous-lowlands-12022.herokuapp.com/]

#### Routes
- There are 4 routes currently active in this project.
    - A list_view route that functions as the home route and serves up my index.html page via the list_view function.
    - A detail_view route that functions as the home route and serves up my detail.html page via the detail_view function.
    - - A edit_view route that functions as the home route and serves up my edit.html page via the edit_view function.
    - - A entry_view route that functions as the home route and serves up my entry.html page via the entry_view function.
- All four view funtions follow the same format and concatenate the path that the html pages are located at.


##

#### Testing Step 4
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
learning_journal_basic/__init__.py                  8      0   100%
learning_journal_basic/routes.py                    6      0   100%
learning_journal_basic/tests.py                    18      1    94%
learning_journal_basic/views.py                    14      5    64%
-------------------------------------------------------------------
TOTAL                                              46      6    87%

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
learning_journal_basic/__init__.py                  8      0   100%
learning_journal_basic/routes.py                    6      0   100%
learning_journal_basic/tests.py                    18      1    94%
learning_journal_basic/views.py                    14      5    64%
-------------------------------------------------------------------
TOTAL                                              46      6    87%
