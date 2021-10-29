# -----------------------------------------------------------------------------------------------------
# Project:       BMI Vamstar Test
# Description:   Test for Vamstar interview
# Release:       1.0
# Date:          2021.10.30
# Author:        Dr. Eng. Massimo Brozzi - mbrozzi@gmail.com +447438578598
# -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------------------------------

import random

# -----------------------------------------------------------------------------------------------------
# External Libs imports
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# App imports
# -----------------------------------------------------------------------------------------------------

from libs.bmi import MIN_HEIGHT, MAX_HEIGHT
from libs.bmi import MIN_WEIGHT, MAX_WEIGHT
from libs.bmi import BodyMassIndex

from libs.chrono_utils import Chrono
from libs.log_utils import log_message

# -----------------------------------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------------------------------

APP_NAME = "BMI Vamstar Test"
APP_RELEASE = "1.0"
APP_DATE = "2021-10-30"
APP_COPYRIGHT = "Dr. Eng. Massimo Brozzi (mbrozzi@gmail.com)"
APP_COPYRIGHT_YEAR = 2021

# -----------------------------------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# Static Methods
# -----------------------------------------------------------------------------------------------------

# *****************************************************************************************************
# Name:   app_header
# Desc:   Display the App Header with information
# Input:  None
# Return: None
# *****************************************************************************************************

def app_header():
    print(
        "{} {} [Release Date: {}]".format(
            APP_NAME, 
            APP_RELEASE,
            APP_DATE,
        )
    )

    print(
        "Copyright {} {}".format(
            APP_COPYRIGHT,
            APP_COPYRIGHT_YEAR,
        )
    )

    print()

# -----------------------------------------------------------------------------------------------------

# *****************************************************************************************************
# Name:   run
# Desc:   Run the tests for specs data, 1,000,000 patients and 10,000,000 patients.
# Input:  None
# Return: None
# *****************************************************************************************************

def run_tests():
    bmi = BodyMassIndex()

    # Chrono the time...
    chrono = Chrono()

    test_dataset = [
        { "Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        { "Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        { "Gender": "Female", "HeightCm": 167, "WeightKg": 82},
    ]

    log_message("----------------------------------------------------")
    log_message("Initial dataset")
    log_message("----------------------------------------------------")

    print(test_dataset)

    test_dataset_bmi = bmi.add_bmi_info_to_persons(test_dataset)
   
    log_message("----------------------------------------------------")
    log_message("Adding BMI Infos...")
    log_message("----------------------------------------------------")

    print(test_dataset_bmi)

    log_message("")
    log_message("----------------------------------------------------")
    log_message("Test Specs Dataset")
    log_message("----------------------------------------------------")

    bmi_counters = bmi.get_bmi_categories_counters(persons=test_dataset)
    bmi.show_bmi_categories_counters(bmi_counters)

    # Print the computation time
    log_message(
        "Test Standard Computation time {}".format(
            chrono.elapsed_time_millisecs_str(True, False),
        )
    )

    test_dataset = []
    for i in range(1000000):
        test_dataset.append(
            {
                "Gender": "Male",
                "HeightCm": random.randint(MIN_HEIGHT, MAX_HEIGHT),
                "WeightKg": random.randint(MIN_WEIGHT, MAX_WEIGHT),
            }
        )

    log_message("")
    log_message("----------------------------------------------------")
    log_message("Test 1,000,000 users Dataset")
    log_message("----------------------------------------------------")

    chrono.start()

    bmi_counters = bmi.get_bmi_categories_counters(persons=test_dataset)
    bmi.show_bmi_categories_counters(bmi_counters)

    # Print the computation time
    log_message(
        "Test 1,000,000 Dataset Computation time {}".format(
            chrono.elapsed_time_millisecs_str(True, False),
        )
    )

    test_dataset = []
    for i in range(10000000):
        test_dataset.append(
            {
                "Gender": "Male",
                "HeightCm": random.randint(MIN_HEIGHT, MAX_HEIGHT),
                "WeightKg": random.randint(MIN_WEIGHT, MAX_WEIGHT),
            }
        )

    log_message("")
    log_message("----------------------------------------------------")
    log_message("Test 10,000,000 users Dataset")
    log_message("----------------------------------------------------")

    chrono.start()

    bmi_counters = bmi.get_bmi_categories_counters(persons=test_dataset)
    bmi.show_bmi_categories_counters(bmi_counters)

    # Print the computation time
    log_message(
        "Test 10,000,000 Dataset Computation time {}".format(
            chrono.elapsed_time_millisecs_str(True, False),
        )
    )


# -----------------------------------------------------------------------------------------------------

# *****************************************************************************************************
# Name:   Main
# Desc:   Execution of the program starts here
# Input:  None
# Return: None
# *****************************************************************************************************

if __name__ == "__main__":
    # Show th App Header
    app_header()

    # Run the tests
    run_tests()

    # Exit the program
    exit()

# -----------------------------------------------------------------------------------------------------
# End of File
# -----------------------------------------------------------------------------------------------------
