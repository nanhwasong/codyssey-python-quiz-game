
"""Python & Git 기초 퀴즈 게임의 실행 파일."""

from quiz_game import QuizGame


def show_menu():
    """게임의 기본 메뉴를 보여준다."""
    print("\n" + "=" * 36)
    print("       Python & Git 퀴즈 게임")
    print("=" * 36)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")


def get_menu_choice(game):
    """안전하게 메뉴 번호를 입력받는다."""
    return game.get_number("\n메뉴 번호를 입력하세요 (1~5): ", 1, 5)


def main():
    """게임 메뉴 실행."""
    game = QuizGame()
    print("Python & Git 기초 퀴즈 게임에 오신 것을 환영합니다!")

    try:
        while True:
            show_menu()
            choice = get_menu_choice(game)

            if choice == 5:
                print("게임을 종료합니다. 감사합니다!")
                break
            elif choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                print("퀴즈 목록 기능은 다음 단계에서 구현합니다.")
            elif choice == 4:
                print("최고 점수 확인 기능은 다음 단계에서 구현합니다.")

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
