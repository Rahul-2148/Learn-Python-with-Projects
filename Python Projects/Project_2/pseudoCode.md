1. Start the program 

2. DEFINE the name of the history file (e.g., "history.txt")

3. LOOP forever (while True):

    a. ASK the user to enter a calculation (like 8 + 5) OR a command ( history, clear, or exit) 

    b. IF user enters "exit":

        i. PRINT a goodbye message
        ii. Break the loop

    c. IF user enters "history":

        i. Try to open the history file for reading
        ii. IF the file exists and not empty, PRINT each line (calculation)
        iii. IF the file doesn't exist or is empty, PRINT "No history found"
        iv. CONTINUE to the next iteration of the loop

    d. IF user enters "clear":

        i. OPEN the history file and overwrite it with nothing (empty it)
        ii. PRINT "History cleared"
        iii. CONTINUE to the next iteration of the loop

    e. OTHERWISE (assume user entered a calculation):

        i. TRY to parse the input to get the numbers and the operator
           (You can split the input by space, e.g., "8 + 5" -> ["8", "+", "5"])

        ii. IF input is not valid, PRINT "Invalid input" and CONTINUE 

        iii. PERFORM the calculation using if/elif:
              - If +, add the numbers
              - If -, subtract the numbers
              - If *, multiply the numbers
              - If /, divide the numbers (and check for divide by zero)

        iv. SHOW the result to the user

        v. Write the calculation and result to the history file 
           (e.g., "8 + 5 = 13")

4. END the program