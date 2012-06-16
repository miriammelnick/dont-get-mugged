
###############################################################################
#
# ValidateUserCredentials
# Validates user credentials and returns user info by specifying a username and password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ValidateUserCredentials(Choreography):

    """
    Create a new instance of the ValidateUserCredentials Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/ValidateUserCredentials')


    def new_input_set(self):
        return ValidateUserCredentialsInputSet()

    def _make_result_set(self, result, path):
        return ValidateUserCredentialsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ValidateUserCredentialsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ValidateUserCredentials
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ValidateUserCredentialsInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) The OfficeDrop password that should be verified.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The OfficeDrop username that should be verified.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ValidateUserCredentials choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ValidateUserCredentialsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ValidateUserCredentialsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ValidateUserCredentialsResultSet(response, path)
