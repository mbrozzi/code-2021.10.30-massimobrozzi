------------------------------------------------------------------------
SETUP
------------------------------------------------------------------------

1. Install Python 3.9.6 (or higher) on your Windows or Linux PC.

Note: No external lib needed to install.

------------------------------------------------------------------------
DESCRIPTION
------------------------------------------------------------------------

Files can be found in the following folders:

source => python Files
doics => docs Files

The core of the code is the file source/libs/bmi.python


Calculation of BMI is an easy task, anyway it could be extremely time consuming 
for millions of records. The code has been created for high performances in 
processing the user data.

For each pair WEIGHT-HEIGHT is calculated the BMI and then result is cached in
a Python Dict for fast retrival.

Once in the cache, every time there is the calculation of bmi and the regarding
risk categories, the result is simply got from the cache, without the need to 
recalculate it again and again...

On a normal PC under windows, it is possible to procss 10,000, 000 patients
in few seconds.

D:\Vamstar\source>python bmi_test.py
BMI Vamstar Test 1.0 [Release Date: 2021-10-27] - Copyright Dr.Eng. Massimo Brozzi (mbrozzi@gmail.com) 2021
----------------------------------------------------
Test Specs Dataset
----------------------------------------------------
[Category] Underweight => 0/6 0.00%
[Category] Normal weight => 2/6 33.33%
[Category] Overweight => 1/6 16.67%
[Category] Moderately obese => 3/6 50.00%
[Category] Severely obese => 0/6 0.00%
[Category] Very severely obese => 0/6 0.00%
Test Standard Computation time [34] millisecs.
----------------------------------------------------
Test 1,000,000 users Dataset
----------------------------------------------------
[Category] Underweight => 127949/1000000 12.79%
[Category] Normal weight => 45208/1000000 4.52%
[Category] Overweight => 34672/1000000 3.47%
[Category] Moderately obese => 34828/1000000 3.48%
[Category] Severely obese => 34881/1000000 3.49%
[Category] Very severely obese => 722462/1000000 72.25%
Test 1,000,000 Dataset Computation time [1172] millisecs.
----------------------------------------------------
Test 10,000,000 users Dataset
----------------------------------------------------
[Category] Underweight => 1277214/10000000 12.77%
[Category] Normal weight => 455000/10000000 4.55%
[Category] Overweight => 347325/10000000 3.47%
[Category] Moderately obese => 349611/10000000 3.50%
[Category] Severely obese => 349563/10000000 3.50%
[Category] Very severely obese => 7221287/10000000 72.21%
Test 10,000,000 Dataset Computation time [11354] millisecs.

------------------------------------------------------------------------
TESTS
------------------------------------------------------------------------

To run the tests:

- Dataset provided in the specs
- 1,000,000 randomly generated persons
- 10,000,000 randomly generated persons

please run

# run.bat

or

# cd source
# python bmi_test.py

------------------------------------------------------------------------
IMPORTANT NOTES
------------------------------------------------------------------------

- Code can be done more robust with a better check of adta and raising
of exceptions.

- Having more time it is worth to write a PyTest collection of testcases to test
all the class methods

Well... not in scope because too much time consuming for just a coding exercise! :)



