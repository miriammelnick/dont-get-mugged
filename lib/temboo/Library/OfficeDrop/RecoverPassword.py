
###############################################################################
#
# RecoverPassword
# Recovers a  password by triggering an email to a specified email address belonging to the user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RecoverPassword(Choreography):

    """
    Create a new instance of the RecoverPassword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/RecoverPassword')


    def new_input_set(self):
        return RecoverPasswordInputSet()

    def _make_result_set(self, result, path):
        return RecoverPasswordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecoverPasswordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RecoverPassword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecoverPasswordInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email address associated with the password you want to recover.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username associated with the password you want to recover.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RecoverPassword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecoverPasswordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RecoverPasswordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecoverPasswordResultSet(response, path)
