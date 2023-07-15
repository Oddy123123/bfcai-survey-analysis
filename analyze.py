import numpy as np
import pandas as pd
import os
import argparse
from tabulate import tabulate
from IPython.display import display
from IPython import get_ipython

def get_questions(has_ta, has_ta2):

    Questions = {
        'مخرجات التعليم المستهدفة': 
        [
            [
                'المقرر له اهداف واضحة ومعلنة',
                'المقرر ينمي القدرة على التفكير والابتكار', 
                'المقرر يزودني بالمعرفة المفيدة والفهم المتعلق بالموضوع',
                'يجمع المقرر بين الجانب النظري والتطبيقي',
            ], 0
        ],

        'المقرر والكتاب':
        [
            [
                'محتويات المقرر تتناسب مع الوقت المخصص',
                'تتوافر المراجع بمكتبة الكلية أو بأحد الصور الإلكترونية الأخرى'
            ], 0
        ],

        'وسائل وطرق التقييم':
        [
            [
                'الامتحانات تعكس محتوى المقرر وتشتمل على الجوانب النظرية والعملية',
                'تعتبر اللغة المستخدمة في الامتحانات واضحة ومفهومة',
                'لا تتضمن الامتحانات اخطاء مطبعية'
            ], 0
        ],

        'المحاضر':
        [
            [
                'قام المحاضر بشرح محتويات المقرر وطرق التقييم عند بدء الدراسة',
                'مدى وضوح أسلوب عرض المحاضر للمادة العلمية للمقرر',
                'التزم المحاضر بحضور المحاضرات في مواعيدها وطبقا للجدول المعلن',
                'اهتم المحاضر بالربط بين المادة العلمية والتطبيقات العملية لموضوعات المقرر',
                'استخدم المحاضر وسائل تعليمية متنوعة ومناسبة لشرح المقرر',
                'شجع المحاضر علي المناقشة والتعليق وإلقاء الأسئلة والرد عليها',
                'مدى قدرة المحاضر على إدارة وضبط المحاضرة',
                'يساوى المحاضر في التعامل مع جميع الطلاب',
                'يلتزم المحاضر بالتواجد في مكتبه في الساعات المكتبية للتواصل مع الطلاب',
                'هل ترغب في دراسة مقررات أخرى مع نفس المحاضر مستقبلا؟'
            ], 0
        ],

        'التعليم الهجين':
        [
            [
                'مستوى الرضا عن التعليم الهجين',
                'مدى مساهمة نظام التعليم الهجين بفعالية في نجاح العملية التعليمية',
                'مدى فعالية دور وحدة الخدمات التكنولوجية IT Unit  في حل المشكلات التقنية',
            ], 0
        ]
    }


    if has_ta:
        Questions['الهيئة المعاونة (العملى)'] = [
            [
                'التزم المعيد بحضور الفصول والمعامل في مواعيدها',
                'يشجع المعيد على العمل في مجموعات طلابية أثناء التمارين والعملي',
                'يساوى المعيد في التعامل مع جميع الطلاب',
                'يتناول المعيد موضوعات تغطي الجانب العملي والتطبيقي للمقرر',
                'يستثمر المعيد وقت الفصول والمعامل في الشرح والمناقشة ويوفر التطبيقات الكافية',
                'هل ترغب في دراسة مقررات أخرى مع نفس المعيد مستقبلا؟'
            ], 0
        ]

    if has_ta2:
        Questions['الهيئة المعاونة (التمارين)'] = [
            [
                'التزم المعيد بحضور الفصول والمعامل في مواعيدها' + '2',
                'يشجع المعيد على العمل في مجموعات طلابية أثناء التمارين والعملي' + '2',
                'يساوى المعيد في التعامل مع جميع الطلاب' + '2',
                'يتناول المعيد موضوعات تغطي الجانب العملي والتطبيقي للمقرر' + '2',
                'يستثمر المعيد وقت الفصول والمعامل في الشرح والمناقشة ويوفر التطبيقات الكافية' + '2',
                'هل ترغب في دراسة مقررات أخرى مع نفس المعيد مستقبلا؟' + '2'
            ], 0
        ]
        
    return Questions


