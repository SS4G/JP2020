class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        outputs = []
        self.generateHelper(n, (0, 0), stack, outputs)
        return outputs

    def generateHelper(self, n, state, stack, outputs):
        "last_state ('(', ')')"
        # try to add )
        if state[1] < state[0]:
            stack.append(')')
            self.generateHelper(n, (state[0], state[1] + 1), stack, outputs)
            stack.pop()

        # try to add (
        if state[0] < n:
            stack.append('(')
            self.generateHelper(n, (state[0] + 1, state[1]), stack, outputs)
            stack.pop()

        if len(stack) == 2 * n:
            outputs.append("".join(stack))
