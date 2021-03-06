
###############################################################################
#
# Mayorships
# Returns a user's mayorships.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Mayorships(Choreography):

    """
    Create a new instance of the Mayorships Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/Mayorships')


    def new_input_set(self):
        return MayorshipsInputSet()

    def _make_result_set(self, result, path):
        return MayorshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MayorshipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Mayorships
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MayorshipsInputSet(InputSet):
        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Identity of the user to get mayorships for. Defaults to "self" to get lists of the acting user.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the Mayorships choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MayorshipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MayorshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MayorshipsResultSet(response, path)
