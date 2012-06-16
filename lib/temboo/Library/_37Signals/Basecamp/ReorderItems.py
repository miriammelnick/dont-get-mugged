
###############################################################################
#
# ReorderItems
# Reorders the items in a specified To-do list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ReorderItems(Choreography):

    """
    Create a new instance of the ReorderItems Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/ReorderItems')


    def new_input_set(self):
        return ReorderItemsInputSet()

    def _make_result_set(self, result, path):
        return ReorderItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReorderItemsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ReorderItems
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ReorderItemsInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the FirstItemID input for this choreography. ((integer) The ID number for the first item in the list.)
        """
        def set_FirstItemID(self, value):
            InputSet._set_input(self, 'FirstItemID', value)

        """
        Set the value of the ListID input for this choreography. ((integer) The ID for the To-do list the items of which you're reordering.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

        """
        Set the value of the Password input for this choreography. ((string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SecondItemID input for this choreography. ((optional, integer) The ID number for the second item in the list.)
        """
        def set_SecondItemID(self, value):
            InputSet._set_input(self, 'SecondItemID', value)

        """
        Set the value of the ThirdItemID input for this choreography. ((optional, integer) The ID number for the third item in the list.)
        """
        def set_ThirdItemID(self, value):
            InputSet._set_input(self, 'ThirdItemID', value)

        """
        Set the value of the Username input for this choreography. ((string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ReorderItems choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ReorderItemsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (No response is returned from Basecamp for reorder items requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ReorderItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReorderItemsResultSet(response, path)
