
###############################################################################
#
# FilterRestaurantsByCuisineAndCoordinates
# Find restaurants by cuisine and near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FilterRestaurantsByCuisineAndCoordinates(Choreography):

    """
    Create a new instance of the FilterRestaurantsByCuisineAndCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterRestaurantsByCuisineAndCoordinates')


    def new_input_set(self):
        return FilterRestaurantsByCuisineAndCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FilterRestaurantsByCuisineAndCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterRestaurantsByCuisineAndCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FilterRestaurantsByCuisineAndCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FilterRestaurantsByCuisineAndCoordinatesInputSet(InputSet):
        """
        Set the value of the Cuisine input for this choreography. ((required, string) Enter a desired cuisine to narrow the search results. See Choreo doc for a list of available cuisine parameters.)
        """
        def set_Cuisine(self, value):
            InputSet._set_input(self, 'Cuisine', value)

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
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by SimpleGeo after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by SimpleGeo after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the Radius input for this choreography. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)


"""
A ResultSet with methods tailored to the values returned by the FilterRestaurantsByCuisineAndCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FilterRestaurantsByCuisineAndCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Factual.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FilterRestaurantsByCuisineAndCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterRestaurantsByCuisineAndCoordinatesResultSet(response, path)
