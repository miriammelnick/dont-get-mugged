
###############################################################################
#
# FindPlacesNearCoordinates
# Find places near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindPlacesNearCoordinates(Choreography):

    """
    Create a new instance of the FindPlacesNearCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Factual/FindPlacesNearCoordinates')


    def new_input_set(self):
        return FindPlacesNearCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindPlacesNearCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindPlacesNearCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindPlacesNearCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindPlacesNearCoordinatesInputSet(InputSet):
        """
        Set the value of the Latitude input for this choreography. ((required, decimal) Enter latitude coordinates of the location defining the center of the search radius.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) Enter longitude coordinates of the location defining the center of the search radius.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Factual after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Factual after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A search string (i.e. Starbucks))
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Radius input for this choreography. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)


"""
A ResultSet with methods tailored to the values returned by the FindPlacesNearCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindPlacesNearCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Factual.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindPlacesNearCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindPlacesNearCoordinatesResultSet(response, path)
