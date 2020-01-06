# TASKS

### The tasks to be done in the current stage of this project are the following:

| Task | Where |
|----- | ------|
| Link to my page is not working<sup>[1](#footnote1)</sup> | Welcome window |
| Sticky the second entry text in whole remaining window | Second window |
| Include "working with previous upload file" option | Second window |
| Get the meaning of all text words after the user upload text | Second window |
| Include a warning that the previous task takes some minutes | Second window |
| Fix scroll roll | Third window
| Create scroll roll | Fourth window
| Fix buttons: "show me" and "skip" buttons are not working | Fourth window |
| Add translation feature in the output of "show me" button | Fourth window |
| Improve text font | All windows |





### Performance bottlenecks and code structure:

Problem | Where
------- | -----
Spending too much time in the transaction from window 1 to 2 after select language  | First window
Too much redundancy in the main code (i.e., brecht_full.py). Improve class structure  | All windows


<a name="footnote1">1</a>: change bind for the command option in Button will probably solve that