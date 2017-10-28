"""Docstring To Do."""
from typing import Dict, Callable
from inspect import getfullargspec


def default_callback(e: object) -> object:
    """
    Define default event callback function.

    Returns:
        e, the Event that triggered the callback function
    """
    return e


default_callbacks = {
    'message': default_callback,
    'postback': default_callback,
    'read': default_callback,
    'delivery': default_callback,
    'optin': default_callback,
}


class CallbackManager:
    """
    Class outsourcing the callback management.

    Use set_callback to set custom callbacks
    """

    def __init__(self, default_callbacks: Dict[str, Callable]) -> None:
        """Init method."""
        self.callbacks = default_callbacks

    def set_callback(self, callback: Callable, caller_type: str) -> None:
        """Set the callback method for the specified message type.

        Args:
            callback (Callable): callback method to call for the specified
            caller_type.
            caller_type (str): message type parameter.

        Returns:
            None if the arguments are correct, raises an error otherwise.

        """
        if not (0 < len(getfullargspec(callback).args) < 3):
            raise ValueError("Callback function must have one argument or two in case of "
                             "a class function of type Event")

        if caller_type in self.callbacks:
            if callable(callback):
                self.callbacks[caller_type] = callback
            else:
                raise TypeError("Callback argument must be callable")
        else:
            raise ValueError(
                "Event type {caller_type} does not exist, must one of :"
                " {available_types}"
                .format(
                    caller_type=caller_type,
                    available_types=list(self.callbacks.keys())
                    ))

    def get_callback(self, caller_type: str) -> Callable:
        """Return the callback method for the specified message type.

        Args:
            caller_type (str): message type parameter.

        Returns:
            Callable: if caller_type exists in callbacks keys, returns the
            corresponding callback, otherwise raises an value error.

        """
        if caller_type in self.callbacks:
            return self.callbacks[caller_type]
        else:
            raise ValueError(
                "Event type {caller_type} does not exist, must one of :"
                " {available_types}".format(
                     caller_type=caller_type,
                     available_types=list(self.callbacks.keys()))
                 )
