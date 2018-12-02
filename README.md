**Mr Advisor**

**Group Name and Section**

Monty Python's Coding Circus, Section 1: Swathi Chandrasekaran (sc4415), Blair
(Xiaoshan) Gui (xg2302), Thomas Jaunet (taj2129), Kevin Tan (kt2707)

**General description**

Mr. Advisor is a python app providing a tool to track your scheduled events on a
monthly calendar, and help you decide which events to attend from a pool of
events you are interested in.

**Installation**

1/1 Clone the project repository on your machine.

**Use Case**

**A . Using directly the source code**

1/3 First input in a csv table (can be given any name) the different events
he/she is considering attending, regardless of time conflicts. For each event,
the user will have to fill-in the following attributes:

| Attribute Name | Description                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------|
| title          | name of the event                                                                                           |
| category       | type of event: A (academic), P (professional), C (cultural)                                                 |
| year           | YYYY format                                                                                                 |
| month          | Numeric MM format                                                                                           |
| day            | DD format                                                                                                   |
| start          | start time in 24 hours HHMM format                                                                          |
| end            | end time in 24 hours HHMM format                                                                            |
| priority       | score out of 10 describing the desire to attend the event                                                   |
| difficulty     | score out of 10 describing the difficulty of the course (for an academic event only, otherwise leave blank) |
| rating         | score out of 10 of the professor lecturing the course (for an academic event only, otherwise leave blank)   |

Here is an example for the table:

![](media/1d5eed94af97d160658a92c051d8a886.jpg)

2/3 Run the "main.py" file. The user will be invited to enter the path of the
csv table described just above. Then, he/she will be invited to enter the month
(MM numeric format) of the calendar needed.

Once "main.py" is done executing, the following message will be displayed:
"Calendar ready in [Month Number].csv"

3/3 Open the final outputs, which are as follows:

\- a csv table named "[Month Name].csv": this is the final recommended monthly
calendar. For each day of the month (columns of the table), it displays the name
of the events to attend at the appropriate time slots (rows). It is stored in
the same folder as the script.

\- an html file named "Display_[Month Number].html": final recommended calendar
in html format. It is stored in the same folder as the script.

**B. Using the Presentation notebook**

1/3 Input your events in a .csv file, following the same pattern as in the
previous method.

2/3 Execute the different cells and enter the file name when needed.

3/3 The last cell will ask you for which month you want to display.

**Internal Processes**

-   Main.py:

    Run this script to get the final calendar output. Creates a new instance of
    Calendar class. Asks for path of input csv table and month number. Then
    loads the input csv table, creates the output calendar file
    (“Calendar.fill()” function). Finally, saves the result into a csv table and
    HTML file (“displayT()” function).

-   Advisor.py:

    Defines functions to resolve conflicts i.e. events overlapping. For academic
    events, computes an academic score combining priority, difficulty and
    rating, which will replace the first priority attribute. Then, resolves
    conflicts based on the priority attribute. If a conflict still exists
    between two academic events, it will prioritize the most difficult course.
    If it’s between an academic event and any other type of event, it will
    always pick the academic one. For all remaining conflicts, one will be
    picked at random.

-   Calendar_tools.py:

    different functions used for formatting and displaying of the calendar.

-   Timetable.py:

    -   display: returns the output of calendar_tools.tableGenerator

    -   Calendar class:

|            | Name | Comment                                                                                 |
|------------|------|-----------------------------------------------------------------------------------------|
| Attributes | cal  | List containing the events to put in the calendar                                       |
| Methods    | load | Loads csv table into a list of dictionaries (1 dictionary equals to a row) put into cal |
|            | fill | Fill an empty calendar from cal                                                         |

-   Utils.py:

    functions used for testing clashes resolution
