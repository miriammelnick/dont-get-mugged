
###############################################################################
#
# SuggestedCompaniesToFollow
# Returns a list of suggested companies to be followed by this user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SuggestedCompaniesToFollow(Choreography):

    """
    Create a new instance of the SuggestedCompaniesToFollow Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/SuggestedCompaniesToFollow')


    def new_input_set(self):
        return SuggestedCompaniesToFollowInputSet()

    def _make_result_set(self, result, path):
        return SuggestedCompaniesToFollowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SuggestedCompaniesToFollowChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SuggestedCompaniesToFollow
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SuggestedCompaniesToFollowInputSet(InputSet):
        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)


"""
A ResultSet with methods tailored to the values returned by the SuggestedCompaniesToFollow choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SuggestedCompaniesToFollowResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SuggestedCompaniesToFollowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SuggestedCompaniesToFollowResultSet(response, path)
