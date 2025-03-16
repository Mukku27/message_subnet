import typing
import bittensor as bt


class Dummy(bt.Synapse):
    """
    A simple dummy protocol that inherits from bt.Synapse.
    This protocol handles message communication between
    the miner and the validator.

    Attributes:
    - message: A string value representing the message sent by the validator.
    - response: An optional string value representing the response from the miner.
    """

    # Required request input, filled by the dendrite caller.
    message: str

    # Optional request output, filled by the axon responder.
    response: typing.Optional[str] = None
