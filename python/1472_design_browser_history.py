class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] # stack
        self.forward_history = [] # stack

    def visit(self, url: str) -> None:
        self.forward_history.clear()
        self.history.append(url)

    def back(self, steps: int) -> str:
        while len(self.history) > 1 and steps > 0:
            self.forward_history.append(self.history.pop())
            steps -= 1

        return self.history[-1]

    def forward(self, steps: int) -> str:
        while self.forward_history and steps > 0:
            self.history.append(self.forward_history.pop())
            steps -= 1

        return self.history[-1]
