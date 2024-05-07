import pandas as pd
import json
import re
from uuid import uuid4
import time


def parse_questions_answers(data):
    # 正则表达式用于匹配问题和答案
    pattern = re.compile(r'Question: (.*?) Answer: (Yes|No)')

    results = []
    for entry in data:
        # 使用正则表达式查找所有匹配的问题-答案对
        matches = pattern.findall(entry)
        for question, answer in matches:
            result = {
                "id": str(uuid4()),  # 生成唯一标识符
                "Question": question.strip(),
                "Answer": answer.strip(),
                "tag": "finance"  # 假设添加额外的标签信息
            }
            results.append(result)
    return results


def main():
    # 开始计时
    start_time = time.time()

    # 读取数据集
    df = pd.read_csv('path_to_dataset.csv')  # 读取实际的数据集
    input_data = df['input_column_name'].tolist()  # 读取实际的列名

    # 解析问题和答案
    formatted_data = parse_questions_answers(input_data)

    # 保存结果为JSON文件
    with open('output.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)

    # 结束计时并计算总耗时
    elapsed_time = time.time() - start_time

    # 打印统计信息和性能指标
    print(f'Total number of question-answer pairs: {len(formatted_data)}')
    print(f'Time taken to complete the dataset cleanup and transformation: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
