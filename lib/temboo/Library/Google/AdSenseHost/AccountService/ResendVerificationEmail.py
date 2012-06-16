
###############################################################################
#
# ResendVerificationEmail
# Resends the verification email. The verification email can be sent up to three times.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ResendVerificationEmail(Choreography):

    """
    Create a new instance of the ResendVerificationEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/ResendVerificationEmail')


    def new_input_set(self):
        return ResendVerificationEmailInputSet()

    def _make_result_set(self, result, path):
        return ResendVerificationEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResendVerificationEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ResendVerificationEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ResendVerificationEmailInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((string) The ID of the publisher to send a verification email to.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the DeveloperURL input for this choreography. ((string) The developer site URL.)
        """
        def set_DeveloperURL(self, value):
            InputSet._set_input(self, 'DeveloperURL', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the ResendVerificationEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ResendVerificationEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ResendVerificationEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ResendVerificationEmailResultSet(response, path)
