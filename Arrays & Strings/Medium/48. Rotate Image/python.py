from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix: List[List[int]] = []

        for i in range(len(matrix)):
            lst: List[int] = []

            for j in range(len(matrix[i])):
                lst.append(matrix[j][i])

            new_matrix.append(lst)

        for i in range(len(new_matrix)):
            matrix[i] = new_matrix[i][::-1]
