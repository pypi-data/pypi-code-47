from enum import Enum


def consider_text_only_document_compare_function(self, other):
    return self.text == other.text


def consider_text_only_document_hash_function(self):
    return hash(frozenset(self.text))


def consider_text_entity_compare_function(self, other):
    return self.text == other.text and self.span_set == other.span_set


def consider_text_entity_hash_function(self):
    return hash((frozenset(self.text), self.span_set))


class DocumentCompareWays(Enum):
    TEXT_ONLY = {
        "eq": consider_text_only_document_compare_function,
        "hash": consider_text_only_document_hash_function,
    }
    TEXT_ENTITY_ONLY = {
        "eq": consider_text_only_document_compare_function,
        "hash": consider_text_entity_hash_function,
    }
    TEXT_ENTITY_INTENT_ONLY = 3
    TEXT_ENTITY_INTENT_DOMAIN = 4
    ALL = 5
