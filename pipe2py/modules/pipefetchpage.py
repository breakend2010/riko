# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab
"""
pipe2py.modules.pipefetchpage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Provides functions for fetching web pages.

Fetches the source of a given web site as a string. This data can then be
converted into an RSS feed or merged with other data in your Pipe using the
`regex` module.

Examples:
    basic usage::

        >>> from pipe2py.modules.pipefetchpage import pipe
        >>> conf = {'url': FILES[5], 'start': '<title>', 'end': '</title>'}
        >>> pipe(conf=conf).next()['content']  # doctest: +ELLIPSIS
        u'CNN.com International - Breaking, World..., Entertainment and Video News'

Attributes:
    OPTS (dict): The default pipe options
    DEFAULTS (dict): The default parser options
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from urllib2 import urlopen
from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.web.client import getPage

from . import processor, FEEDS, FILES
from pipe2py.lib import utils
from pipe2py.lib.log import Logger
from pipe2py.lib.dotdict import DotDict
from pipe2py.twisted import utils as tu

OPTS = {'ftype': 'none'}
logger = Logger(__name__).logger


def get_string(content, start, end):
    # TODO: convert relative links to absolute
    # TODO: remove the closing tag if using an HTML tag stripped of HTML tags
    # TODO: clean html with Tidy
    content = content.decode('utf-8')
    start_location = content.find(start) if start else 0
    right = content[start_location + len(start):]
    end_location = right[1:].find(end) + 1 if end else len(right)
    return right[:end_location] if end_location > 0 else right


@inlineCallbacks
def asyncParser(_, objconf, skip, **kwargs):
    """ Asynchronously parses the pipe content

    Args:
        _ (None): Ignored
        objconf (obj): The pipe configuration (an Objectify instance)
        skip (bool): Don't parse the content
        kwargs (dict): Keyword argurments

    Kwargs:
        assign (str): Attribute to assign parsed content (default: content)
        feed (dict): The original item

    Returns:
        Tuple(Iter[dict], bool): Tuple of (feed, skip)

    Examples:
        >>> from twisted.internet.task import react
        >>> from pipe2py.lib.utils import Objectify
        >>>
        >>> def run(reactor):
        ...     callback = lambda x: print(x[0].next()['content'][:32])
        ...     conf = {'url': FILES[5], 'start': '<title>', 'end': '</title>'}
        ...     objconf = Objectify(conf)
        ...     kwargs = {'feed': {}, 'assign': 'content'}
        ...     d = asyncParser(None, objconf, False, **kwargs)
        ...     return d.addCallbacks(callback, logger.error)
        >>>
        >>> try:
        ...     react(run, _reactor=tu.FakeReactor())
        ... except SystemExit:
        ...     pass
        ...
        CNN.com International - Breaking
    """
    if skip:
        feed = kwargs['feed']
    else:
        url = utils.get_abspath(objconf.url)
        content = yield tu.urlRead(url)
        parsed = get_string(content, objconf.start, objconf.end)
        splits = parsed.split(objconf.token) if objconf.token else [parsed]
        feed = ({kwargs['assign']: chunk} for chunk in splits)

    result = (feed, skip)
    returnValue(result)


def parser(_, objconf, skip, **kwargs):
    """ Parses the pipe content

    Args:
        _ (None): Ignored
        objconf (obj): The pipe configuration (an Objectify instance)
        skip (bool): Don't parse the content

    Returns:
        Tuple(Iter[dict], bool): Tuple of (feed, skip)

    Examples:
        >>> from pipe2py.lib.utils import Objectify
        >>> conf = {'url': FILES[5], 'start': '<title>', 'end': '</title>'}
        >>> objconf = Objectify(conf)
        >>> kwargs = {'feed': {}, 'assign': 'content'}
        >>> result, skip = parser(None, objconf, False, **kwargs)
        >>> result.next()['content'][:32]
        u'CNN.com International - Breaking'
    """
    if skip:
        feed = kwargs['feed']
    else:
        url = utils.get_abspath(objconf.url)
        content = urlopen(url).read()
        parsed = get_string(content, objconf.start, objconf.end)
        splits = parsed.split(objconf.token) if objconf.token else [parsed]
        feed = ({kwargs['assign']: chunk} for chunk in splits)

    return feed, skip


@processor(async=True, **OPTS)
def asyncPipe(*args, **kwargs):
    """A source that asynchronously fetches the content of a given web site as
    a string.

    Args:
        item (dict): The entry to process
        kwargs (dict): The keyword arguments passed to the wrapper

    Kwargs:
        context (obj): pipe2py.Context object
        conf (dict): The pipe configuration. Must contain the key 'url'. May
            contain the keys 'start', 'end', 'token', or 'assign'.

            url (str): The web site to fetch
            start (str): The starting string to fetch (exclusive, default: None).
            end (str): The ending string to fetch (exclusive, default: None).
            token (str): The tokenizer delimiter string (default: None).
            assign (str): Attribute to assign parsed content (default: content)

        field (str): Item attribute from which to obtain the string to be
            tokenized (default: content)

    Returns:
        dict: twisted.internet.defer.Deferred item with feeds

    Examples:
        >>> from twisted.internet.task import react
        >>>
        >>> def run(reactor):
        ...     callback = lambda x: print(x.next())
        ...     path = 'value.items'
        ...     conf = {'url': FILES[4], 'start': 'DOCTYPE ', 'end': 'http'}
        ...     d = asyncPipe(conf=conf)
        ...     return d.addCallbacks(callback, logger.error)
        >>>
        >>> try:
        ...     react(run, _reactor=tu.FakeReactor())
        ... except SystemExit:
        ...     pass
        ...
        {u'content': u'html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" "'}
    """
    return asyncParser(*args, **kwargs)


@processor(**OPTS)
def pipe(*args, **kwargs):
    """A source that fetches the content of a given web site as a string.

    Args:
        item (dict): The entry to process
        kwargs (dict): The keyword arguments passed to the wrapper

    Kwargs:
        context (obj): pipe2py.Context object
        conf (dict): The pipe configuration. Must contain the key 'url'. May
            contain the keys 'start', 'end', 'token', or 'assign'.

            url (str): The web site to fetch
            start (str): The starting string to fetch (exclusive, default: None).
            end (str): The ending string to fetch (exclusive, default: None).
            token (str): The tokenizer delimiter string (default: None).
            assign (str): Attribute to assign parsed content (default: content)

        field (str): Item attribute from which to obtain the string to be
            tokenized (default: content)

    Yield:
        dict: an item on the feed

    Examples:
        >>> conf = {'url': FILES[4], 'start': 'DOCTYPE ', 'end': 'http'}
        >>> pipe(conf=conf).next()
        {u'content': u'html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" "'}
    """
    return parser(*args, **kwargs)
