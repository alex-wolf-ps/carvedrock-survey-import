# Pulse survey import

SurveyPoint, the platform the customer survey runs on, has no integration worth using. It emails a
raw dump instead: semicolon-delimited, two preamble lines, and columns named `q1` to `q5`.

`import_survey.py` turns that into `survey-export.csv`, which is what the analysis uses.

Run it with `python import_survey.py`.