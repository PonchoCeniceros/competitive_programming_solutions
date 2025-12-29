from typing import List
import re


#
# Exercise 241
#
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # algoritmo recursivo
        def solver(E, Ops):
            if len(E) == 1:
                return E

            ans = []
            for i, op in enumerate(Ops):
                for x in solver(E[0 : i + 1], Ops[0:i]):
                    for y in solver(E[i + 1 : len(E)], Ops[i + 1 : len(Ops)]):
                        ans.append(
                            x + y if op == "+" else (x - y if op == "-" else x * y)
                        )
            return ans

        # procesar la entrada
        tokens = re.findall(r"(?:[1-9][0-9]|[0-9])|[+\-*]", expression)
        E = [int(t) for t in tokens if t not in ["+", "-", "*"]]
        Ops = [t for t in tokens if t in ["+", "-", "*"]]

        # implementacion de la funcion
        return E if len(E) == 1 else solver(E, Ops)


if __name__ == "__main__":
    solver = Solution()
    print("✅", solver.diffWaysToCompute(expression="11"))
    print("✅", solver.diffWaysToCompute(expression="2-1-1"))
    print("✅", solver.diffWaysToCompute(expression="2*3-4*5"))
