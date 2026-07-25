from models.action import Action
from planner.intent import Intent


class Planner:

    def plan(self, question: str) -> Action:

        question = question.lower()

        if "show" in question and "pods" in question:
            return Action(intent=Intent.LIST_PODS)

        if "crashing" in question:
            pod_name = question.split()[1]

            return Action(
                intent=Intent.ANALYZE_POD,
                resource_name=pod_name,
                tools=[
                    "describe_pod",
                    "get_logs",
                    "get_events"
                ]
            )

        return Action(intent=Intent.UNKNOWN)