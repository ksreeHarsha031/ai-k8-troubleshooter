from planner.intent import Intent


class Planner:

    def get_intent(self, question: str) -> Intent:

        question = question.lower()

        if "show" in question and "pods" in question:
            return Intent.LIST_PODS

        return Intent.UNKNOWN