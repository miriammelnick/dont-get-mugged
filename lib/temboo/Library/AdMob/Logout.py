
###############################################################################
#
# Logout
# Logout from AdMob service.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Logout(Choreography):

    """
    Create a new instance of the Logout Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/Logout')


    def new_input_set(self):
        return LogoutInputSet()

    def _make_result_set(self, result, path):
        return LogoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogoutChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Logout
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LogoutInputSet(InputSet):
        """
        Set the value of the ClientKey input for this choreography. ((string) Enter user AdMob client key.)
        """
        def set_ClientKey(self, value):
            InputSet._set_input(self, 'ClientKey', value)

        """
        Set the value of the Token input for this choreography. ((string) Enter the token to be destroyed.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the Logout choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LogoutResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LogoutChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogoutResultSet(response, path)
