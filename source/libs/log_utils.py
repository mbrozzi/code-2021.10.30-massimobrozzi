
# -----------------------------------------------------------------------------------------------------

LOG_FILE = "logfile.log"

# *****************************************************************************************************
# Name: log_message
# Desc: Display an message on screen and log it to file
# Input: [STRING] text ==> text to log
#        [STRING] log_filename ==> file to log
# Return: None
# *****************************************************************************************************

def log_message(
        text=None,
        log_filename=LOG_FILE,
):
    if text:
        # Display the text on console/screen
        print(text)

        # Log the text also on file
        if log_filename:
            try:
                f = open(log_filename, 'a+', encoding='utf-8', errors='ignore')
                if f:
                    f.write("{}\n".format(text))
                f.close()
            except:
                print("Error in writing to file [{}]".format(log_filename))


# -----------------------------------------------------------------------------------------------------

# *****************************************************************************************************
# Name: display_error
# Desc: Display an error on screen, exit program if necessary
# Input: [STRING] text ==> error text
#        [BOOL True/False] ==> if True exit program
#        [STRING] log_filename ==> file to log
# Return: None
# *****************************************************************************************************

def display_error(
        text=None,
        exit_program=True,
        log_filename=LOG_FILE,
):
    if text:
        # Display the text on console/screen
        log_text = "[ERROR] {}".format(text)
        log_message(log_text, log_filename)

    if exit_program:
        exit()

# -----------------------------------------------------------------------------------------------------

# *****************************************************************************************************
# Name: display_warning
# Desc: Display a warning on screen
# Input: [STRING] text ==> error text
#        [STRING] log_filename ==> file to log
# Return: None
# *****************************************************************************************************

def display_warning(
        text=None,
        log_filename=LOG_FILE,
):
    if text:
        # Display the text on console/screen
        log_text = "[WARNING] {}".format(text)
        log_message(log_text, log_filename)

# -----------------------------------------------------------------------------------------------------
