import csv
import random

# 读取题库文件
def load_questions(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 6:  # 确保每行有6列数据
                questions.append({
                    "question": row[0],
                    "options": row[1:5],
                    "answer": row[5].strip().upper()
                })
    return questions

# 显示题目并判断答案
def start_quiz(questions):
    random.shuffle(questions)  # 随机打乱题目
    used_questions = set()
    correct_answers = 0
    incorrect_answers = 0
    
    for idx, q in enumerate(questions, start=1):
        if idx in used_questions:
            continue
        used_questions.add(idx)
        print(f"\n题目 {idx}: {q['question']}")
        for i, option in enumerate(q['options'], start=1):
            print(f"{chr(64 + i)}. {option}")

        user_answer = input("请输入你的答案 (A/B/C/D): ").strip().upper()
        if user_answer == q['answer']:
            correct_answers += 1
            print(f"回答正确！已正确回答 {correct_answers} 个题目！")
        else:
            incorrect_answers += 1
            print(f"回答错误！已回答错误 {incorrect_answers} 个题目！正确答案是: {q['answer']}")

# 主函数
if __name__ == "__main__":
    file_path = 'E:\Desktop\English\questions.csv'.strip()
    try:
        questions = load_questions(file_path)
        if questions:
            print(f"成功加载了 {len(questions)} 道题目。开始刷题！")
            start_quiz(questions)
        else:
            print("题库为空，请检查文件内容！")
    except FileNotFoundError:
        print("未找到题库文件，请检查文件路径！")
    except Exception as e:
        print(f"发生错误: {e}")
