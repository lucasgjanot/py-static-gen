import unittest
from py_static_gen.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr_format(self):
        node = HTMLNode("h1","Teste")
        self.assertEqual(repr(node), "HTMLNode(h1, Teste, children: None, None)")


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        cases = [
        ("p", "This is a paragraph of text.", None, "<p>This is a paragraph of text.</p>"),
        ("a", "Click me!", {"href": "https://www.google.com"}, '<a href="https://www.google.com">Click me!</a>'),
        ]
        for tag, value, props,expected in cases:
            with self.subTest(tag=tag, value=value,props=props):
                leaf = LeafNode(tag, value, props)
                self.assertEqual(leaf.to_html(), expected)
    
    def test_to_html_no_value(self):
        leaf=LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf.to_html()
        
    def test_to_html_no_tag(self):
        leaf=LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "This is a paragraph of text.")
        

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


if __name__ == "__main__":
    unittest.main()