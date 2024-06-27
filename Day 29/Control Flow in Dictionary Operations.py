def get_letter_grades(scores):
    def grade(avg):
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        elif avg >= 60: return 'D'
        else: return 'F'
    
    return {name: grade(sum(scores) / len(scores)) for name, scores in scores.items()}

# Example usage:
student_scores = {
    'Alice': [85, 90, 92],
    'Bob': [78, 80, 75],
    'Charlie': [90, 95, 98]
}
print(get_letter_grades(student_scores))
# Output: {'Alice': 'B', 'Bob': 'C', 'Charlie': 'A'}