class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        results = []
        ball_colors = {}  # Stores only balls that have been assigned a color
        color_counts = {}  # Stores color frequencies
        non_zero_colors = 0  # Count of colors with at least one ball

        for ball, new_color in queries:
            old_color = ball_colors.get(ball, 0)

            if old_color != new_color:
                # Remove old color count
                if old_color in color_counts:
                    color_counts[old_color] -= 1
                    if color_counts[old_color] == 0:
                        del color_counts[old_color]
                        non_zero_colors -= 1

                # Add new color count
                if new_color != 0:
                    if new_color not in color_counts:
                        color_counts[new_color] = 0
                        non_zero_colors += 1
                    color_counts[new_color] += 1

                # Update ball color
                if new_color == 0:
                    ball_colors.pop(ball, None)  # Remove ball if its color is 0
                else:
                    ball_colors[ball] = new_color

            results.append(non_zero_colors)

        return results
