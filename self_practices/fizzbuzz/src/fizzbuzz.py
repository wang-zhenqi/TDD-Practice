import yaml


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def is_digit_present(number: int, digit: str) -> bool:
    return digit in str(number)


class ActionRules:
    definitions = None

    def __init__(self):
        self.load_definitions()

    def load_definitions(self):
        with open("../config.yaml") as f:
            self.definitions = yaml.load(f, Loader=yaml.FullLoader)

    def apply(self, number: int):
        candidates_effectiveness = {candidate: False for candidate in self.definitions.keys()}

        for candidate, rules in self.definitions.items():
            for rule in rules:
                take_action = globals()[rule["action"]]
                condition = rule["condition"]
                candidates_effectiveness[candidate] |= take_action(number, condition)

        return candidates_effectiveness


def produce_result(candidates_effectiveness_dict: dict[str, bool]) -> str:
    return "".join([candidate for candidate, is_effective in candidates_effectiveness_dict.items() if is_effective])


class NumberProcessor:
    def __init__(self, rules: ActionRules):
        self.action_rules = rules

    def process_number(self, number: int) -> str:
        candidates_effectiveness = self.action_rules.apply(number)

        result = produce_result(candidates_effectiveness)
        return result if result else str(number)


class Generator:
    def __init__(self, processor):
        self.processor = processor

    def generate(self) -> list[str]:
        return [self.processor.process_number(x) for x in range(1, 101)]


if __name__ == "__main__":
    number_processor = NumberProcessor(ActionRules())

    generator = Generator(number_processor)

    print(generator.generate())
