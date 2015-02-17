####################
IS 210 Assignment 04
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 15
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

The synthesizing tasks for week four are intended to challenge your application
of the principals of control-flow in some pseudo-realistic contexts. Be
especially careful to consider the problems from all angles as the unit tests
will challenge your attention to detail.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

The conditional ``if`` may be nested like many other compound statements. This
can be used to provide branching for decision trees.

Here we'll imagine that you're redesigning one of the rooms in your home but
are overwhelmed with all of the color choices available. You find it much
easier to make a decision between two colors than having all of them in front
of you at the same time. You know you want to have three colors in the room,
a ``BASE`` color, an ``ACCENT`` color, and a ``HIGHLIGHT`` color. To help
you pick, you'll build a decision tree where you select each of your three
colors one-at-a-time from the selections below.

Specifications
^^^^^^^^^^^^^^

1.  Create a file named ``task_01.py``

2.  Using ``raw_input()`` and nested ``if``, write a program to help you
    compare the colors in the chart below.
    
    1.  Prompt the user after each color is chosen to select from two new colors.
    
    2.  Only colors of the same Type and with the same Parent Color should be
        compared against each other (eg, ``Accent`` colors with the parent
        ``Pumice`` are only compared against other ``Accent`` colors with the
        parent ``Pumice``).
    
3.  Save each result into a variable named after the type, (eg, ``BASE``,
    ``ACCENT``, and ``HIGHLIGHT``).

4.  Complete the program by printing your color selections using a formatting
    string and ``.format()`` to replace your colors in the string.

    .. table:: Colors

        ================= ============ =======================
        Color             Type         Parent Color
        ================= ============ =======================
        Seattle Gray      Base         None
        Manatee           Base         None
        Ceramic Glaze     Accent       Seattle Gray
        Cumulus Nimbus    Accent       Seattle Gray
        Platinum Mist     Accent       Manatee
        Spartan Sage      Accent       Manatee
        Basically White   Highlight    Ceramic Glaze
        White             Highlight    Ceramic Glaze
        Off-White         Highlight    Cumulus Nimbus
        Paper White       Highlight    Cumulus Nimbus
        Bone White        Highlight    Platinum Mist
        Just White        Highlight    Platinum Mist
        Fractal White     Highlight    Spartan Sage
        Not White         Highlight    Spartan Sage
        ================= ============ =======================

Examples
^^^^^^^^

.. code:: console

    $ python -i task_01.py
    Which base color, "Seattle Gray" or "Manatee"?: Manatee
    Which accent color, "Platinum Mist" or "Spartan Sage"?: Spartan Sage
    Which highlight color, "Fractal White" or "Not White": Not White
    Your selected colors are, Manatee, Spartan Sage, and Not White.


.. code:: console

    $ python -i task_01.py
    Which base color, "Seattle Gray" or "Manatee"?: Manatee
    Which accent color, "Platinum Mist" or "Spartan Sage"?: Platinum Mist
    Which highlight color, "Bone White" or "Just White": Bone White
    Your selected colors are, Manatee, Platinum Mist, and Bone White.

Task 02
-------

When you need to perform a simple either/or assignment, a ternary expression
can be a useful tool in your toolkit. Here, we'll build a simple alarm clock
with snooze function.

Specifications
^^^^^^^^^^^^^^

1.  Open a new file named ``task_02.py``

2.  Ask the user what day it is using ``raw_input()``

