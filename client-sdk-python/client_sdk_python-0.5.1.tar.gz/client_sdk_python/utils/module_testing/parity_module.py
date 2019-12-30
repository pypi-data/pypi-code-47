import pytest

from eth_utils import (
    add_0x_prefix,
)

from client_sdk_python.utils.formatters import (
    hex_to_integer,
)


class ParityModuleTest:

    def test_trace_replay_transaction(self, web3, parity_fixture_data):
        trace = web3.parity.traceReplayTransaction(parity_fixture_data['mined_txn_hash'])

        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        assert trace['trace'][0]['action']['from'] == add_0x_prefix(parity_fixture_data['coinbase'])

    def test_trace_replay_block_with_transactions(self,
                                                  web3,
                                                  block_with_txn,
                                                  parity_fixture_data):
        trace = web3.parity.traceReplayBlockTransactions(block_with_txn['number'])
        assert len(trace) > 0
        trace_0_action = trace[0]['trace'][0]['action']
        assert trace_0_action['from'] == add_0x_prefix(parity_fixture_data['coinbase'])

    def test_trace_replay_block_without_transactions(self, web3, empty_block):
        trace = web3.parity.traceReplayBlockTransactions(empty_block['number'])
        assert len(trace) == 0

    def test_trace_block(self, web3, block_with_txn):
        trace = web3.parity.traceBlock(block_with_txn['number'])
        assert trace[0]['blockNumber'] == block_with_txn['number']

    def test_trace_transaction(self, web3, parity_fixture_data):
        trace = web3.parity.traceTransaction(parity_fixture_data['mined_txn_hash'])
        assert trace[0]['action']['from'] == add_0x_prefix(parity_fixture_data['coinbase'])

    def test_trace_call(self, web3, math_contract, math_contract_address):
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(7, 11),
            transaction={'from': coinbase, 'to': math_contract_address},
        )
        trace = web3.parity.traceCall(txn_params)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        result = hex_to_integer(trace['output'])
        assert result == 18

    def test_eth_call_with_0_result(self, web3, math_contract, math_contract_address):
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(0, 0),
            transaction={'from': coinbase, 'to': math_contract_address},
        )
        trace = web3.parity.traceCall(txn_params)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        result = hex_to_integer(trace['output'])
        assert result == 0

    @pytest.mark.parametrize(
        'raw_transaction',
        [
            (
                # address 0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6
                '0xf8648085174876e8008252089439eeed73fb1d3855e90cbd42f348b3d7b340aaa601801ba0ec1295f00936acd0c2cb90ab2cdaacb8bf5e11b3d9957833595aca9ceedb7aada05dfc8937baec0e26029057abd3a1ef8c505dca2cdc07ffacb046d090d2bea06a'  # noqa: E501
            ),
        ]
    )
    def test_trace_raw_transaction(self,
                                   web3,
                                   raw_transaction,
                                   funded_account_for_raw_txn):
        trace = web3.parity.traceRawTransaction(raw_transaction)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        assert trace['trace'][0]['action']['from'] == funded_account_for_raw_txn.lower()

    def test_trace_filter(self, web3, txn_filter_params, parity_fixture_data):
        trace = web3.parity.traceFilter(txn_filter_params)
        assert isinstance(trace, list)
        assert trace[0]['action']['from'] == add_0x_prefix(parity_fixture_data['coinbase'])
