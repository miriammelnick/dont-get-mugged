
###############################################################################
#
# UserRegistration
# Register a new user account at OfficeDrop with your application.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UserRegistration(Choreography):

    """
    Create a new instance of the UserRegistration Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/UserRegistration')


    def new_input_set(self):
        return UserRegistrationInputSet()

    def _make_result_set(self, result, path):
        return UserRegistrationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserRegistrationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UserRegistration
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UserRegistrationInputSet(InputSet):
        """
        Set the value of the CustomerName input for this choreography. ((required, string) The customer name that is associated with the new registration)
        """
        def set_CustomerName(self, value):
            InputSet._set_input(self, 'CustomerName', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address that is associated with the new registration)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password that is associated with the new registration)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username that is associated with the new registration)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the UserRegistration choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UserRegistrationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UserRegistrationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserRegistrationResultSet(response, path)
