package hackerrank

import "fmt"

func inOrder(Node *root) {
	if root == nil {
		return
	}
	inOrder(root.left)
	fmt.Printf("%d ", root.data)
	inOrder(root.right)
}
