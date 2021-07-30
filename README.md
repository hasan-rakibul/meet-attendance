# meet-attendance
Extracting student IDs from the recorded chat of a Google Meet session.

The initial code (ID extraction from clipboard) was written by my BRAC University colleague Md. Mahmudul Islam Wridoy. Later I personalized it for my purpose including saving those in excel as different sheet named according to course Id and date.

#### Steps
- Students will write their ID in the meet chatbox while the meeting is being recorded
- After the meeting, copy (Ctrl C) the whole chat transcript (saved on your G Drive) into computer clipboard
- Run the source code, and follow the instruction
- IDs will be available on the target excel file as a separate sheet. At first run, you need to create an excel file according to the name given within the source code.
- Process the students IDs in excel if required. For example, I used VLOOKUP there to count as per their ID serial and to know who is absent.
