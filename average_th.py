import pandas as pd
true_line_list = list()

with open('../data/crt_uniform_c.txt', 'r', encoding='utf-8') as crt_txt:
    for i in range(7 * (210 - 2)):
        # if len(crt_txt.readline()) == 0:
        #     continue
        str_line = crt_txt.readline()
        if str_line[0] == 'T' and str_line[1] == 'r':
            print()
            print(str_line)
            print(str_line.split(': ')[1])
            true_line_list.append(str_line.split(': ')[1])
        print(true_line_list)
        true_line_list = [float(num) for num in true_line_list]
        df = pd.DataFrame(true_line_list)
        df.to_csv('crt_uniform_c_232527_210_data.csv')
        print(true_line_list)

