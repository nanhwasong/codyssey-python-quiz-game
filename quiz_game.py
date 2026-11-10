
"""퀴즈 게임의 진행과 점수를 관리하는 클래스."""

from quiz_data import get_default_quizzes


class QuizGame:
    """퀴즈 게임 전체를 관리한다."""

    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def get_number(self, message, minimum, maximum):
        """허용 범위의 정수를 입력받는다."""
        while True:
            value = input(message).strip()

            if not value:
                print("입력값이 없습니다. 번호를 입력해 주세요.")
                continue

            try:
                number = int(value)
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(f"{minimum}부터 {maximum}까지 입력해 주세요.")

    def play_quiz(self):
        """저장된 퀴즈를 풀고 점수를 계산한다."""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        print(f"\n총 {len(self.quizzes)}문제를 시작합니다!")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{len(self.quizzes)}]")
            quiz.display()

            answer = self.get_number("정답 번호 (1~4): ", 1, 4)

            if quiz.check_answer(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        total = len(self.quizzes)
        score = round(correct_count / total * 100)

        print("\n========== 퀴즈 결과 ==========")
        print(f"맞힌 문제: {correct_count}/{total}")
        print(f"점수: {score}점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")



    def add_quiz(self):
        """새로운 퀴즈를 입력받아 목록에 추가한다."""
        from quiz import Quiz

        print("\n========== 새 퀴즈 등록 ==========")

        while True:
            question = input("문제를 입력하세요: ").strip()
            if question:
                break
            print("문제는 비워둘 수 없습니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 선택지: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("선택지는 비워둘 수 없습니다.")

        answer = self.get_number("정답 번호 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("새로운 퀴즈가 등록되었습니다!")
        print(f"현재 등록된 퀴즈: {len(self.quizzes)}개")
