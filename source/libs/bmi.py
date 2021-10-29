# -----------------------------------------------------------------------------------------------------
# Class:         BMI
# Description:   Class to calculate BMI (Body Mass Index)
# Release:       1.0
# Author:        Dr. Eng. Massimo Brozzi - mbrozzi@gmail.com +447438578598
# -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------------------------------

# None
 
# -----------------------------------------------------------------------------------------------------
# External Libs imports
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# App imports
# -----------------------------------------------------------------------------------------------------

from libs.log_utils import display_error

# -----------------------------------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------------------------------


MIN_HEIGHT = 1
MAX_HEIGHT = 250

MIN_WEIGHT = 1
MAX_WEIGHT = 300

# Table 1 - BMI Category and the Health Risk.
# BMI Category BMI Range (kg/m2) Health risk
# Underweight          18.4 and below Malnutrition risk
# Normal weight        18.5 - 24.9 Low risk
# Overweight           25 - 29.9 Enhanced risk
# Moderately obese     30 - 34.9 Medium risk
# Severely obese       35 - 39.9 High risk
# Very severely obese  40 and above Very high risk

RISK_TABLE = {
    "Underweight": {
        "bmi": 18.4,
        "health_risk": "Malnutrition risk",
    },  # Index 0
    "Normal weight": {
        "bmi":18.5,
        "health_risk": "Low risk",
    },  # Index 1
    "Overweight": {
        "bmi": 25.0,
        "health_risk": "Enhanced risk",
    },  # Index 2
    "Moderately obese": {
        "bmi": 30.0,
        "health_risk": "Medium risk",
    },  # Index 3
    "Severely obese": {
        "bmi": 35.0,
        "health_risk": "High risk",
    },  # Index 4
    "Very severely obese": {
        "bmi": 40.0,
        "health_risk": "Very high risk",
    },  # Index 5
}


# -----------------------------------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# Static Methods
# -----------------------------------------------------------------------------------------------------

# None

# -----------------------------------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------------------------------

