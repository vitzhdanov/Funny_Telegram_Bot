from operator import itemgetter
test = [(1, 495432329, 'Vladislav', 162), (2, 495432322, 'Victor', 17), (2, 495432332, 'Vica', 24)]

sort_test = sorted(test, key=lambda x:x[3], reverse=True)


for i in range(len(sort_test)):
    print(f"{i+1} место: {sort_test[i][2]} - {sort_test[i][3]} нецензурных слов")