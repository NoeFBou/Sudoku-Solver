# Author: Noe Florence
# Description: Implementation of the Observable class for the Observer design pattern.

class Observable:
    """
    A class that allows observers to subscribe and be notified of events.
    """

    def __init__(self):
        """Initialize the Observable with an empty list of observers."""
        self.observers = []

    def add_observer(self, observer):
        """
        Add an observer to the list of observers.
        Args:
            observer: The observer object to be added.
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove an observer from the list of observers.
        Args:
            observer: The observer object to be removed.
        """

        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, event=None):
        """
        Notify all observers about an event.
        Args:
            event: An optional event object containing event data.
        """

        for observer in self.observers:
            observer.update(self, event)
