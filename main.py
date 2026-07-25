from planner.planner import Planner
from kubernetes.executor import KubernetesExecutor

def main():
    print("\n🚀 Welcome to KubePilot")
    print("-" * 40)

    question = input("Ask me anything about your Kubernetes cluster:\n> ")

    planner = Planner()

    action = planner.plan(question)

    print(action)

    executor = KubernetesExecutor()

    if action.intent.value == "list_pods":
        output = executor.execute(["kubectl", "get", "pods"])

        print(output)


if __name__ == "__main__":
    main()