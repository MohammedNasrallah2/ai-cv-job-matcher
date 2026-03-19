def compare_skills(cv_skills: list[str], job_skills: list[str]) -> dict:
    cv_set = set(cv_skills)
    job_set = set(job_skills)

    matched_skills = sorted(cv_set.intersection(job_set))
    missing_skills = sorted(job_set.difference(cv_set))

    if job_skills:
        match_score = round((len(matched_skills) / len(job_set)) * 100, 2)
    else:
        match_score = 0.0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score
    }