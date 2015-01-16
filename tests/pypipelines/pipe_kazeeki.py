# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab
# Pipe pipe_82cdc3ce2af818cea73009f17cef4cd5 generated by pipe2py

from os import path as p
from pprint import pprint
from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.internet.task import react
from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.lib.utils import combine_dicts as cdict
from pipe2py.lib.collections import SyncPipe
from pipe2py.twisted.collections import AsyncPipe

PARENT = p.dirname(p.dirname(p.dirname(__file__)))

forever = pipe_forever()
make_regex = lambda f, m, r: {'field': f, 'match': m, 'replace': r}


def make_simplemath(other, op):
    return {'OTHER': {'subkey': other, 'type': 'number'}, 'OP': op}


def make_substring(_from, length):
    return {
        'from': {'type': 'integer', 'value': _from}
        , 'length': {'type': 'integer', 'value': length}
    }


def make_exchangerate(quote, offline=True):
    return {
        'quote': quote
        , 'default': DEF_CUR_CODE
        , 'offline': {'type': 'bool', 'value': offline}
    }


def make_tokenizer(to_str, dedupe=False, sort=False):
    return {
        'to-str': to_str
        , 'dedupe': {'type': 'bool', 'value': dedupe}
        , 'sort': {'type': 'bool', 'value': sort}
    }


def make_loop(_with, assign_to, embed_conf, **kwargs):
    return {
        'assign_part': kwargs.get('part', 'all'),
        'emit_part': kwargs.get('part', 'all'),
        'mode': kwargs.get('mode', 'assign'),
        'with': _with,
        'assign_to': assign_to,
        'embed': {'conf': embed_conf},
        'pass_if': kwargs.get('pass_if')
    }

DEF_CUR_CODE = 'USD'
mmatch = {'multilinematch': '4'}
smatch = {'singlelinematch': '2'}
gmatch = {'globalmatch': '1'}

