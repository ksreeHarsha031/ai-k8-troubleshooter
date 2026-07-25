from dataclasses import dataclass, field
from planner.intent import Intent


@dataclass
class Action:
    intent: Intent
    resource_name: str | None = None
    namespace: str = "default"
    tools: list[str] = field(default_factory=list)