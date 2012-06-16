
###############################################################################
#
# GetAccountInfo
# Retrieves information about a specified Google Documents account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAccountInfo(Choreography):

    """
    Create a new instance of the GetAccountInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/GetAccountInfo')


    def new_input_set(self):
        return GetAccountInfoInputSet()

    def _make_result_set(self, result, path):
        return GetAccountInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAccountInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAccountInfoInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetAccountInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAccountInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAccountInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountInfoResultSet(response, path)
