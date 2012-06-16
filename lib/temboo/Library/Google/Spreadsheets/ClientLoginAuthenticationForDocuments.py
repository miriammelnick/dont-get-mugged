
###############################################################################
#
# ClientLoginAuthenticationForDocuments
# Request an authorization token for Google Documents.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ClientLoginAuthenticationForDocuments(Choreography):

    """
    Create a new instance of the ClientLoginAuthenticationForDocuments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/ClientLoginAuthenticationForDocuments')


    def new_input_set(self):
        return ClientLoginAuthenticationForDocumentsInputSet()

    def _make_result_set(self, result, path):
        return ClientLoginAuthenticationForDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ClientLoginAuthenticationForDocumentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ClientLoginAuthenticationForDocuments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ClientLoginAuthenticationForDocumentsInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ClientLoginAuthenticationForDocuments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ClientLoginAuthenticationForDocumentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Stores the response from Google login.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AuthorizationKey" output from this choreography execution. ((string) The authorization token parsed from the Google login response.)
        """
        def get_AuthorizationKey(self):
            return self._output.get('AuthorizationKey', None)

class ClientLoginAuthenticationForDocumentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ClientLoginAuthenticationForDocumentsResultSet(response, path)
