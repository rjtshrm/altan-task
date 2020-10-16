import task2

intervals = [
    [[1, 9], [11, 20], [2, 10], [3, 19]],
    [[4, 3], [1, 10], [2, 4], [4, 7]],
    [[25, 30], [2, 19], [14, 23], [4, 8]]
]

intervals_result = [
    [[1, 20]],
    [[1, 10]],
    [[2, 23], [25, 30]]
]

class Test_Task_2:
    def test(self):
        for idx, ir in enumerate(zip(intervals, intervals_result)):
            i, r = ir
            op = task2.merge_intervals(i)
            assert op == r
            print('Test {0} cases passed'.format(idx))


Test_Task_2().test()







