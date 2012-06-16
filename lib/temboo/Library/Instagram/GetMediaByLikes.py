
###############################################################################
#
# GetMediaByLikes
# Retrieves a list of what media is most popular at the moment, sorted by Likes.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMediaByLikes(Choreography):

    """
    Create a new instance of the GetMediaByLikes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetMediaByLikes')


    def new_input_set(self):
        return GetMediaByLikesInputSet()

    def _make_result_set(self, result, path):
        return GetMediaByLikesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMediaByLikesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMediaByLikes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMediaByLikesInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the MediaID input for this choreography. ((required, integer) The ID of the media object you want to retrieve. For example, a valid MediaID could be 3.)
        """
        def set_MediaID(self, value):
            InputSet._set_input(self, 'MediaID', value)


"""
A ResultSet with methods tailored to the values returned by the GetMediaByLikes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMediaByLikesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMediaByLikesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMediaByLikesResultSet(response, path)
