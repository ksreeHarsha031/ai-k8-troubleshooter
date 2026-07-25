from enum import Enum


class Intent(Enum):
    LIST_PODS = "list_pods"
    DESCRIBE_POD = "describe_pod"
    GET_LOGS = "get_logs"
    ANALYZE_POD = "analyze_pod"
    UNKNOWN = "unknown"