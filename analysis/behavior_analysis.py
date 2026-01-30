def stability_score(study_hours, mean_hours):
    return 1 / (1 + abs(study_hours - mean_hours))


def detect_mismatch(study_hours, exam_score, threshold=15):
    gap = study_hours - (exam_score / 10)
    return gap > threshold
