
###############################################################################
#
# FindStoriesByCoordinates
# Return the most recent stories from a specified U.S. latitude and longitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindStoriesByCoordinates(Choreography):

    """
    Create a new instance of the FindStoriesByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Patch/FindStoriesByCoordinates')


    def new_input_set(self):
        return FindStoriesByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindStoriesByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindStoriesByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindStoriesByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindStoriesByCoordinatesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) A valid API key provided by Patch.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API shared secret provided by Patch.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Keyword input for this choreography. ((optional, string) Specify one or more words or phrases to find in the story title, story summary, and topic tags of the stories to return.)
        """
        def set_Keyword(self, value):
            InputSet._set_input(self, 'Keyword', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitiude for the area from which to retrieve stories. For example, "40.740512".)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Specify how many stories to return, between 1 and 100. The default is 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude for the area from which to retrieve stories. For example, "-73.991479".)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the MaximumAge input for this choreography. ((optional, integer) Specify the maximum age in days of the stories to return, between 1 and 30. The default is 10.)
        """
        def set_MaximumAge(self, value):
            InputSet._set_input(self, 'MaximumAge', value)

        """
        Set the value of the Radius input for this choreography. ((optional, integer) Specify a radius in feet in which to search the specified coordinates, between 500 and 26,400. The default is 1,000 feet.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify "xml" to convert the Patch JSON response to XML. The default is "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FindStoriesByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindStoriesByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response returned from Patch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindStoriesByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindStoriesByCoordinatesResultSet(response, path)
