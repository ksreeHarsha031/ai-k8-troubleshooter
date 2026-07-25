from tools.base_tool import BaseTool


class ListPodsTool(BaseTool):

    def execute(self, action):

        return """
NAME                  READY   STATUS              RESTARTS
payment-service       0/1     CrashLoopBackOff   12
user-service          1/1     Running            0
nginx                 1/1     Running            0
redis                 1/1     Running            0
"""