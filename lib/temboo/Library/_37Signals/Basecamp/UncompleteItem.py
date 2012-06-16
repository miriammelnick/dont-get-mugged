
###############################################################################
#
# UncompleteItem
# Marks a single, specified item in a To-do list as incomplete.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UncompleteItem(Choreography):

    """
    Create a new instance of the UncompleteItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/UncompleteItem')


    def new_input_set(self):
        return UncompleteItemInputSet()

    def _make_result_set(self, result, path):
        return UncompleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UncompleteItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UncompleteItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UncompleteItemInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the ItemID input for this choreography. ((integer) The ID of the item to mark as complete.)
        """
        def set_ItemID(self, value):
            InputSet._set_input(self, 'ItemID', value)

        """
        Set the value of the Password input for this choreography. ((string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the UncompleteItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UncompleteItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (There is no structrued response from uncomplete item requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UncompleteItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UncompleteItemResultSet(response, path)
