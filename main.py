
"""Python & Git 기초 퀴즈 게임의 실행 파일."""


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


def get_menu_choice():
    """1~5 사이의 메뉴 번호를 안전하게 입력받는다."""
    while True:
        user_input = input("\n메뉴 번호를 입력하세요 (1~5): ").strip()

        if not user_input:
            print("입력값이 없습니다. 번호를 입력해 주세요.")
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        if 1 <= choice <= 5:
            return choice

        print("1부터 5까지의 번호를 입력해 주세요.")


def main():
    """메뉴를 반복 실행하고 선택한 기능을 처리한다."""
    print("Python & Git 기초 퀴즈 게임에 오신 것을 환영합니다!")

    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 5:
                print("게임을 종료합니다. 감사합니다!")
                break
            elif choice == 1:
                print("퀴즈 풀기 기능은 다음 단계에서 구현합니다.")
            elif choice == 2:
                print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")
            elif choice == 3:
                print("퀴즈 목록 기능은 다음 단계에서 구현합니다.")
            elif choice == 4:
                print("최고 점수 확인 기능은 다음 단계에서 구현합니다.")

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
