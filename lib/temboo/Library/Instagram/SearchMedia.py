
###############################################################################
#
# SearchMedia
# Allows you to search for media in a given area.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchMedia(Choreography):

    """
    Create a new instance of the SearchMedia Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/SearchMedia')


    def new_input_set(self):
        return SearchMediaInputSet()

    def _make_result_set(self, result, path):
        return SearchMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchMediaChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchMedia
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchMediaInputSet(InputSet):
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
        Set the value of the Distance input for this choreography. ((optional, integer) The distance in meters. Defaults to 1000. Max is 5000.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) Latitude of the center search coordinate.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) Longitude of the center search coordinate.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the MaxTimestamp input for this choreography. ((optional, date) A unix timestamp. All media returned will be taken earlier than this timestamp.)
        """
        def set_MaxTimestamp(self, value):
            InputSet._set_input(self, 'MaxTimestamp', value)

        """
        Set the value of the MinTimestamp input for this choreography. ((optional, date) A unix timestamp. All media returned will be taken later than this timestamp.)
        """
        def set_MinTimestamp(self, value):
            InputSet._set_input(self, 'MinTimestamp', value)


"""
A ResultSet with methods tailored to the values returned by the SearchMedia choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchMediaResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchMediaResultSet(response, path)
