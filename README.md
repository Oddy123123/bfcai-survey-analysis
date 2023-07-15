# bfcai-survey-analysis

This code allows us to analyze surveys in BFCAI to calculate percentage of each choice in addition to overall satisfaction percentage.
Original code by Eng. Abdallah Al-Ghamry can be found in the initial commit.

## Usage

### Method 1: GUI

![Screenshot 2023-07-15 224757](https://github.com/Oddy123123/bfcai-survey-analysis/assets/95940642/dc73296b-b2a0-472d-8dbd-77246507ccba)


1. Open the file "Analysis.ipynb" inside Jupyter notebook and run the code. A GUI will open.
2. Choose the course type (Lecture only / Lecture + Lab / Lecture + Lab + Exercise)
3. Click on the "choose file" button and locate the excel file that contains the survey responses
4. If you receive a success message:
   - you will find the analysis result in an excel file in the same folder as the notebook file.
   - Also you will find the summary result in the output of the notebook like the following image

![Untitled](https://github.com/Oddy123123/bfcai-survey-analysis/assets/95940642/ecc79bd7-5f88-4b46-89cb-ff51ad985955)

### Method 2: CLI

You can also use this tool from the command line and get the same output. You can run the following command:

`python analyze.py <path> <course_type>`

Such that:
- The `<path>` argument is the path to the excel file that contains the survey resonses
- The `<course_type>` argument is an integer (1-3) indicating the type of the course where:
    - 1 = Lecture only
    - 2 = Lecture + Lab
    - 3 = Lecture + Lab + Exercise
 
Example usage:

`python analyze.py "D:\College\_الاستبيانات\excel\استبيان مقرر برمجة شيئية - 2023(1-13).xlsx" 2`

You will get the same output as mentioned in method 1

Example output:

```
--------------------------------------------------
استبيان مقرر برمجة شيئية - 2023(1-13).xlsx
number of students: 13
╒═══╤══════════════════════════════╤═══════╕
│ 0 │ x مخرجات التعليم المستهدفة x         │ 82.1% │
├───┼──────────────────────────────┼───────┤
│ 1 │ x المقرر والكتاب x                │ 64.1% │
├───┼──────────────────────────────┼───────┤
│ 2 │ x وسائل وطرق التقييم x             │ 66.7% │
├───┼──────────────────────────────┼───────┤
│ 3 │ x المحاضر x                    │ 75.6% │
├───┼──────────────────────────────┼───────┤
│ 4 │ x التعليم الهجين x                 │ 54.7% │
├───┼──────────────────────────────┼───────┤
│ 5 │ x الهيئة المعاونة (العملى) x          │ 87.2% │
├───┼──────────────────────────────┼───────┤
│ 6 │ x النتيجة x                      │ 71.7% │
╘═══╧══════════════════════════════╧═══════╛
```
