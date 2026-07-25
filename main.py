from planner.planner import Planner

def main():
    print("\n🚀 Welcome to KubePilot")
    print("-" * 40)

    question = input("Ask me anything about your Kubernetes cluster:\n> ")

    planner = Planner()

    intent = planner.get_intent(question)

    print(f"\nIntent: {intent}")


if __name__ == "__main__":
    main()