
###############################################################################
#
# GetRecentlyWatched
# Retrieves a subscriber's viewing history.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentlyWatched(Choreography):

    """
    Create a new instance of the GetRecentlyWatched Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Netflix/GetRecentlyWatched')


    def new_input_set(self):
        return GetRecentlyWatchedInputSet()

    def _make_result_set(self, result, path):
        return GetRecentlyWatchedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentlyWatchedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentlyWatched
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentlyWatchedInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Neflix after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Netflix after registering your application.)
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
        Set the value of the StartIndex input for this choreography. ((optional, integer) The offset number of the results from the query.)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the UpdatedMin input for this choreography. ((optional, date) If set, the response will include only those items with updated timestamps greater than or equal to the timestamp provided. Specify this value either in Unix time format (seconds since epoch).)
        """
        def set_UpdatedMin(self, value):
            InputSet._set_input(self, 'UpdatedMin', value)

        """
        Set the value of the UserID input for this choreography. ((required, string) The ID associated with the user whose recently watch movies you want to retrieve.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentlyWatched choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentlyWatchedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Netflix.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentlyWatchedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentlyWatchedResultSet(response, path)
