
class Quiz:
    """퀴즈 한 문제를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 빈 문자열일 수 없습니다.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")

        if any(
            not isinstance(choice, str) or not choice.strip()
            for choice in choices
        ):
            raise ValueError("선택지는 빈 문자열일 수 없습니다.")

        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답은 1부터 4까지의 숫자여야 합니다.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer

    def display(self):
        """문제와 선택지 출력"""
        print(f"\n문제: {self.question}")

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        """사용자가 선택한 번호가 정답인지 확인"""
        return self.answer == user_answer

    def to_dict(self):
        """Quiz 객체를 JSON 저장용 딕셔너리로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 Quiz 객체 복원"""
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

        return cls(
            data["question"],
            data["choices"],
            data["answer"],
        )
