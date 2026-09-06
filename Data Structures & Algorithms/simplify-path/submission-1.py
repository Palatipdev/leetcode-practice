class Solution:
    def simplifyPath(self, path: str) -> str:
        # using while loop
        # if a single / found, continue until a character is found
        # if a single . found, concacenate to check the length
        # if a char is found, concacinate until / . is found
        # should take single pass, O(n)
        # sidenote: above is the bruteforce but this feels like a sliding window question

        output = ""

        splitPath = path.split("/")
        stack = []
       
        for block in splitPath:
            if block == "" or block == ".":
                continue
            elif block == "..":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(block)

        if not stack:
            return "/"

        for block in stack:
            output += "/" + block

        return output
        