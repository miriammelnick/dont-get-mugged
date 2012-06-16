
###############################################################################
#
# AccountLogin
# Retrieves an authentication token from FilesAnywhere.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AccountLogin(Choreography):

    """
    Create a new instance of the AccountLogin Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/AccountLogin')


    def new_input_set(self):
        return AccountLoginInputSet()

    def _make_result_set(self, result, path):
        return AccountLoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountLoginChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AccountLogin
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AccountLoginInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by FilesAnywhere.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AllowedIPList input for this choreography. ((optional, string) List of allowed IP addresses.  Multiple IP addresses can be separated by commas.)
        """
        def set_AllowedIPList(self, value):
            InputSet._set_input(self, 'AllowedIPList', value)

        """
        Set the value of the ClientEncryptParam input for this choreography. ((optional, string) Used to return an encrypted password to use for subsequent logins.)
        """
        def set_ClientEncryptParam(self, value):
            InputSet._set_input(self, 'ClientEncryptParam', value)

        """
        Set the value of the OrgID input for this choreography. ((optional, integer) Defaults to 0 for a FilesAnywhere Web account.  Use 50 for a FilesAnywhere WebAdvanced account.)
        """
        def set_OrgID(self, value):
            InputSet._set_input(self, 'OrgID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your FilesAnywhere password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserName input for this choreography. ((required, string) Your FilesAnywhere username.)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)


"""
A ResultSet with methods tailored to the values returned by the AccountLogin choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AccountLoginResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FilesAnywhere.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((string) The token value parsed from the FilesAnywhere response.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class AccountLoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountLoginResultSet(response, path)
