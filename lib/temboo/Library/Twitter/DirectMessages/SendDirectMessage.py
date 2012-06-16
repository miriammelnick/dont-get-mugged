
###############################################################################
#
# SendDirectMessage
# Sends a new direct message to the specified user from the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SendDirectMessage(Choreography):

    """
    Create a new instance of the SendDirectMessage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/DirectMessages/SendDirectMessage')


    def new_input_set(self):
        return SendDirectMessageInputSet()

    def _make_result_set(self, result, path):
        return SendDirectMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendDirectMessageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SendDirectMessage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendDirectMessageInputSet(InputSet):
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
        Set the value of the ScreenName input for this choreography. ((conditional, string) The screen name of the user who should receive the direct message. Required unless specifying the UserId.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)

        """
        Set the value of the Text input for this choreography. ((required, multiline) The text for the direct message. Max characters is 140.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the UserID input for this choreography. ((conditional, integer) The ID of the user who should receive the direct message. Required unless specifying the ScreenName.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)

        """
        Set the value of the WrapLinks input for this choreography. ((optional, boolean) When set to true, any valid URL found in the body will automatically be wrapped with the Twitter's t.co link wrapper.)
        """
        def set_WrapLinks(self, value):
            InputSet._set_input(self, 'WrapLinks', value)


"""
A ResultSet with methods tailored to the values returned by the SendDirectMessage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendDirectMessageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SendDirectMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendDirectMessageResultSet(response, path)
