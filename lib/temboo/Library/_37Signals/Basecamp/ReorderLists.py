
###############################################################################
#
# ReorderLists
# Allows you to reorder To-do lists in a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ReorderLists(Choreography):

    """
    Create a new instance of the ReorderLists Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/ReorderLists')


    def new_input_set(self):
        return ReorderListsInputSet()

    def _make_result_set(self, result, path):
        return ReorderListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReorderListsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ReorderLists
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ReorderListsInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the FirstListID input for this choreography. ((integer) The ID number for the project's first To-Do list.)
        """
        def set_FirstListID(self, value):
            InputSet._set_input(self, 'FirstListID', value)

        """
        Set the value of the Password input for this choreography. ((string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProjectID input for this choreography. ((integer) The ID for the project associated with the to-do lists that you are reordering.)
        """
        def set_ProjectID(self, value):
            InputSet._set_input(self, 'ProjectID', value)

        """
        Set the value of the SecondListID input for this choreography. ((optional, integer) The ID number for the project's second To-Do list.)
        """
        def set_SecondListID(self, value):
            InputSet._set_input(self, 'SecondListID', value)

        """
        Set the value of the ThirdListID input for this choreography. ((optional, integer) The ID number for the project's third To-Do list.)
        """
        def set_ThirdListID(self, value):
            InputSet._set_input(self, 'ThirdListID', value)

        """
        Set the value of the Username input for this choreography. ((string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ReorderLists choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ReorderListsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (No response is returned from Basecamp for update requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ReorderListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReorderListsResultSet(response, path)
