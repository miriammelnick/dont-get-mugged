
###############################################################################
#
# DirectMessagesSent
# Retrieves the 20 most recent direct messages sent by the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DirectMessagesSent(Choreography):

    """
    Create a new instance of the DirectMessagesSent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/DirectMessages/DirectMessagesSent')


    def new_input_set(self):
        return DirectMessagesSentInputSet()

    def _make_result_set(self, result, path):
        return DirectMessagesSentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DirectMessagesSentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DirectMessagesSent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DirectMessagesSentInputSet(InputSet):
        """
        Set the value of the Count input for this choreography. ((optional, integer) Specifies the number of records to retrieve up to a maximum of 200.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) An advanced option for returning more verbose metadata. When set to either true, t or 1, each tweet will include a node called "entities".)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the MaxID input for this choreography. ((optional, integer) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        def set_MaxID(self, value):
            InputSet._set_input(self, 'MaxID', value)

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
        Set the value of the Page input for this choreography. ((optional, integer) Specifies the page of results to retrieve.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the SinceID input for this choreography. ((optional, integer) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        def set_SinceID(self, value):
            InputSet._set_input(self, 'SinceID', value)


"""
A ResultSet with methods tailored to the values returned by the DirectMessagesSent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DirectMessagesSentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DirectMessagesSentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DirectMessagesSentResultSet(response, path)
