import unittest
from py_static_gen.parentnode import ParentNode
from py_static_gen.leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag_raises(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode must have a tag")

    def test_to_html_no_children_raises(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode must have children")

    def test_to_html_empty_children_list_raises(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode must have children")

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("b", "two")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><span>one</span><b>two</b></div>")

    def test_nested_parent_and_leaf_nodes(self):
        leaf1 = LeafNode("i", "italic")
        leaf2 = LeafNode("u", "underline")
        inner_parent = ParentNode("p", [leaf1, leaf2])
        outer_parent = ParentNode("div", [inner_parent])
        self.assertEqual(
            outer_parent.to_html(),
            "<div><p><i>italic</i><u>underline</u></p></div>"
        )
