
"""퀴즈와 최고 점수를 JSON 파일에 저장하고 불러온다."""

import json
from pathlib import Path

from quiz import Quiz
from quiz_data import get_default_quizzes


STATE_FILE = Path(__file__).with_name("state.json")


def load_state():
    """저장된 퀴즈와 최고 점수를 불러온다."""
    if not STATE_FILE.exists():
        return get_default_quizzes(), None

    try:
        with STATE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        quizzes = [
            Quiz.from_dict(item)
            for item in data["quizzes"]
        ]

        best_score = data["best_score"]

        if not isinstance(best_score, int) and best_score is not None:
            raise ValueError("최고 점수 형식 오류")

        if isinstance(best_score, bool) or (
            best_score is not None and not 0 <= best_score <= 100
        ):
            raise ValueError("최고 점수 범위 오류")

        return quizzes, best_score

    except (OSError, ValueError, TypeError, KeyError, UnicodeError) as error:
        print(f"저장 데이터를 읽을 수 없습니다: {error}")
        print("기본 퀴즈로 시작합니다.")
        return get_default_quizzes(), None


def save_state(quizzes, best_score):
    """현재 퀴즈와 최고 점수를 JSON 파일에 저장한다."""
    data = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score,
    }

    try:
        with STATE_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("데이터 저장 완료")
        return True

    except OSError as error:
        print(f"데이터 저장 실패: {error}")
        return False