rename1_rule = [
    {'newval': '', 'field': 'y:title', 'op': 'rename'},
    {'newval': '', 'field': 'content', 'op': 'rename'},
    {'newval': 'k:posted', 'field': 'y:published', 'op': 'rename'},
    {'newval': 'k:job_type', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:content', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:work_location', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:client_location', 'field': 'description', 'op': 'copy'},
    # {'newval': 'k:category', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:tags', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:due', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:submissions', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:budget_raw', 'field': 'description', 'op': 'copy'},
    {'newval': 'k:marketplace', 'field': 'link', 'op': 'copy'},
    {'newval': 'k:author', 'field': 'title', 'op': 'copy'}]

rename2_rule = [
    {'newval': 'k:budget_raw1', 'field': 'k:budget_raw', 'op': 'copy'},
    {'newval': 'k:budget_raw2', 'field': 'k:budget_raw', 'op': 'copy'}]

rename3_rule = [
    {'newval': 'k:budget_raw1_num', 'field': 'k:budget_raw1', 'op': 'copy'},
    {'newval': 'k:budget_raw1_sym', 'field': 'k:budget_raw1', 'op': 'copy'},
    {'newval': 'k:budget_raw1_code', 'field': 'k:budget_raw1', 'op': 'copy'},
    {'newval': 'k:budget_raw2_num', 'field': 'k:budget_raw2', 'op': 'copy'},
    {'newval': 'k:budget_raw2_sym', 'field': 'k:budget_raw2', 'op': 'copy'},
    {'newval': 'k:budget_raw2_code', 'field': 'k:budget_raw2', 'op': 'copy'}]

rename4_rule = [
    {'newval': 'k:budget_full', 'field': 'k:budget_w_sym', 'op': 'copy'}]

match1_01 = '(.*)( - oDesk|\\| Elance Job)'
match1_02 = '^(http[s]?:\\/\\/)?\\/?([^\\/\\.]+\\.)*([^\\/\\.]+\\.[^:\\/\\s\\.]{2,3})(.*)'
match1_03 = '.*(Hourly budget:|Budget:<.*?> Hourly).*'
match1_04 = '.*(Fixed Price budget:|Budget:<.*?> Fixed Price).*'
match1_05 = '^(?!\\b(hourly|fixed)\\b).*'
match1_06 = '(.*)(<b>)?(Category|Budget):?(<.*?>)?(.*)'
match1_07 = '(.*)(<b>Description:<.*?>)(.*?)(<.*?>)(.*)'
match1_08 = '(.*)(<b>Proposals:<.*?>)(.*?)(<a href)(.*)'
match1_09 = '(.*)(<b>)(.*)'
match1_10 = '(.*)(\\bby\\b)(.*)'
match1_11 = '(.*)(<b>)(.*)'
match1_12 = '(.*)(<b>(Freelancer|Preferred Job) Location:<.*?>)(.*?)(<.*?>)(.*)'
match1_13 = '(.*)(<b>)(.*)'
match1_14 = '(.*)(<b>(Client Location:<.*?>|Country<.*?>:))(.*?)(<.*?>)(.*)'
match1_14b = '(.*)(<b>)(.*)'
match1_15 = '(.*)(<b>(Category:?<.*?>:?))(.*?)(<.*?>|<b>Skills<.*?>)(.*)'
match1_16 = '(.*)(<b>(Required skills|Desired Skills):<.*?>)(.*?)(<.*?>)(.*)'
match1_17 = '(.*)(Jobs:)(.*?)(\\))(.*)'
match1_18 = '&gt;|<br>'
match1_19 = '(\\w+)(?!.*,)'
match1_20 = '\\/'
match1_21 = '[^a-zA-Z\\d,]+'
match1_22 = '.*Time Left.*\\\(Ends(.*)\\\) <.*?>'
match1_23 = '(.*)(<b>)(.*)'
match1_24 = '(.*)(Fixed Price budget:<.*?>|Hourly budget.*Rate:|Budget:|Type and Budget|Budget<.*?>:)(.*?)(<.*?>|, Jobs:)(.*)'
match1_25 = 'Under|Upto|Less than|or less'
match1_26 = '^(?!.*-.*)(.*)'

regex1_rule = [
    cdict(mmatch, smatch, make_regex('title', match1_01, '$1')),
    make_regex('k:marketplace', match1_02, '$3'),
    cdict(mmatch, smatch, make_regex('k:job_type', match1_03, 'hourly')),
    cdict(mmatch, smatch, make_regex('k:job_type', match1_04, 'fixed')),
    cdict(mmatch, smatch, make_regex('k:job_type', match1_05, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:content', match1_06, '$1')),
    cdict(mmatch, smatch, make_regex('k:content', match1_07, '$3')),
    cdict(mmatch, smatch, make_regex('k:submissions', match1_08, '$3')),
    cdict(mmatch, smatch, make_regex('k:submissions', match1_09, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:author', match1_10, '$3')),
    cdict(mmatch, smatch, make_regex('k:author', match1_11, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:work_location', match1_12, '$4')),
    cdict(mmatch, smatch, make_regex('k:work_location', match1_13, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:client_location', match1_14, '$4')),
    cdict(mmatch, smatch, make_regex('k:client_location', match1_14b, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:tags', match1_15, '$4')),
    cdict(mmatch, smatch, make_regex('k:tags', match1_16, '$4')),
    cdict(mmatch, smatch, make_regex('k:tags', match1_17, '$3')),
    cdict(gmatch, make_regex('k:tags', match1_18, '')),
    cdict(gmatch, make_regex('k:tags', match1_19, '$1,')),
    cdict(gmatch, make_regex('k:tags', match1_20, ',')),
    cdict(gmatch, make_regex('k:tags', match1_21, '-')),
    cdict(gmatch, make_regex('k:tags', '^-|-$', '')),
    cdict(gmatch, make_regex('k:tags', ',-|-,', ',')),
    cdict(gmatch, make_regex('k:tags', '^,|,$', '')),
    cdict(mmatch, smatch, make_regex('k:due', match1_22, '$1')),
    cdict(mmatch, smatch, make_regex('k:due', match1_23, 'unknown')),
    cdict(mmatch, smatch, make_regex('k:budget_raw', match1_24, '$3')),
    make_regex('k:budget_raw', 'k', '000'),
    make_regex('k:budget_raw', match1_25, '-'),
    make_regex('k:budget_raw', match1_26, '$1-$1'),
]

regex2_rule = [
    make_regex('k:budget_raw1', '(.*)-(.*)', '$1')
    , make_regex('k:budget_raw2', '(.*)-(.*)', '$2')
]

regex3_rule = [
    make_regex('k:budget_raw1_num', '[^\\d]*(\\d+\\.?\\d*).*', '$1')
    , make_regex('k:budget_raw1_sym', '\\s*([$£€₹]).*', '$1')
    , make_regex('k:budget_raw1_code', '.*(\\b[A-Z]{3}\\b).*', '$1')
    , make_regex('k:budget_raw2_num', '[^\\d]*(\\d+\\.?\\d*).*', '$1')
    , make_regex('k:budget_raw2_sym', '\\s*([$£€₹]).*', '$1')
    , make_regex('k:budget_raw2_code', '.*(\\b[A-Z]{3}\\b).*', '$1')
]

regex4_rule = [make_regex('k:cur_code', '^(?![A-Z]{3}\\b)(.*)', DEF_CUR_CODE)]

strregex1_conf = {
    'RULE': [
        make_regex(None, '.*hr.*', 'hourly')
        , make_regex(None, '.*unknown.*', 'unknown')
        , make_regex(None, '^(?!.*(hourly|unknown).*).*', 'fixed')
    ]
}

strregex2_conf = {
    'RULE': [make_regex(None, '^unknown$', {'subkey': 'loop:strregex'})]}

strregex3_conf = {
    'RULE': [
        {'param': '1', 'find': '$', 'replace': 'USD'}
        , {'param': '1', 'find': u'£', 'replace': 'GBP'}
        , {'param': '1', 'find': u'€', 'replace': 'EUR'}
        , {'param': '1', 'find': u'₹', 'replace': 'INR'}
    ]
}

strregex4_conf = {
    'RULE': [
        {'match': 'fixed', 'replace': '1'}
        , {'match': 'hourly', 'replace': '2'}
        , {'match': 'unknown', 'replace': '3'}
    ]
}

strconcat1_conf = {
    'part': [
        {'subkey': 'k:budget_raw1_code'}
        , {'subkey': 'k:budget_raw2_code'}
    ]
}

strconcat2_conf = {
    'part': [
        {'subkey': 'k:budget_raw1_sym'}
        , {'subkey': 'k:budget_raw2_sym'}
    ]
}

strconcat3_conf = {
    'part': [
        {'subkey': 'k:budget_w_sym'}
        , {'value': ' ('}
        , {'subkey': 'k:budget_converted_w_sym'}
        , {'value': ')'}
    ]
}

strconcat4_conf = {
    'part': [{'subkey': 'k:budget_full'}, {'value': ' / hr'}]}

tokenizer_conf = make_tokenizer(',', True, True)
substring1_conf = make_substring('0', '3')
substring2_conf = make_substring('0', '1')
currencyformat1_conf = {'currency': {'subkey': 'k:cur_code'}}
exchangerate_conf = make_exchangerate(DEF_CUR_CODE, True)
currencyformat2_conf = {'currency': DEF_CUR_CODE}
simplemath1_conf = make_simplemath('k:budget_raw2_num', 'mean')
simplemath2_conf = make_simplemath('k:rate', 'multiply')
test1 = lambda item: item.get('k:cur_code')
test2 = lambda item: item.get('k:cur_code') != DEF_CUR_CODE
test3 = lambda item: item.get('k:cur_code') == DEF_CUR_CODE
test4 = lambda item: item.get('k:job_type') != 'hourly'

my_item = {
    'content': '<p>Hello, I need to fix an application i am working on.\xa0\xa0Currently the rss has a cross origin problem, and i need to fix this.<br>\n<br>\nNext thing is i need to configure that the news will be read as an ion-list element, and a single article will be in a new page. with transition.<br>\n<br>\nThe application is in ionic + angular, so only experienced developers are welcome to this project.<br><br><b>Budget</b>: 10 EUR<br><b>Posted On</b>: December 27, 2014 13:32 UTC<br><b>ID</b>: 204946132<br><b>Category</b>: Web Development &gt; Web Programming<br><b>Skills</b>: Array<br><b>Country</b>: Israel<br><a href="https://www.odesk.com/jobs/Need-fix-Ionic-Rss-Reader-Application_%7E01d9a84fc5a0a79ddb?source=rss">click to apply</a></p>',
    'link': 'https://www.odesk.com/jobs/Need-fix-Ionic-Rss-Reader-Application_%7E01d9a84fc5a0a79ddb?source=rss',
    'pubDate': 'December 27, 2014',
    'summary': '<p>Hello, I need to fix an application i am working on.\xa0\xa0Currently the rss has a cross origin problem, and i need to fix this.<br>\n<br>\nNext thing is i need to configure that the news will be read as an ion-list element, and a single article will be in a new page. with transition.<br>\n<br>\nThe application is in ionic + angular, so only experienced developers are welcome to this project.<br><br><b>Budget</b>: 10 EUR<br><b>Posted On</b>: December 27, 2014 13:32 UTC<br><b>ID</b>: 204946132<br><b>Category</b>: Web Development &gt; Web Programming<br><b>Skills</b>: Array<br><b>Country</b>: Israel<br><a href="https://www.odesk.com/jobs/Need-fix-Ionic-Rss-Reader-Application_%7E01d9a84fc5a0a79ddb?source=rss">click to apply</a></p>',
    'title': 'Need to fix Ionic Rss Reader Application - oDesk',
    'updated': 'Sat, 27 Dec 2014 13:32:55 +0000',
    'y:id': None,
    'y:published': None,
    'y:title': 'Need to fix Ionic Rss Reader Application - oDesk'
}

loop1_conf = make_loop('k:budget_raw', 'loop:strregex', strregex1_conf)
loop2_conf = make_loop('k:job_type', 'k:job_type', strregex2_conf)
loop3_conf = make_loop('k:tags', 'k:tags', tokenizer_conf)
loop4_conf = make_loop('k:budget_raw1_num', 'k:budget', simplemath1_conf)
loop5_conf = make_loop('', 'k:cur_code', strconcat1_conf)
loop6_conf = make_loop('k:cur_code', 'k:cur_code', substring1_conf)
loop7_conf = make_loop('', 'k:budget_sym', strconcat2_conf)
loop8_conf = make_loop('k:budget_sym', 'k:budget_sym', substring2_conf)
loop9_conf = make_loop(
    'k:budget_sym', 'k:cur_code', strregex3_conf, pass_if=test1)
loop10_conf = make_loop('k:job_type', 'k:job_type_code', strregex4_conf)
loop11_conf = make_loop('link', 'id', {'embed': {}})
loop12_conf = make_loop('k:budget', 'k:budget_w_sym', currencyformat1_conf)
loop13_conf = make_loop('k:cur_code', 'k:rate', exchangerate_conf)
loop14_conf = make_loop('k:budget', 'k:budget_converted', simplemath2_conf)
loop15_conf = make_loop(
    'k:budget_converted', 'k:budget_converted_w_sym', currencyformat2_conf)
loop16_conf = make_loop('', 'k:budget_full', strconcat3_conf, pass_if=test3)
loop17_conf = make_loop('', 'k:budget_full', strconcat4_conf, pass_if=test4)

itembuilder_attrs = [{'key': k, 'value': v} for k, v in my_item.items()]

def make_conf(source):
    return {'value': source.values()[0], 'type': source.keys()[0]}

sources = [
    {'url': 'http://feeds.feedburner.com/guru/all'}
    , {'url': 'http://feeds.feedburner.com/odesk/rss'}
    , {'url': 'http://feeds.feedburner.com/elance/all'}
    , {'url': 'http://feeds.feedburner.com/freelancer/all'}
    , {'url': 'http://feeds.feedburner.com/guru/it'}
    , {'url': 'http://feeds.feedburner.com/guru/design'}
    , {'url': 'http://feeds.feedburner.com/elance/it'}
    , {'url': 'http://feeds.feedburner.com/elance/design'}
]

abspath = p.abspath(p.join(PARENT, 'pipe2py', 'data', 'kazeeki.json'))
url = "file://%s" % abspath
fetchdata_conf = {'URL': {'value': url}, 'path': {'value': 'items'}}

fetch_conf = {'URL': map(make_conf, sources)}
itembuilder_conf = {'attrs': itembuilder_attrs}

def parse_source(source):
    pipe = (
        source
            .pipe('rename', conf={'RULE': rename1_rule})
            .pipe('regex', conf={'RULE': regex1_rule})
            .pipe('rename', conf={'RULE': rename2_rule})
            .pipe('regex', conf={'RULE': regex2_rule})
            .pipe('rename', conf={'RULE': rename3_rule})
            .pipe('regex', conf={'RULE': regex3_rule})
            .loop('strregex', conf=loop1_conf)
            .loop('strregex', conf=loop2_conf)
            .loop('stringtokenizer', conf=loop3_conf)
            .loop('simplemath', conf=loop4_conf)
            .loop('strconcat', conf=loop5_conf)
            .loop('substr', conf=loop6_conf)
            .loop('strconcat', conf=loop7_conf)
            .loop('substr', conf=loop8_conf)
            .loop('strreplace', conf=loop9_conf)
            .pipe('regex', conf={'RULE': regex4_rule})
            .loop('strregex', conf=loop10_conf)
            .loop('hash', conf=loop11_conf)
            .loop('currencyformat', conf=loop12_conf)
            .loop('exchangerate', conf=loop13_conf)
            .loop('simplemath', conf=loop14_conf)
            .loop('currencyformat', conf=loop15_conf)
            .pipe('rename', pass_if=test2, conf={'RULE': rename4_rule})
            .loop('strconcat', conf=loop16_conf)
            .loop('strconcat', conf=loop17_conf)
    )

    return pipe.output


def print_content(output):
    pipe = list(output)
    pprint(pipe[0])
    print 'count:', len(pipe)


def pipe_kazeeki(context=None, conf=itembuilder_conf, **kwargs):
    # source = SyncPipe('fetch', conf=fetch_conf, context=context)
    # source = SyncPipe('itembuilder', conf=conf, context=context)
    source = SyncPipe('fetchdata', conf=fetchdata_conf, context=context)
    output = parse_source(source)
    return output


def asyncPipeKazeeki(reactor, context=None, conf=itembuilder_conf, **kwargs):
    # source = AsyncPipe('fetch', conf=fetch_conf, context=context)
    # source = AsyncPipe('itembuilder', conf=conf, context=context)
    source = AsyncPipe('fetchdata', conf=fetchdata_conf, context=context)
    output = parse_source(source)
    output.addCallback(print_content)
    return output

if __name__ == "__main__":
    # output = pipe_kazeeki(Context())
    # print_content(output)
    react(asyncPipeKazeeki, [Context()])
