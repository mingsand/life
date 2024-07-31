# 인생의 여정을 비유한 코드

class Journey:
    def __init__(self, name):
        self.name = name
        self.steps = []

    def take_step(self, description):
        self.steps.append(description)
        print(f"{self.name}가 한 걸음을 내딛었습니다: {description}")

    def reflect(self):
        print(f"\n{self.name}의 여정을 되돌아봅니다:")
        for i, step in enumerate(self.steps, 1):
            print(f"  {i}. {step}")

# 여정 시작
my_journey = Journey("내 인생")

# 걸음을 내딛다
my_journey.take_step("새로운 언어를 배우다")
my_journey.take_step("좋은 친구를 만나다")
my_journey.take_step("도전 과제를 해결하다")
my_journey.take_step("시작지점에서 휴식하다")

# 여정을 되돌아보다
my_journey.reflect()
