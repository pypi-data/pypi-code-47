from typing import Callable, Tuple, List

from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.document_compare_ways import DocumentCompareWays


class CorpusDiff:
    def __init__(self, left: Corpus, right: Corpus):
        self.left_corpus = left
        self.right_corpus = right

    def compare(self):
        # check
        if self.left_corpus.get_all_doc_ids() != self.right_corpus.get_all_doc_ids():
            raise ValueError("left and right corpus are not equal")

        doc_id_list = self.left_corpus.get_all_doc_ids()
        diff_pair_list = []
        for doc_id in doc_id_list:
            left_doc = self.left_corpus.get_doc_by_id(doc_id)
            right_doc = self.right_corpus.get_doc_by_id(doc_id)

            if left_doc == right_doc:
                continue

            diff_pair = DocumentDiffResult(left_doc, right_doc)
            diff_pair_list.append(diff_pair)

        return CorpusDiffResult(diff_pair_list)

    def set_document_compare_way(self, compare_way: DocumentCompareWays):
        self.left_corpus.set_document_compare_way(compare_way)
        self.right_corpus.set_document_compare_way(compare_way)

    def set_document_compare_method(
        self, compare_method: Callable[["Sequence", "Sequence"], bool]
    ):
        self.left_corpus.set_document_compare_method(compare_method)
        self.right_corpus.set_document_compare_method(compare_method)

    def set_document_hash_method(self, hash_method: Callable[["Sequence"], int]):
        self.left_corpus.set_document_compare_method(hash_method)
        self.right_corpus.set_document_compare_method(hash_method)


class DocumentDiffResult:
    def __init__(self, left: Document, right: Document):
        assert left.id == right.id

        self.left = left
        self.right = right

        self.id = left.id


class CorpusDiffResult(List[DocumentDiffResult]):
    def render_to_md(self) -> str:
        doc_pair_segment_list = []
        for doc_diff_result in self:
            doc_pair_segment = "# {}\n- {}\n- {}".format(
                doc_diff_result.id, doc_diff_result.left, doc_diff_result.right
            )
            doc_pair_segment_list.append(doc_pair_segment)

        return "\n\n".join(doc_pair_segment_list)
