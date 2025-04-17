import json
from app.recommender import recommend_assessments

def test_assessment_data_exists():
    with open("app/data/assessments.json") as f:
        data = json.load(f)
    assert len(data) >= 20, f"Expected at least 20 assessments, but got {len(data)}"


def test_recommendation_results():
    query = "Looking for a test to measure analytical and cognitive skills in under 30 minutes."
    results = recommend_assessments(query)

    assert len(results) > 0, "No recommendations returned!"
    
    for r in results:
        print(f"{r['name']} ({r.get('duration', 'N/A')}) - {r['type']}")
        print(f"URL: {r['url']}")
        print(f"Remote Support: {r['remote_support']} | Adaptive: {r['adaptive_support']}")
        print("---")
