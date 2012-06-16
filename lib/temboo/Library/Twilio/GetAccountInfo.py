
###############################################################################
#
# GetAccountInfo
# Obtain account information.
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
        Choreography.__init__(self, temboo_session, '/Library/Twilio/GetAccountInfo')


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
        Set the value of the AccountSID input for this choreography. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        def set_AccountSID(self, value):
            InputSet._set_input(self, 'AccountSID', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)


"""
A ResultSet with methods tailored to the values returned by the GetAccountInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAccountInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAccountInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountInfoResultSet(response, path)
