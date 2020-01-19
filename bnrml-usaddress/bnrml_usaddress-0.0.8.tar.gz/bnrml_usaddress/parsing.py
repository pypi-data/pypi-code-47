#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/1/19
"""
This module contains parsing utilities for US addresses.

.. currentmodule:: brnl_usaddress.parsing
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
from functools import lru_cache
from typing import Dict, List, Mapping, NamedTuple, Set
from bnrml import Normalizer, Normalization
import usaddress
from .normalizers import by_component
from .normalizers.numbers import Extras
from .version import __version__, __release__

MAX_PARSE_CACHE: int = 1024  #: the maximum number of parse results to cache


class UsAddressComponents:
    """
    ``usaddress` components to which this module refers.
    """
    address_number = "AddressNumber"
    address_number_suffix = "AddressNumberSuffix"

    address_number_components = {
        address_number,
        address_number_suffix
    }  #: address number components


class AddressComponent(NamedTuple):
    """Describes a parsed address component."""
    key: str  #: the address component key
    value: str  #: the value

    def collapse(self, other: 'AddressComponent') -> 'AddressComponent':
        """
        Append the value of another address component.

        :param other: the other address component
        :return: a new address component with the concatenated value
        :raises ValueError: if the other address component's key does not
            match this address component's key
        """
        if not self.key == other.key:
            raise ValueError(
                f"Key mismatch: '{other.key}' != '{self.key}'"
            )
        return AddressComponent(
            key=self.key,
            value=f"{self.value} {other.value}".strip()
        )

    def export(self) -> Mapping[str, str]:
        """
        Export this object as a mapping of simple types.

        :return: the mapping
        """
        return self._asdict()  # pylint: disable=no-member


def _insert_addrnum_suffix(
        address_components: List[AddressComponent],
        suffix: str
) -> None:
    # Sanity Check:  If there's no suffix, there's nothing to do.
    if not suffix:
        return
    # Create a new address component.
    addrnum_sfx_ac = AddressComponent(
        key="AddressNumberSuffix",
        value=suffix
    )
    # Sanity Check:  If the list is empty...
    if not address_components:
        # ...just put the suffix in it.
        address_components.append(addrnum_sfx_ac)
        return
    # Go through the list backward...
    for idx, ac in reversed(list(enumerate(address_components))):
        # We'll insert behind the first `usaddress` "AddressNumber" or
        # "AddressNumberSuffix" component we find.
        if ac.key in UsAddressComponents.address_number_components:
            try:
                address_components.insert(idx+1, addrnum_sfx_ac)
            except KeyError:
                address_components.append(addrnum_sfx_ac)


class UsAddressParser:
    """
    Parse US addresses.
    """
    def __init__(
            self,
            normalizers: Mapping[str, Normalizer] = None,
            auto_normalizers: bool = True
    ):
        """

        :param normalizers: the preferred normalizers
        :param auto_normalizers: `True` to load normalizers from configuration
            automatically
        """
        self._normalizers = (
            dict(normalizers) if normalizers else {}
        )
        self._auto_normalizers: bool = auto_normalizers

    @classmethod
    def _collapse(
            cls,
            components: List[AddressComponent],
            keys: Set[str]
    ) -> List[AddressComponent]:
        """
        Collapse contiguous address components with the same key into a
        single address component within an ordered list.

        :param components: the components
        :keys: the ``usaddress`` component keys to collapse
        """
        # Make a copy of the input list.
        collapsed = [ac for ac in components]
        # We're not going to enumerate the address components in *reverse*
        # order so that we can append any component that should be collapsed
        # with the one that comes before it (in cases where they share the
        # same key).
        for idx, ac in reversed(list(enumerate(collapsed))):
            # We don't need to check the first item.
            if idx == 0:
                break
            up = idx-1  # The next (i.e. *previous* item index).
            # If this is one of the keys we're collapsing, and the key
            # next (i.e. *previous*) item has the same key...
            if ac.key in keys and ac.key == collapsed[up].key:
                # ...collapse this item into the previous one...
                collapsed[up] = collapsed[up].collapse(ac)
                # ...and remove this one.  See?  We're "rolling 'em up".
                collapsed[idx] = None
        # Return a new list, eliminating the items
        return [ac for ac in collapsed if ac is not None]

    @lru_cache(maxsize=MAX_PARSE_CACHE)
    def parse(self, address: str, debug: bool = False) -> Mapping[str, Dict]:
        """
        Parse a US address string.

        :param address: the address string
        :param debug: includes debugging information
        :return: the parsed address
        """

        # Let's start by letting `usaddress` do it's thing.  We'll put the
        # result into a case-insensitive dictionary.
        usaddress_parsed = usaddress.parse(address)

        # Reconfigure the `usaddress` parse result.  This is the object
        # we'll modify from here on in.
        normalized = [
            AddressComponent(key=key, value=value)
            for value, key
            in usaddress_parsed
        ]

        # Collapse key-value pairs that `usaddress` might have broken out,
        # but which, for the sake of normalization, we need to see as a
        # single value.
        normalized = self._collapse(
            components=normalized,
            keys={
                "StreetNamePreDirectional",
                "StreetNamePostDirectional",
                "StreetName"
            }
        )

        # Create a list to hold the normalizations.
        debug_nzns = []
        # Create a dictionary to hold debugging information.
        debug_info = {
            'address': address,
            'usaddress': {
                'parse': usaddress_parsed
            },
            'bnrml-usaddress': {
                'info': {
                    'version': __version__,
                    'release': __release__
                },
                'normalizations': debug_nzns
            }
        }

        # If the address number is normalized, hang on to it for
        # post-processing.
        addrnum_normal: Normalization = None

        # Let's look at each item `usaddress` parsed for us.
        for idx, (key, value) in enumerate(normalized):
            try:
                normalizer = self._normalizers[key]
            except KeyError:
                # If we're not supposed to try to update the collection of
                # normalizers automatically...
                if not self._auto_normalizers:
                    # ...just move along.
                    continue
                # Let's see if we can get a configured normalizer for this
                # component.
                normalizer = by_component(key.lower())
                # In any case, save this result for next time.
                self._normalizers[key] = normalizer
                # If we have a normalizer for this component...
            if normalizer:
                # ...attempt the normalization.
                normalization = normalizer.normalize(value)
                # If we got a normalization...
                if normalization is not None:
                    # ...update the dictionary with the normalized value.
                    normalized[idx] = AddressComponent(
                        key=key,
                        value=normalization.normalized
                    )
                    # Add the result to the debugging information.
                    if debug:
                        debug_nzns.append(
                            (key, normalization.export())
                        )
                # If this is the `AddressNumber` component, hang on to it.
                if key == 'AddressNumber':
                    addrnum_normal = normalization

        # Do some post-processing with the address number normalization
        # (if there is one).
        if addrnum_normal:
            suffix = addrnum_normal.extras.get(Extras.suffix)
            if suffix:
                _insert_addrnum_suffix(normalized, suffix)

        # Prepare the result.
        result = {
            'result': [
                ({
                    k: v.upper() if k == 'value' else v
                    for k, v in ac.export().items()
                })
                for ac in normalized
            ]
        }

        # If the caller wants debugging information...
        if debug:
            # ...add it now.
            result['debug'] = debug_info

        # There we go.
        return result
