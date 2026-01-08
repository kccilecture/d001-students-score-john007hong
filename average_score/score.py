#!/usr/bin/env python
import sys
import csv
import os


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]


def subject_average(student_scores: dict, subjects: list):
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """
    avrg_dic = {}
    key_lst = student_scores.keys()
    sz_r = len(key_lst)
    sz_c = len(subjects)
    for sbj in subjects:
        idx = subjects.index(sbj)
        ttl = 0;
        for ky in key_lst:
            val_lst = student_scores[ky]
            ttl += int(val_lst[idx]);
        avrg = ttl / sz_r
        avrg_dic[sbj] = avrg
    return avrg_dic

def student_average(student_scores: dict):
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    avrg_lst = []
    key_lst = student_scores.keys()
    sz_r = len(key_lst)
    for ky in key_lst:
        val_lst = student_scores[ky]
        sz = len(val_lst)
        ttl = 0
        for val_str in val_lst:
            val = int(val_str)
            ttl += val
        avrg = ttl / sz
        avrg_lst.append((ky, avrg))
    
    sort_avrg_lst = sorted(avrg_lst, key=lambda x:x[1], reverse=True)
    return sort_avrg_lst

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print(f"USAGE: {sys.argv[0]} <csv_file>")
    #     sys.exit()
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    scv_path = dir_path + "/score.csv"
    if os.path.isfile(scv_path) == False:
        sys.exit()

    # student_scores, subjects = load_from_csv(sys.argv[1])
    student_scores, subjects = load_from_csv(scv_path)
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")
