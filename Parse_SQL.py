import sqlparse as sp
from collections import Iterable

text1 = """
select  a.col1, a.col2, a.col3
from    ONEdb.DBO.someTable a inner join SOMEdb.DBO.anotherTable b on a.jcol = b.jcol
where
    a.col1 =
        (
            SELECT max(col) from maxTABLE c
        )
"""

text2 = """
select  a.col1, a.col2, a.col3
from    (select * from thisTable) a inner join (select * from thatTable) b on a.jcol = b.jcol
where    a.col1 = ( SELECT max(col) from maxTABLE c)

UNION ALL

select col1 from someTable d

"""
text_lst = []
text_lst.append(text1)
text_lst.append(text2)


import itertools
import sqlparse

from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML


def is_subselect(parsed):
    if not parsed.is_group():
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if item.is_group():
            for x in extract_from_part(item):
                yield x
        if from_seen:
            if is_subselect(item):
                for x in extract_from_part(item):
                    yield x
            elif item.ttype is Keyword and item.value.upper() in ['ORDER', 'GROUP', 'BY', 'HAVING', 'UNION']:
                from_seen = False
                StopIteration
            else:
                yield item
        if item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                value = identifier.value.replace('"', '').lower()
                yield value
        elif isinstance(item, Identifier):
            value = item.value.replace('"', '').lower()
            yield value


def extract_tables(sql):
    # let's handle multiple statements in one sql string
    extracted_tables = []
    statements = list(sqlparse.parse(sql))
    for statement in statements:
        if statement.get_type() != 'UNKNOWN':
            stream = extract_from_part(statement)
            extracted_tables.append(set(list(extract_table_identifiers(stream))))
    return list(itertools.chain(*extracted_tables))


print text1, [item for item in extract_tables(text1) if not '(' in item]
print text2, [item for item in extract_tables(text2) if not '(' in item]
