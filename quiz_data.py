
"""Python과 Git 기초 퀴즈 데이터."""

from quiz import Quiz


def get_default_quizzes():
    """기본 퀴즈 8개를 Quiz 객체 목록으로 반환한다."""
    return [
        Quiz(
            "Python에서 화면에 글자를 출력하는 함수는?",
            ["input()", "print()", "len()", "type()"],
            2,
        ),
        Quiz(
            "Python에서 사용자의 키보드 입력을 받는 함수는?",
            ["print()", "open()", "input()", "range()"],
            3,
        ),
        Quiz(
            "Python에서 여러 값을 순서대로 저장하는 자료형은?",
            ["int", "bool", "str", "list"],
            4,
        ),
        Quiz(
            "Python에서 조건에 따라 코드를 실행할 때 사용하는 키워드는?",
            ["if", "for", "def", "class"],
            1,
        ),
        Quiz(
            "Python에서 함수를 정의할 때 사용하는 키워드는?",
            ["return", "import", "def", "while"],
            3,
        ),
        Quiz(
            "Git 저장소를 처음 생성할 때 사용하는 명령어는?",
            ["git push", "git init", "git pull", "git clone"],
            2,
        ),
        Quiz(
            "Git에서 변경 사항을 커밋 대상으로 등록하는 명령어는?",
            ["git add", "git log", "git status", "git merge"],
            1,
        ),
        Quiz(
            "Git에서 로컬 커밋을 GitHub 원격 저장소로 업로드하는 명령어는?",
            ["git pull", "git clone", "git checkout", "git push"],
            4,
        ),
    ]
