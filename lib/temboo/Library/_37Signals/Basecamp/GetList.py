
###############################################################################
#
# GetList
# Retrieves a single To-do list specified by its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetList(Choreography):

    """
    Create a new instance of the GetList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the ListID input for this choreography. ((integer) The ID for the To-Do list to return.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

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
A ResultSet with methods tailored to the values returned by the GetList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Basecamp.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
