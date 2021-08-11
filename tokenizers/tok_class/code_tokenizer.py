#!/usr/bin/env python3
# Author : Saikat Chakraborty (saikatc@cs.columbia.edu)
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Basic tokenizer that splits text into alpha-numeric tokens and
non-whitespace tokens.
"""

import logging
import re

logger = logging.getLogger(__name__)

# !/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Base tokenizer/tokens classes and utilities."""

import copy


class Tokens(object):
    """A class to represent a list of tokenized text."""
    TEXT = 0
    TEXT_WS = 1
    SPAN = 2
    POS = 3
    LEMMA = 4
    NER = 5

    def __init__(self, data, annotators, opts=None):
        self.data = data
        self.annotators = annotators
        self.opts = opts or {}

    def __len__(self):
        """The number of tokens."""
        return len(self.data)

    def slice(self, i=None, j=None):
        """Return a view of the list of tokens from [i, j)."""
        new_tokens = copy.copy(self)
        new_tokens.data = self.data[i: j]
        return new_tokens

    def untokenize(self):
        """Returns the original text (with whitespace reinserted)."""
        return ''.join([t[self.TEXT_WS] for t in self.data]).strip()

    def words(self, uncased=False):
        """Returns a list of the text of each token
        Args:
            uncased: lower cases text
        """
        if uncased:
            return [t[self.TEXT].lower() for t in self.data]
        else:
            return [t[self.TEXT] for t in self.data]

    def offsets(self):
        """Returns a list of [start, end) character offsets of each token."""
        return [t[self.SPAN] for t in self.data]

    def pos(self):
        """Returns a list of part-of-speech tags of each token.
        Returns None if this annotation was not included.
        """
        if 'pos' not in self.annotators:
            return None
        return [t[self.POS] for t in self.data]

    def lemmas(self):
        """Returns a list of the lemmatized text of each token.
        Returns None if this annotation was not included.
        """
        if 'lemma' not in self.annotators:
            return None
        return [t[self.LEMMA] for t in self.data]

    def entities(self):
        """Returns a list of named-entity-recognition tags of each token.
        Returns None if this annotation was not included.
        """
        if 'ner' not in self.annotators:
            return None
        return [t[self.NER] for t in self.data]

    def ngrams(self, n=1, uncased=False, filter_fn=None, as_strings=True):
        """Returns a list of all ngrams from length 1 to n.
        Args:
            n: upper limit of ngram length
            uncased: lower cases text
            filter_fn: user function that takes in an ngram list and returns
              True or False to keep or not keep the ngram
            as_string: return the ngram as a string vs list
        """

        def _skip(gram):
            if not filter_fn:
                return False
            return filter_fn(gram)

        words = self.words(uncased)
        ngrams = [(s, e + 1)
                  for s in range(len(words))
                  for e in range(s, min(s + n, len(words)))
                  if not _skip(words[s:e + 1])]

        # Concatenate into strings
        if as_strings:
            ngrams = ['{}'.format(' '.join(words[s:e])) for (s, e) in ngrams]

        return ngrams

    def entity_groups(self):
        """Group consecutive entity tokens with the same NER tag."""
        entities = self.entities()
        if not entities:
            return None
        non_ent = self.opts.get('non_ent', 'O')
        groups = []
        idx = 0
        while idx < len(entities):
            ner_tag = entities[idx]
            # Check for entity tag
            if ner_tag != non_ent:
                # Chomp the sequence
                start = idx
                while idx < len(entities) and entities[idx] == ner_tag:
                    idx += 1
                groups.append((self.slice(start, idx).untokenize(), ner_tag))
            else:
                idx += 1
        return groups


class Tokenizer(object):
    """Base tokenizer class.
    Tokenizers implement tokenize, which should return a Tokens class.
    """

    def tokenize(self, text):
        raise NotImplementedError

    def shutdown(self):
        pass

    def __del__(self):
        self.shutdown()


def tokenize_with_camel_case(token):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', token)
    return [m.group(0) for m in matches]


def tokenize_with_snake_case(token):
    return token.split('_')


class CodeTokenizer(Tokenizer):
    def __init__(self, camel_case=True, snake_case=True, **kwargs):
        """
        Args:
            camel_case: Boolean denoting whether CamelCase split is desired
            snake_case: Boolean denoting whether snake_case split is desired
            annotators: None or empty set (only tokenizes).
        """
        super(CodeTokenizer, self).__init__()
        self.snake_case = snake_case
        self.camel_case = camel_case
        assert self.snake_case or self.camel_case, \
            'To call CodeIdentifierTokenizer at least one of camel_case or ' \
            'snake_case flag has to be turned on in the initializer'
        if len(kwargs.get('annotators', {})) > 0:
            logger.warning('%s only tokenizes! Skipping annotators: %s' %
                           (type(self).__name__, kwargs.get('annotators')))
        self.annotators = set()

    def tokenize(self, text):
        tokens = text.split()
        snake_case_tokenized = []
        if self.snake_case:
            for token in tokens:
                snake_case_tokenized.extend(tokenize_with_snake_case(token))
        else:
            snake_case_tokenized = tokens
        camel_case_tokenized = []
        if self.camel_case:
            for token in snake_case_tokenized:
                camel_case_tokenized.extend(tokenize_with_camel_case(token))
        else:
            camel_case_tokenized = snake_case_tokenized
        data = []
        for token in camel_case_tokenized:
            data.append((token, token, token))

        return Tokens(data, self.annotators)


if __name__ == '__main__':
    line_to_tok = "@dev CammelCase snake_snaky for eliminate-elimin {my friend;} \t @param"
    tokens = CodeTokenizer()
    token = tokens.tokenize(line_to_tok)
    print(token.words())
