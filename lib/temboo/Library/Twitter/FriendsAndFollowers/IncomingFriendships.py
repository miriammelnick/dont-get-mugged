
###############################################################################
#
# IncomingFriendships
# Retrieves a list of numeric IDs for every user who has a pending request to follow the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class IncomingFriendships(Choreography):

    """
    Create a new instance of the IncomingFriendships Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/IncomingFriendships')


    def new_input_set(self):
        return IncomingFriendshipsInputSet()

    def _make_result_set(self, result, path):
        return IncomingFriendshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IncomingFriendshipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the IncomingFriendships
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class IncomingFriendshipsInputSet(InputSet):
        """
        Set the value of the Cursor input for this choreography. ((optional, integer) Used to page through large results. Provide a value of -1 to begin paging. Use values as returned in the response body's next_cursor and previous_cursor attributes to page back and forth in the list.)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

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
        Set the value of the StringifyIDs input for this choreography. ((optional, boolean) Many programming environments will not consume Twitter IDs due to their size. Provide this option to have ids returned as strings instead. Set to 1 to enable.)
        """
        def set_StringifyIDs(self, value):
            InputSet._set_input(self, 'StringifyIDs', value)


"""
A ResultSet with methods tailored to the values returned by the IncomingFriendships choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class IncomingFriendshipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class IncomingFriendshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return IncomingFriendshipsResultSet(response, path)