3.  Next, use ``raw_input()`` to ask the user the time as a 4-digit number
    without a colon ('eg, ``0605``).

4.  Write a ternary expression to set a value to a variable named ``SNOOZE``

    If the day is ``'sat'`` or ``'sun'`` or the user-submitted time is
    less-than ``600``, set ``SNOOZE`` to ``True``, otherwise set it to
    ``False``

5.  Print an repeating alarm if ``SNOOZE`` is ``False``, eg::

        Beep! Beep! Beep! Beep! Beep!

.. hint::

    You can't always pre-edit whether your users will input strings in the
    right case. Since Python is case sensitive it can at times be helpful to
    force user-submitted input into a consistent case like lowercase before
    starting a comparison.

    Similarly, you can't always predict if they'll use common shorthands like
    ``'Sat'`` for ``'Saturday'`` or ``'Sun'`` for ``'Sunday'``. When
    reasonable, also consider shortening user-inputs with string slices.

.. note::

    Right now, we're going to skip an in-depth explanation of the Date/Time
    types of Python. This is not a particularly precise way of comparing
    times since it would allow a time like ``0670`` to exist but for our
    simple purposes here, it's enough. Not unlike ``Decimal()``, Python has
    special object types for dates and times.

Examples
^^^^^^^^

.. code:: console

    $ python -i task_02.py
    What day is it?: Tues
    What time is it?: 0813
    Beep! Beep! Beep! Beep! Beep!

Task 03
-------

Combined with Python's significant mathematical capabilities, the power of
conditionals can make for a powerful decision-making engine. To demonstrate
this power, we're going to be a mortgage calculator to calculate the lifetime
compound interest of a loan.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file ``task_03.py``

2.  Consider the following compound interest equation:

    .. math::

        A=P(1+\frac{r}{n})^{nt}

        \text{Where}\\
        &A \text{ is the total amount accumulated, with interest, over the
        duration of the loan}\\
        &P \text{ is the principal amount (the initial amount borrowed)}\\
        &r \text{ is the annual rate of interest represented as a decimal}\\
        &n \text{ is the number of times the interest is compounded each
        year}\\
        &t \text{ is the number of years for which } P \text{ is borrowed}\\

3.  Use this equation and the table below to create a program that calculates
    the total amount owed over the life of a loan. Use ``raw_input()`` to
    ask your users the following questions, in order:

    #.  What is your name?

    #.  What is the amount of your principal (the amount being borrowed)?

        - A whole integer

    #.  For how many years is this loan being borrowed?

        - A whole integer

    #.  Are you pre-qualified for this loan?

        -   Acceptable answers for this are 'Yes', 'y', 'No', and 'n'

    .. table:: Interest Rates

        ===================== ============ ============== =============
        Principal             Duration     Pre-qualified?  Interest Rate
        ===================== ============ ============== =============
        $0 - $199,999         1 - 15yrs    Yes            3.63%
        $0 - $199,999         1 - 15yrs    No             4.65%
        $0 - $199,999         16 - 20yrs   Yes            4.04%
        $0 - $199,999         16 - 20yrs   No             4.98%
        $0 - $199,999         21 - 30yrs   Yes            5.77%
        $0 - $199,999         21 - 30yrs   No             6.39%
        $200,000 - $999,999   1 - 15yrs    Yes            3.02%
        $200,000 - $999,999   1 - 15yrs    No             3.98%
        $200,000 - $999,999   16 - 20yrs   Yes            3.27%
        $200,000 - $999,999   16 - 20yrs   No             4.08%
        $200,000 - $999,999   21 - 30yrs   Yes            4.66%
        $1,000,000+           1 - 15yrs    Yes            2.05%
        $1,000,000+           16 - 20yrs   Yes            2.62%
        ===================== ============ ============== =============

#.  Using a series of nested ``if`` statements and comparison operators,
    calculate the total amount owed as an integer and store the result
    in a variable named ``TOTAL``.

    Assume that interest is compounded monthly (so *n = 12* in our above
    equation).

#.  Next, create a report for this user. The report should include the
    user's name and a summary of the relevant data and resemble the following::

        Loan Report for: Montgomery Burns
        --------------------------------------------------------------------
              Principal:         $173,254
              Duration:             18yrs
              Pre-qualified?:         Yes

              Total:             $358,073


    Replacing the recipient's name, principal amount, duration,
    pre-qualification status, and total as instructed. Note the uses of
    indentation, repetition, newlines (``\n``) and right justification.

#.  Save the completed report to a variable named ``REPORT``.

#.  Print the report.

.. note::

    There are several gaps in the Interest Rates table for pre-qualification
    statuses, durations, or principals that are not allowed. Your program
    should take these into account and set the total to ``None``.

.. hint::

    Use the Decimal() class to achieve the highest precision but ``round()``
    to round the final result to the nearest whole dollar.
    
.. hint::

    The value ``None`` is not the same as the string ``'None'``. How will
    that be represented in your report?

.. hint::

    You can use a variety of methods to build the report including
    concatenation assignment operators (``+=``), string repetition (``*``), 
    multi-line strings (``''''''``), parenthetical concatenation, and
    formatting strings with ``.format()``.

.. hint::

    A fundamental programming principal is DRY which stands for:
    *Don't repeat yourself.* Code that is copy/pasted within the same file or
    files is prone to breakage and can cause considerable clutter. Instead
    of calculating the total owed inside all of your ``if`` statements,
    consider just using the ``if`` to find the interest rate and set it into
    a variable. After the ``if`` block is complete, you can use the variable
    in your calculation.

Example
^^^^^^^

.. code:: console

    $ python -i task_03.py
    What is your name? Marlowe Sizzles
    What is the principal of the loan? 173254
    For how long is this being borrowed? 18
    Are you pre-qualified? Yes
    Loan Report for: Marlowe Sizzles
    --------------------------------------------------------------------
          Principal:         $173,254
          Duration:             18yrs
          Pre-qualified?:         Yes

          Total:             $358,073

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ sh runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
