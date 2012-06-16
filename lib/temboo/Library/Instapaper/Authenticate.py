
###############################################################################
#
# Authenticate
# Validate an Instapaper account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Authenticate(Choreography):

    """
    Create a new instance of the Authenticate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instapaper/Authenticate')


    def new_input_set(self):
        return AuthenticateInputSet()

    def _make_result_set(self, result, path):
        return AuthenticateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AuthenticateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Authenticate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AuthenticateInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Enter an Instapaper password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Enter an Instapaper username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the Authenticate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AuthenticateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Instapaper. Successful reqests will return a 200 status code.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AuthenticateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AuthenticateResultSet(response, path)
