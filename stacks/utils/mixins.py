from stacks import BuildLinkedStack


# Using Stack
# Time Complexity: O(N)
# Space Complexity: O(N)
class GreaterElementMixin:
    def __init__(self, arr: []):
        self.arr = arr
        self.intermediate_processing_stack = BuildLinkedStack().build()

    def get_ans_arr(self):
        raise NotImplementedError('Ans Array is Unknown')

    def get_arr_traversal(self):
        raise NotImplementedError('Input Array Traversal is Unknown')

    def _get_greater_elem(self):
        ans_arr = self.get_ans_arr()
        for elem in self.get_arr_traversal():
            while not self.intermediate_processing_stack.is_empty() and self.intermediate_processing_stack.top < elem:
                self.intermediate_processing_stack.pop()

            # Push next greater elem in stack if exists
            ans_arr.push(-1 if self.intermediate_processing_stack.is_empty() else self.intermediate_processing_stack.top)

            self.intermediate_processing_stack.push(elem)

        return ans_arr
