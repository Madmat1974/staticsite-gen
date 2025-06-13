import unittest

from textnode import *
from splitdelimiter import *



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

    def test_text_textnode(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_list = text_to_textnodes(node)
        
        
        self.assertEqual(node_list,[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])


 

if __name__ == "__main__":
    unittest.main()