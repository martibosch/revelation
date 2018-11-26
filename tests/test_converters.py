import shutil
import tempfile
from os import path
from unittest import TestCase

from revelation import converters, pandoc_config
from revelation.config import Config


class ConvertersTestCase(TestCase):
    def setUp(self):
        self.tests_folder = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tests_folder)

    def test_pandoc_converter(self):
        # ACHTUNG: `PandocConverter.convert` will require internet connection
        revealjs_url = 'https://revealjs.com'
        input_slides = 'example_slides/slides-pandoc.md'

        # TODO: test parameter values for `slide_level` and `theme` (check
        # pypandoc exceptions)
        config = Config()
        config.load_from_object(pandoc_config)
        pandoc_converter = converters.PandocConverter(
            revealjs_url=revealjs_url, config=config)

        # invalid input file path
        self.assertRaises(RuntimeError, pandoc_converter.convert,
                          'example_slides/inexisting.md')

        # test that we are outputting html
        output = pandoc_converter.convert(input_slides)
        assert 'doctype' in output.splitlines()[0].lower()

        # test that we are outputting a file
        tmp_fp = self.tests_folder + 'slides.html'
        pandoc_converter.convert(input_slides, output_fp=tmp_fp)

        assert path.exists(tmp_fp)
