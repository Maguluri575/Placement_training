class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftCount = 0


class BST:

    # =========================================================
    # 1. INSERT
    # =========================================================

    def insert(self, root, val):

        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
            root.leftCount += 1

        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root

    # =========================================================
    # 2. INORDER
    # =========================================================

    def helper(self, root, res):

        if root is None:
            return

        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    def inorderTraversal(self, root):

        res = []
        self.helper(root, res)
        return res

    # =========================================================
    # 3. PREORDER
    # =========================================================

    def preorder(self, root, res):

        if root is None:
            return

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def preorderTraversal(self, root):

        res = []
        self.preorder(root, res)
        return res

    # =========================================================
    # 4. POSTORDER
    # =========================================================

    def postorder(self, root, res):

        if root is None:
            return

        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root):

        res = []
        self.postorder(root, res)
        return res

    # =========================================================
    # 5. LEVEL ORDER TRAVERSAL
    # =========================================================

    def levelOrder(self, root):

        if root is None:
            return []

        queue = [root]
        result = []

        while queue:

            temp = queue.pop(0)

            result.append(temp.val)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

        return result

    # =========================================================
    # 6. COUNT NODES
    # =========================================================

    def countNodes(self, root):

        if root is None:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right

    # =========================================================
    # 7. LEAF NODES
    # =========================================================

    def getLeaves(self, root, leaves):

        if root is None:
            return

        # Leaf node
        if root.left is None and root.right is None:
            leaves.append(root.val)
            return

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)

    # =========================================================
    # 8. NON-LEAF NODES
    # =========================================================

    def getNonLeaves(self, root, nonLeaves):

        if root is None:
            return

        # If it is a leaf, return
        if root.left is None and root.right is None:
            return

        nonLeaves.append(root.val)

        self.getNonLeaves(root.left, nonLeaves)
        self.getNonLeaves(root.right, nonLeaves)

    # =========================================================
    # 9. SUM
    # =========================================================

    def sumValues(self, root):

        if root is None:
            return 0

        return (
            root.val
            + self.sumValues(root.left)
            + self.sumValues(root.right)
        )

    # =========================================================
    # 10. MIN AND MAX
    # =========================================================

    def maxminValues(self, root):

        if root is None:
            return None, None

        min_value = root.val
        max_value = root.val

        left_min, left_max = self.maxminValues(root.left)
        right_min, right_max = self.maxminValues(root.right)

        if left_min is not None:
            min_value = min(min_value, left_min)
            max_value = max(max_value, left_max)

        if right_min is not None:
            min_value = min(min_value, right_min)
            max_value = max(max_value, right_max)

        return min_value, max_value

    # =========================================================
    # 11. LEFT VIEW
    # =========================================================

    def leftview(self, root):

        if root is None:
            return []

        queue = [root]
        result = []

        while queue:

            n = len(queue)

            for i in range(n):

                temp = queue.pop(0)

                if i == 0:
                    result.append(temp.val)

                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)

        return result

    # =========================================================
    # 12. RIGHT VIEW
    # =========================================================

    def rightview(self, root):

        if root is None:
            return []

        queue = [root]
        result = []

        while queue:

            n = len(queue)

            for i in range(n):

                temp = queue.pop(0)

                if i == n - 1:
                    result.append(temp.val)

                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)

        return result

    # =========================================================
    # 13. BOUNDARY VIEW
    # =========================================================

    def leftBoundary(self, node, result):

        if node is None:
            return

        if node.left is not None:
            result.append(node.val)
            self.leftBoundary(node.left, result)

        elif node.right is not None:
            result.append(node.val)
            self.leftBoundary(node.right, result)

    def getBoundaryLeaves(self, node, result):

        if node is None:
            return

        if node.left is None and node.right is None:
            result.append(node.val)
            return

        self.getBoundaryLeaves(node.left, result)
        self.getBoundaryLeaves(node.right, result)

    def rightBoundary(self, node, result):

        if node is None:
            return

        if node.right is not None:
            self.rightBoundary(node.right, result)
            result.append(node.val)

        elif node.left is not None:
            self.rightBoundary(node.left, result)
            result.append(node.val)

    def boundarynodes(self, root):

        if root is None:
            return []

        # Special case: root itself is a leaf
        if root.left is None and root.right is None:
            return [root.val]

        result = []

        # Root
        result.append(root.val)

        # Left boundary
        self.leftBoundary(root.left, result)

        # Leaves
        self.getBoundaryLeaves(root.left, result)
        self.getBoundaryLeaves(root.right, result)

        # Right boundary
        self.rightBoundary(root.right, result)

        return result

    # =========================================================
    # 14. LCA
    # =========================================================

    def lcs(self, root, n1, n2):

        if root is None:
            return None

        if n1 < root.val and n2 < root.val:
            return self.lcs(root.left, n1, n2)

        if n1 > root.val and n2 > root.val:
            return self.lcs(root.right, n1, n2)

        return root

    # =========================================================
    # 15. ZIGZAG TRAVERSAL
    # =========================================================

    def zigzagTraversal(self, root):

        if root is None:
            return []

        queue = [root]
        flag = True
        result = []

        while queue:

            size = len(queue)
            level = [0] * size

            for i in range(size):

                temp = queue.pop(0)

                if flag:
                    index = i
                else:
                    index = size - 1 - i

                level[index] = temp.val

                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)

            result.extend(level)

            flag = not flag

        return result

    # =========================================================
    # 16. VALIDATE BST
    # =========================================================

    def isValidBST(self, root):

        return self.validate(root, float("-inf"), float("inf"))

    def validate(self, root, minimum, maximum):

        if root is None:
            return True

        if root.val <= minimum or root.val >= maximum:
            return False

        return (
            self.validate(root.left, minimum, root.val)
            and
            self.validate(root.right, root.val, maximum)
        )

    # =========================================================
    # 17. KTH SMALLEST
    # =========================================================

    def kthSmallest(self, root, k):

        while root is not None:

            if k == root.leftCount + 1:
                return root.val

            elif k <= root.leftCount:
                root = root.left

            else:
                k = k - (root.leftCount + 1)
                root = root.right

        return -1

    # =========================================================
    # 18. SORTED ARRAY TO BST
    # =========================================================

    def sortedArrayToBST(self, nums):

        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, low, high):

        if low > high:
            return None

        mid = low + (high - low) // 2

        root = TreeNode(nums[mid])

        # Number of elements on left side
        root.leftCount = mid - low

        root.left = self.build(nums, low, mid - 1)
        root.right = self.build(nums, mid + 1, high)

        return root

    # =========================================================
    # 19. DELETE NODE
    # =========================================================

    def deleteNode(self, root, key):

        if root is None:
            return None

        if key < root.val:

            root.left = self.deleteNode(root.left, key)

            # Decrease leftCount only if a node was actually deleted
            if root.leftCount > 0:
                root.leftCount -= 1

        elif key > root.val:

            root.right = self.deleteNode(root.right, key)

        else:

            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            successor = self.getMin(root.right)

            root.val = successor.val

            root.right = self.deleteNode(
                root.right,
                successor.val
            )

        return root

    def getMin(self, node):

        while node.left is not None:
            node = node.left

        return node

    # =========================================================
    # 20. SERIALIZE
    # =========================================================

    def serialize(self, root):

        if root is None:
            return ""

        result = []

        self.preorder(root, result)

        return ",".join(map(str, result))

    # =========================================================
    # 21. DESERIALIZE
    # =========================================================

    def deserialize(self, data):

        if data is None or data == "":
            return None

        values = list(map(int, data.split(",")))

        index = [0]

        return self.buildBST(
            values,
            index,
            float("-inf"),
            float("inf")
        )

    def buildBST(self, values, index, minimum, maximum):

        if index[0] >= len(values):
            return None

        value = values[index[0]]

        if value <= minimum or value >= maximum:
            return None

        root = TreeNode(value)

        index[0] += 1

        root.left = self.buildBST(
            values,
            index,
            minimum,
            value
        )

        root.right = self.buildBST(
            values,
            index,
            value,
            maximum
        )

        # Calculate leftCount
        root.leftCount = self.countNodes(root.left)

        return root


