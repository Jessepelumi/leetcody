class Solution:
    def spiralMatrix(self, matrix):
        result = []

        row, col = len(matrix), len(matrix[0])

        t, b = 0, row - 1
        l, r = 0, col - 1

        while l <= r and t <= b:
            # Traverse top, l -> r
            for col in range(l, r + 1):
                result.append(matrix[t][col])
            t += 1

            # Traverse right, t -> b
            for row in range(t, b + 1):
                result.append(matrix[row][r])
            r -= 1

            # Traverse bottom, r -> l
            if t <= b:
                for col in range(r, l - 1, -1):
                    result.append(matrix[b][col])
                b -= 1

            # Traverse left, b -> t
            if l <= r:
                for row in range(b, t - 1, -1):
                    result.append(matrix[row][l])
                l += 1

        return result