def analyze(file_name, course_type):
    '''
        - file_name (str): Path to .xlsx file that has the survey responses
        - course_type (int): 1 = lecture only, 2 = lecture + lab, 3 = lecture + lab + exercise 
    '''
    if not os.path.exists(file_name):
        raise ValueError('File not found "{}"'.format(file_name))
    
    if course_type not in [1, 2, 3]:
        raise ValueError('Invalid course_type value')
    
    data = pd.read_excel(file_name)      
    has_ta = False
    has_ta2 = False
    if course_type == 2:
        has_ta = True
    if course_type == 3:
        has_ta = True
        has_ta2 = True
    
    Questions = get_questions(has_ta, has_ta2)
    
    for cat in Questions:
        Questions[cat][1] = 0

        
    data_formated = []

    for col in data.columns[6:]:
        total = data[col].count()
        question = col
        strongly_agree = (data[col].astype(str).str.strip() == 'موافق بشدة').sum()
        agree = (data[col].astype(str).str.strip() == 'موافق').sum()
        maybe = (data[col].astype(str).str.strip() == 'إلى حد ما').sum()
        disagree = (data[col].astype(str).str.strip() == 'غير موافق').sum()
        strongly_disagree = (data[col].astype(str).str.strip() == 'غير موافق بشدة').sum()

        nums = [question, strongly_agree, agree, maybe, disagree, strongly_disagree, 0]
        data_formated.append(nums)

        perc = np.array([0, strongly_agree, agree, maybe, disagree, strongly_disagree])
        if total != 0:
            perc = perc / total
        perc = np.round(perc*100, 1)

        weights = np.array([3, 2, 1, 0, -1])
        count = nums[1:-1]
        result = 0
        if sum(count) != 0:
            result = weights.dot(count) / sum(count) / max(weights) * 100
        result = np.round(result, 1)
        
        for cat in Questions:
            if col.strip() in Questions[cat][0]:
                Questions[cat][1] += result
                
        

        perc = perc.tolist()
        perc.append(result)
        perc = [x.replace('.0', '') + '%' for x in np.array(perc).astype('str')]

        data_formated.append(perc)

    df = pd.DataFrame(data=data_formated, columns=['السؤال',
                                                   'موافق بشدة',
                                                   'موافق',
                                                   'إلى حد ما',
                                                   'غير موافق', 
                                                   'غير موافق بشدة', 
                                                   'النتيجة'
                                                  ])
    df = df.replace(0, '')
    df = df.replace('0.0', '')
    df = df.replace('0%', '')
    df = df.replace('nan%', '')
    
    name = os.path.basename(file_name)
    df.to_excel('2'+name, index=False)
    

    final_results = []
    for cat in Questions:
        total_result = np.round(Questions[cat][1] / len(Questions[cat][0]), 1)
        final_results.append([cat, total_result])
    final_results.append(['النتيجة', np.round(np.average([x[1] for x in final_results]), 1)])
    
    final_results = [[x, str(y) + '%'] for x, y in final_results]
    df_results = pd.DataFrame(final_results, columns = ['السؤال', 'النسبة'])
    print('-'*50)
    print(name)
    print('number of students:', len(data))
    
    if get_ipython() is not None:
        display(df_results)
    else:
        df_results['السؤال'] = 'x ' + df_results['السؤال'] + ' x'
        print(tabulate(df_results, tablefmt='fancy_grid'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", 
        help="Path to xlsx file that contains survey responses",
    )
    parser.add_argument(
        "course_type", 
        help=("An integer indicating the course type: 1 = lecture only, "
              "2 = lecture + lab, 3 = lecture + lab + exercise"),
        choices=(1, 2, 3),
        type=int,
    )
    args = parser.parse_args()
    analyze(args.path, args.course_type)

if __name__=='__main__':
    main()