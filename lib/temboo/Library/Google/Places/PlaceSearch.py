
###############################################################################
#
# PlaceSearch
# Search for places based on latitude/longitude coordinates, keywords, and distance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PlaceSearch(Choreography):

    """
    Create a new instance of the PlaceSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/PlaceSearch')


    def new_input_set(self):
        return PlaceSearchInputSet()

    def _make_result_set(self, result, path):
        return PlaceSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PlaceSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PlaceSearchInputSet(InputSet):
        """
        Set the value of the Key input for this choreography. ((required, string) Enter your Google API key.)
        """
        def set_Key(self, value):
            InputSet._set_input(self, 'Key', value)

        """
        Set the value of the Keyword input for this choreography. ((optional, string) Enter a keyword (term, address, type, customer review, etc.) to be matched against all results retrieved for this Place.)
        """
        def set_Keyword(self, value):
            InputSet._set_input(self, 'Keyword', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Latitude input for this choreography. ((required, string) Specify a latitude point around which Places results will be retrieved.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, string) Specify a longitude point around which Places results will be retrieved.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) Enter a name to be matched when results are retrieved for this specified Place.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Radius input for this choreography. ((optional, integer) Specify the radius in meters, for which Places results will be returned. Maximum radius is limited to 50,000 meters. If rankby=distance, then radius must not be specified.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)

        """
        Set the value of the RankBy input for this choreography. ((optional, string) Specify how results are listed. Values include: prominence (default); distance - sorts results by distance from specified location. Radius must not be used, and Keyword, Name, or Types are required).)
        """
        def set_RankBy(self, value):
            InputSet._set_input(self, 'RankBy', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)

        """
        Set the value of the Types input for this choreography. ((optional, string) Filter results by types, such as: bar, dentist.  Multiple types must be separated by the pipe ("|") symbol: bar|dentist||airport.)
        """
        def set_Types(self, value):
            InputSet._set_input(self, 'Types', value)


"""
A ResultSet with methods tailored to the values returned by the PlaceSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PlaceSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PlaceSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PlaceSearchResultSet(response, path)
