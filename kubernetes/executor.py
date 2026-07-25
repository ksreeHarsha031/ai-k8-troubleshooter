import subprocess


class KubernetesExecutor:

    def execute(self, command: list[str]) -> str:
        """
        Executes a kubectl command and returns the output.
        """

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )

            return result.stdout

        except subprocess.CalledProcessError as e:
            return e.stderr