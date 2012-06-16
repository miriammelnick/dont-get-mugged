
###############################################################################
#
# Lookup
# Returns user information for specific Twitter users. The Choreo accepts comma-separated lists of multiple screen names or user IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Lookup(Choreography):

    """
    Create a new instance of the Lookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Users/Lookup')


    def new_input_set(self):
        return LookupInputSet()

    def _make_result_set(self, result, path):
        return LookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Lookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LookupInputSet(InputSet):
        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Twitter after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Twitter after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process or provided by Twitter when registering your application)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process or provided by Twitter when registering your application)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ScreenName input for this choreography. ((conditional, string) The screen name of the Twitter user you want to retrieve information for. Required if UserId isn't specified.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)

        """
        Set the value of the UserId input for this choreography. ((conditional, integer) The user id of the Twitter user to return information for. Required if ScreenName isn't specified.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the Lookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LookupResultSet(response, path)
