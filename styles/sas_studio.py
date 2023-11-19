# -*- coding: utf-8 -*-
"""
    pygments.styles.sas_studio
    ~~~~~~~~~~~~~~~~~~~

    Style inspired by SAS Studio. Note This is not meant to be a
    complete style. It's merely meant to mimic SAS Studio's syntax
    highlighting.

    :copyright: Copyright 2023 by Ruiyang Wu.
    :license: BSD, see LICENSE for details.

"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Other, Whitespace, Generic


class SasStudioStyle(Style):
    """
    Style inspired by SAS Studio. Note This is not meant to be a
    complete style. It's merely meant to mimic SAS Studio's syntax
    highlighting.
    """

    default_style = ''

    styles = {
        Whitespace:            '#bbbbbb',
        Comment:               'italic #008800',
        String:                '#800080',
        Number:                'bold #2e8b57',
        Other:                 '#8f7a47',
        Keyword:               '#2c2cff',
        Keyword.Reserved:      'bold #353580',
        Keyword.Constant:      'bold',
        Name.Builtin:          '#2c2cff',
        Name.Function:         'bold italic',
        Name.Variable:         'bold #2c2cff',
        Generic:               '#2c2cff',
        Generic.Emph:          '#008800',
        Generic.Error:         '#d30202',
        Error:                 'bg:#e3d2d2 #a61717'
    }
