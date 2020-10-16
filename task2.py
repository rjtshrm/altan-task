# Algorithm (Merge Intervals)
# - Sort the interval by first element
# - Append the first interval to stack
# - For next interval check if it overlaps with the top interval in stack, if yes merge them


def merge_intervals(intervals):
    # Sort interval by first element
    sort_intervals_first_elem = sorted(intervals, key=lambda k: k[0])

    stack = []

    # stack iteration and interval operation
    for interval in sort_intervals_first_elem:
        if len(stack) == 0:
            stack.append(interval)
        else:
            f, e = interval
            tf, te = stack[-1]  # top element in stack

            if tf <= f <= te:
                # interval overlap each other
                stack[-1][1] = max(e, te)
            else:
                stack.append(interval)

    return stack


if __name__ == '__main__':
    intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
    print(merge_intervals(intervals))
