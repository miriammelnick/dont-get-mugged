
###############################################################################
#
# CompleteItem
# Marks a single, specified item in a To-do list as complete.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CompleteItem(Choreography):

    """
    Create a new instance of the CompleteItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CompleteItem')


    def new_input_set(self):
        return CompleteItemInputSet()

    def _make_result_set(self, result, path):
        return CompleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompleteItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CompleteItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CompleteItemInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the CompleteItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CompleteItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (There is no structrued response from complete item requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CompleteItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompleteItemResultSet(response, path)