# =============================================================
# MAIN PROGRAM
# =============================================================

def main():

    sol = BST()

    root = None
    data = ""

    while True:

        print("\nMenuuuuuu:")
        print(".............")
        print(
            "1.Insert , "
            "2.Inorder , "
            "3.Preorder , "
            "4.Postorder, "
            "5.Level Order Traversal, "
            "6.Count , "
            "7.Leaf Nodes, "
            "8.Non Leaf Nodes, "
            "9.Sum "
            "10.MinMax, "
            "11.LeftView , "
            "12.RightView, "
            "13.Boundary View, "
            "14.LCA , "
            "15.Zigzag , "
            "16.Validate BST , "
            "17.Kth Smallest , "
            "18.ArrayToBST , "
            "19.Delete Node , "
            "20.Serialize , "
            "21.Deserialize , "
            "22.Exit"
        )

        try:
            choice = int(input("\nEnter your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        # =====================================================
        # 1. INSERT
        # =====================================================

        if choice == 1:

            value = int(input("Enter value: "))

            root = sol.insert(root, value)

            print("Inserted:", value)

        # =====================================================
        # 2. INORDER
        # =====================================================

        elif choice == 2:

            print("Inorder:")
            print(sol.inorderTraversal(root))

        # =====================================================
        # 3. PREORDER
        # =====================================================

        elif choice == 3:

            print("Preorder:")
            print(sol.preorderTraversal(root))

        # =====================================================
        # 4. POSTORDER
        # =====================================================

        elif choice == 4:

            print("Postorder:")
            print(sol.postorderTraversal(root))

        # =====================================================
        # 5. LEVEL ORDER
        # =====================================================

        elif choice == 5:

            print("Level Order Traversal:")
            print(sol.levelOrder(root))

        # =====================================================
        # 6. COUNT
        # =====================================================

        elif choice == 6:

            print("Node Count:")

            totalNodes = sol.countNodes(root)

            print("Total number of nodes:", totalNodes)

        # =====================================================
        # 7. LEAF NODES
        # =====================================================

        elif choice == 7:

            print("Leaf Node:")

            leaves = []

            sol.getLeaves(root, leaves)

            print(leaves)

        # =====================================================
        # 8. NON-LEAF NODES
        # =====================================================

        elif choice == 8:

            print("Non Leaf Node:")

            nonLeaves = []

            sol.getNonLeaves(root, nonLeaves)

            print(nonLeaves)

        # =====================================================
        # 9. SUM
        # =====================================================

        elif choice == 9:

            print(
                "Sum of Node Values:",
                sol.sumValues(root)
            )

        # =====================================================
        # 10. MIN MAX
        # =====================================================

        elif choice == 10:

            print("Max and Min values:")

            minimum, maximum = sol.maxminValues(root)

            if root is None:
                print("Tree is empty.")
            else:
                print("Max:", maximum)
                print("Min:", minimum)

        # =====================================================
        # 11. LEFT VIEW
        # =====================================================

        elif choice == 11:

            print("Left View:")

            print(sol.leftview(root))

        # =====================================================
        # 12. RIGHT VIEW
        # =====================================================

        elif choice == 12:

            print("Right View:")

            print(sol.rightview(root))

        # =====================================================
        # 13. BOUNDARY VIEW
        # =====================================================

        elif choice == 13:

            print("Boundary View:")

            print(sol.boundarynodes(root))

        # =====================================================
        # 14. LCA
        # =====================================================

        elif choice == 14:

            print("LCS / LCA:")

            n1 = int(input("Enter No 1: "))
            n2 = int(input("Enter No 2: "))

            t = sol.lcs(root, n1, n2)

            if t is not None:
                print("LCA:", t.val)
            else:
                print("LCA Not Found")

        # =====================================================
        # 15. ZIGZAG
        # =====================================================

        elif choice == 15:

            print("Zigzag Traversal:")

            print(sol.zigzagTraversal(root))

        # =====================================================
        # 16. VALIDATE BST
        # =====================================================

        elif choice == 16:

            print("Validate BST:")

            if sol.isValidBST(root):
                print("Tree is a VALID BST")
            else:
                print("Tree is NOT a BST")

        # =====================================================
        # 17. KTH SMALLEST
        # =====================================================

        elif choice == 17:

            print("Kth Smallest:")

            k = int(input("Enter k Value: "))

            result = sol.kthSmallest(root, k)

            if result == -1:
                print("Invalid k")
            else:
                print("Result:", result)

        # =====================================================
        # 18. ARRAY TO BST
        # =====================================================

        elif choice == 18:

            print("Sorted Array to BST:")

            arr = [10, 20, 30, 40, 50, 60, 70]

            root = sol.sortedArrayToBST(arr)

            result = sol.inorderTraversal(root)

            print(result)

        # =====================================================
        # 19. DELETE NODE
        # =====================================================

        elif choice == 19:

            print("Delete Node:")

            key = int(input("Enter value to delete: "))

            root = sol.deleteNode(root, key)

            print("After deletion:")

            print(sol.inorderTraversal(root))

        # =====================================================
        # 20. SERIALIZE
        # =====================================================

        elif choice == 20:

            print("Serialize:")

            data = sol.serialize(root)

            print("Serialized BST:")

            print(data)

        # =====================================================
        # 21. DESERIALIZE
        # =====================================================

        elif choice == 21:

            print("Deserialize:")

            if data == "":
                print("No serialized data available.")

            else:
                root = sol.deserialize(data)

                print("Inorder after deserialization:")

                print(sol.inorderTraversal(root))

        # =====================================================
        # 22. EXIT
        # =====================================================

        elif choice == 22:

            print("Exiting...")

            break

        else:

            print("Invalid choice. Please select 1-22.")


# =============================================================
# START PROGRAM
# =============================================================

if __name__ == "__main__":
    main()