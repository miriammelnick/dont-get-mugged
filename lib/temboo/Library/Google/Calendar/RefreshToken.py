
###############################################################################
#
# RefreshToken
# Retrieves a new access token when the provided access token is expired.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RefreshToken(Choreography):

    """
    Create a new instance of the RefreshToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/RefreshToken')


    def new_input_set(self):
        return RefreshTokenInputSet()

    def _make_result_set(self, result, path):
        return RefreshTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefreshTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RefreshToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RefreshTokenInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((required, string) The client ID provided by Google when you sign up for an account.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The client secret provided by Google when you sign up for an account.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the OAuth process to be used when your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the RefreshToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RefreshTokenResultSet(ResultSet):
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((string) The access token that is parsed from the request to refresh the token.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class RefreshTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefreshTokenResultSet(response, path)
