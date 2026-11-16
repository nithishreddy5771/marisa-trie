import marisa_trie
import pytest


@pytest.mark.parametrize('trie_type', [marisa_trie.Trie, marisa_trie.BinaryTrie])
@pytest.mark.parametrize('left,right', [
    ('\0a', '\0b'),
    ('a\0b', 'a\0c'),
    ('a\0\0', 'a\0c'),
    ('a\0', 'a\0'),
    ('a\0', 'a\0b'),
    ('', ''),
    ('abc', 'abd'),
])
def test_equality_compares_bytes_after_nul(trie_type, left, right):
    if trie_type is marisa_trie.BinaryTrie:
        left, right = left.encode(), right.encode()
    first = trie_type([left])
    second = trie_type([right])
    assert (first == second) is (left == right)
    assert (first != second) is (left != right)
