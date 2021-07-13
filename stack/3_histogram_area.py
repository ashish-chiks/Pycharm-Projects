# Given an array denoting length of bars in a histogram.
# print the max area of rectangle in histogram.


def MAH(histogram):
    stack = list()
    max_area = 0
    index = 0
    while index < len(histogram):

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))

            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))

        max_area = max(max_area, area)

    return max_area


hist = [6, 2, 5, 4, 5, 1, 6]
print(MAH(hist))
