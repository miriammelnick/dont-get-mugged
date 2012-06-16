
###############################################################################
#
# FriendshipsLookup
# Retrieves the relationship of the authenticating user to the comma-separated list of up to 100 screen names or user IDs provided.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FriendshipsLookup(Choreography):

    """
    Create a new instance of the FriendshipsLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/FriendshipsLookup')


    def new_input_set(self):
        return FriendshipsLookupInputSet()

    def _make_result_set(self, result, path):
        return FriendshipsLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendshipsLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FriendshipsLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FriendshipsLookupInputSet(InputSet):
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
        Set the value of the ScreenName input for this choreography. ((conditional, string) The screen name for the friend you want to create a friendship with. Required if UserId isn't specified.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)

        """
        Set the value of the UserID input for this choreography. ((conditional, integer) The user ID for the friend you want to create a friendship with. Required if ScreenName isn't specified.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the FriendshipsLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FriendshipsLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FriendshipsLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FriendshipsLookupResultSet(response, path)
