
###############################################################################
#
# StatusesUpdate
# Allows you to update your Twitter status.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StatusesUpdate(Choreography):

    """
    Create a new instance of the StatusesUpdate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/StatusesUpdate')


    def new_input_set(self):
        return StatusesUpdateInputSet()

    def _make_result_set(self, result, path):
        return StatusesUpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusesUpdateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StatusesUpdate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatusesUpdateInputSet(InputSet):
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
        Set the value of the StatusUpdate input for this choreography. ((required, string) The text for your status update. 140-character limit.)
        """
        def set_StatusUpdate(self, value):
            InputSet._set_input(self, 'StatusUpdate', value)


"""
A ResultSet with methods tailored to the values returned by the StatusesUpdate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatusesUpdateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatusesUpdateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusesUpdateResultSet(response, path)
