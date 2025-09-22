import unittest
from py_static_gen.inline_markdown import extract_markdown_links, extract_mark_down_images

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_mark_down_images(self):
        text = "This is an image ![alt text](http://example.com/image.png)"
        expected = [("alt text", "http://example.com/image.png")]
        self.assertEqual(extract_mark_down_images(text), expected)

    def test_extract_mark_down_images_multiple(self):
        text = "![img1](url1) and ![img2](url2)"
        expected = [("img1", "url1"), ("img2", "url2")]
        self.assertEqual(extract_mark_down_images(text), expected)

    def test_extract_mark_down_images_none(self):
        text = "No images here"
        expected = []
        self.assertEqual(extract_mark_down_images(text), expected)

    def test_extract_markdown_links(self):
        text = "Check this [link](http://example.com)"
        expected = [("link", "http://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_multiple(self):
        text = "[Link1](url1) and [Link2](url2)"
        expected = [("Link1", "url1"), ("Link2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_images(self):
        text = "![Image](img_url) and [Link](link_url)"
        expected = [("Link", "link_url")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_none(self):
        text = "No links here"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)