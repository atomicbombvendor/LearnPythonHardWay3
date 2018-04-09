row_data = {}
with open("resource/PaceData.csv") as paces:
    column_heading = paces.readline().strip().split(',')
    column_heading.pop(0)

    for each_line in paces:
        row = each_line.strip().split(",")
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_heading)):
            inner_dict[row[i]] = column_heading[i]
        row_data
    num_cols = len(column_heading)
    print(num_cols, end=' -> ')
    print(column_heading)
    num_2mi = len(row_data['2mi'])
    print(num_2mi, end=' -> ')
    print(row_data['2mi'])
    num_Marathon = len(row_data['Marathon'])
    print(num_Marathon, end = ' -> ')
    print(row_data['Marathon'])