
###############################################################################
#
# ListLocationHistory
# Returns a list of a user's location history.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListLocationHistory(Choreography):

    """
    Create a new instance of the ListLocationHistory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Latitude/ListLocationHistory')


    def new_input_set(self):
        return ListLocationHistoryInputSet()

    def _make_result_set(self, result, path):
        return ListLocationHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListLocationHistoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListLocationHistory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListLocationHistoryInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((string) The client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((string) The client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Granularity input for this choreography. ((optional, string) Specify the level of detailed returned.  Enter: best, or city.  Default is city.)
        """
        def set_Granularity(self, value):
            InputSet._set_input(self, 'Granularity', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Enter the maximum number of results to return.  If unspecified, 100 results will be returned.  The maximum results returned is 1000.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the MaxTime input for this choreography. ((optional, integer) The maximum timestamp of the locations to return (in milliseconds since the epoch).)
        """
        def set_MaxTime(self, value):
            InputSet._set_input(self, 'MaxTime', value)

        """
        Set the value of the MinTime input for this choreography. ((optional, integer) The minimum timestamp of the locations to return (in milliseconds since the epoch).)
        """
        def set_MinTime(self, value):
            InputSet._set_input(self, 'MinTime', value)

        """
        Set the value of the RefreshToken input for this choreography. ((string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the ListLocationHistory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListLocationHistoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (XML) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListLocationHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListLocationHistoryResultSet(response, path)
