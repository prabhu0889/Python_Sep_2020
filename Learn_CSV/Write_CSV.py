import csv

with open('test.csv', 'w', newline="") as f:
    write = csv.writer(f)

    heading = ['Roll_Num', 'Email', 'Ph']
    write.writerow(heading)

    data = [
            [1, 'g@gmail.com', 123],
            [2, 'b@gmail.com', 456],
            [3, 's@gmail.com', 789]
            ]
    write.writerows(data)