class BodyMassIndex():
    # -----------------------------------------------------------------------------

    category_dict = {}

    # -----------------------------------------------------------------------------
    # Method:      __init__
    # Description: Initializer
    # Input:       None
    # Output:      None
    # -----------------------------------------------------------------------------

    def __init__(
        self,
    ):
        self.calc_all_bmi_categories()

    # -----------------------------------------------------------------------------
    # Method:      calc_all_bmi_categories
    # Description: Initializer
    # Input:       None
    # Output:      None
    # -----------------------------------------------------------------------------

    def calc_all_bmi_categories(self):
        self.category_dict = {}

        for weight in range(MIN_WEIGHT, MAX_WEIGHT + 1):
            for height in range(MIN_HEIGHT, MAX_HEIGHT + 1):
                key = BodyMassIndex.get_bmi_key_dict(weight, height)
                bmi = self.calc_bmi(weight, height)
                if bmi is not None:
                    self.category_dict[key] = self.get_bmi_category(bmi)
                else:
                    print("errore", bmi)

    # -----------------------------------------------------------------------------
    # Method:      get_bmi_key_dict
    # Description: Initializer
    # Input:       None
    # Output:      None
    # -----------------------------------------------------------------------------

    @staticmethod
    def get_bmi_key_dict(
        weight,
        height,
    ):
        return "{}_{}".format(weight, height)

    # -----------------------------------------------------------------------------
    # Method:      calc_bmi
    # Description: Initializer
    # Input:       INT => weigth in KGs
    #              INT => height in CMs
    # Output:      FLOAT => BMI value
    # -----------------------------------------------------------------------------

    @staticmethod
    def calc_bmi(
        weight=None,
        height=None,
    ):
        result = None

        if not weight or not MIN_WEIGHT <= weight <= MAX_WEIGHT:
            display_error("Wrong Weight value [{}]".format(weight), exit_program=False)
        elif not height or not MIN_HEIGHT <= height <= MAX_HEIGHT:
            display_error("Wrong Height value [{}]".format(height), exit_program=False)
        else:
            # Note: Height must be expressed in Mt dividing Cm per 100
            # Coìnverting possible floating values to int
            result = int(weight) / ((0.01 * int(height)) ** 2)

        return result

    # -----------------------------------------------------------------------------
    # Method:      get_categories_risk_list
    # Description: Initializer
    # Input:       None
    # Output:      LIST => Risk Categories names
    # -----------------------------------------------------------------------------

    def get_categories_risk_list(
        self,
    ):
        return list(RISK_TABLE.keys())

    # -----------------------------------------------------------------------------
    # Method:      get_bmi_category
    # Description: Initializer
    # Input:       float => bmi value > 0.0
    # Output:      string => Risk Category ID
    # -----------------------------------------------------------------------------

    def get_bmi_category(
        self,
        bmi=None,
    ):
        result = None

        if bmi and bmi > 0.0:
            risks = self.get_categories_risk_list()

            result = risks[0] # "Underweight"

            # loops oin categories to find the right one
            for risk in risks[1:]:
                if bmi >= RISK_TABLE[risk]["bmi"]:
                      result = risk
                else:
                     break

        return result

    # -----------------------------------------------------------------------------
    # Method:      get_person_bmi
    # Description: Calculate BMI for a person
    # Input:       DICT => person
    # Output:      float => bmi
    # -----------------------------------------------------------------------------

    def get_person_bmi(
        self,
        person=None,
    ):
        if not person:
            display_error("No person to process")

        if "WeightKg" not in person:
            display_error("No WeightKg field in person")

        if "HeightCm" not in person:
            display_error("No HeightCM field in person")

        return self.calc_bmi(
            person["WeightKg"],
            person["HeightCm"],
        )
    
    # -----------------------------------------------------------------------------
    # Method:      get_person_bmi_category
    # Description: Calculate BMI risk category for a person
    # Input:       DICT => person
    # Output:      float => bmi
    # -----------------------------------------------------------------------------

    def get_person_bmi_category(
        self,
        person=None,
    ):
        if not person:
            display_error("No person to process")

        if "WeightKg" not in person:
            display_error("No WeightKg field in person")

        if "HeightCm" not in person:
            display_error("No HeightCM field in person")

        return self.category_dict[
            BodyMassIndex.get_bmi_key_dict(
                person["WeightKg"],
                person["HeightCm"],
            )
        ]

    # -----------------------------------------------------------------------------
    # Method:      add_bmi_info_to_persons
    # Description: Add to persons the BMI info
    # Input:       Array[Dicts] => Persons
    # Output:      Array[Dicts] => Persons with BMI info
    # -----------------------------------------------------------------------------

    def add_bmi_info_to_persons(
        self,
        persons=None,
    ):
        if not persons:
            display_error("No persons to process")

        if persons:
            for i in range(0, len(persons)):
                persons[i]["bmi"] = self.get_person_bmi(persons[i])
                person_bmi_category = self.get_person_bmi_category(persons[i])
                persons[i]["BMICategory"] = person_bmi_category
                persons[i]["HealthRisk"] = RISK_TABLE[person_bmi_category]["health_risk"]

        return persons

    # -----------------------------------------------------------------------------
    # Method:      get_bmi_categories_counters
    # Description: Calculates counters for Risk Categories
    # Input:       Array[Dicts] => Persons
    # Output:      Dict => Counters for risk categories
    # -----------------------------------------------------------------------------

    def get_bmi_categories_counters(
        self,
        persons=None,
    ):
        if not persons:
            display_error("No persons to process")

        bmi_counters = {}
 
        if persons:
            for risk in self.get_categories_risk_list():
                bmi_counters[risk] = 0

            for person in persons:
                person_bmi_category = self.get_person_bmi_category(person)
                if person_bmi_category is not None:
                    bmi_counters[person_bmi_category] += 1

        return bmi_counters

    # -----------------------------------------------------------------------------
    # Method:      show_bmi_categories_counters
    # Description: Display/Log counters/stats for BMI Risk Categories
    # Input:       Dict => Counters for risk categories
    # Output:      None
    # -----------------------------------------------------------------------------

    @staticmethod
    def show_bmi_categories_counters(
        bmi_counters=None,
    ):
        if not bmi_counters:
            display_error("No BMIs to display")

        total_bmi = sum(list(bmi_counters.values()))

        if total_bmi:
            for bmi_category in bmi_counters.keys():
                print(
                    "[Category] {} => {}/{} {:.2f}%".format(
                        bmi_category, 
                        bmi_counters[bmi_category],
                        total_bmi,
                        100.0 * bmi_counters[bmi_category] / total_bmi
                    )
                )
        else:
            print("No BMI Categories to display.")

# -----------------------------------------------------------------------------------------------------
# End of Class Chrono
# -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# End of File
# -----------------------------------------------------------------------------------------------------

