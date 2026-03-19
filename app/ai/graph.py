from langgraph.graph import END, StateGraph

from app.ai.state import MatchState
from app.services.job_text_processor import prepare_job_description_for_extraction
from app.services.matcher import compare_skills
from app.services.recommender import generate_recommendation
from app.services.skill_extractor import extract_skills_from_text
from app.services.text_cleaner import clean_extracted_text


def clean_texts_node(state: MatchState) -> MatchState:
    return {
        **state,
        "cv_text": clean_extracted_text(state["cv_text"]),
        "job_description": clean_extracted_text(state["job_description"]),
    }


def prepare_job_description_node(state: MatchState) -> MatchState:
    prepared_job_description = prepare_job_description_for_extraction(state["job_description"])
    return {
        **state,
        "prepared_job_description": prepared_job_description,
    }


def extract_cv_skills_node(state: MatchState) -> MatchState:
    cv_skills = extract_skills_from_text(state["cv_text"])
    return {
        **state,
        "cv_skills": cv_skills,
    }


def extract_job_skills_node(state: MatchState) -> MatchState:
    job_skills = extract_skills_from_text(state["prepared_job_description"])
    return {
        **state,
        "job_skills": job_skills,
    }


def compare_skills_node(state: MatchState) -> MatchState:
    comparison = compare_skills(state["cv_skills"], state["job_skills"])
    return {
        **state,
        "matched_skills": comparison["matched_skills"],
        "missing_skills": comparison["missing_skills"],
        "match_score": comparison["match_score"],
    }


def recommendation_node(state: MatchState) -> MatchState:
    recommendation = generate_recommendation(
        state["match_score"],
        state["missing_skills"]
    )
    return {
        **state,
        "recommendation": recommendation,
    }


def build_match_graph():
    graph = StateGraph(MatchState)

    graph.add_node("clean_texts", clean_texts_node)
    graph.add_node("prepare_job_description", prepare_job_description_node)
    graph.add_node("extract_cv_skills", extract_cv_skills_node)
    graph.add_node("extract_job_skills", extract_job_skills_node)
    graph.add_node("compare_skills", compare_skills_node)
    graph.add_node("recommendation", recommendation_node)

    graph.set_entry_point("clean_texts")
    graph.add_edge("clean_texts", "prepare_job_description")
    graph.add_edge("prepare_job_description", "extract_cv_skills")
    graph.add_edge("extract_cv_skills", "extract_job_skills")
    graph.add_edge("extract_job_skills", "compare_skills")
    graph.add_edge("compare_skills", "recommendation")
    graph.add_edge("recommendation", END)

    return graph.compile()


match_graph = build_match_graph()