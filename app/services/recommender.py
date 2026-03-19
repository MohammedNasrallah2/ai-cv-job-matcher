def generate_recommendation(match_score: float, missing_skills: list[str]) -> str:
    if match_score >= 80:
        if missing_skills:
            return (
                f"Your CV is strongly aligned with the job, but you still need: "
                f"{', '.join(missing_skills)}."
            )
        return "Your CV is strongly aligned with the job requirements."

    if match_score >= 50:
        if missing_skills:
            return (
                f"Your CV is partially aligned with the job. "
                f"You should improve these skills: {', '.join(missing_skills)}."
            )
        return "Your CV is partially aligned with the job requirements."

    if missing_skills:
        return (
            f"Your CV is weakly aligned with the job. "
            f"The main missing skills are: {', '.join(missing_skills)}."
        )

    return "Your CV is weakly aligned with the job requirements."