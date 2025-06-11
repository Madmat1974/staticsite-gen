import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_unequaltext(self):
        node = TextNode("This is the correct node", TextType.ITALIC)
        node2 = TextNode("This is not the correct node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_missingurl(self):
        node = TextNode("I have an url", TextType.LINK, "https:www.boot.dev/")
        node2 = TextNode("I have an url", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_differenttype(self):
        node = TextNode("Yes i am awesome", TextType.BOLD)
        node2 = TextNode("Yes i am awesome", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()