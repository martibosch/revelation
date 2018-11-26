from . import utils


class PandocConverter:
    def __init__(self, revealjs_url='https://revealjs.com', config={}):
        self.revealjs_url = revealjs_url
        # this is a verbose way of providing defaults since a config file with
        # defaults for `PandocConverter` already exists at `pandoc_config.py`
        self.slide_level = config.get('REVEAL_SLIDE_LEVEL', 1)
        self.theme = config.get('REVEAL_THEME', 'black')
        self.transition = config.get('REVEAL_CONFIG', {}).get(
            'transition', 'default')

    def convert(self, slides_fp, output_fp=None):
        return utils.pandoc_convert(
            slides_fp, output_fp, revealjs_url=self.revealjs_url,
            theme=self.theme, transition=self.transition,
            slide_level=self.slide_level)

    convert.__doc__ = utils.pandoc_convert.__doc__
