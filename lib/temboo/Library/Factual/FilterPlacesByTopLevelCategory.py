
###############################################################################
#
# FilterPlacesByTopLevelCategory
# Find places by top-level category and near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FilterPlacesByTopLevelCategory(Choreography):

    """
    Create a new instance of the FilterPlacesByTopLevelCategory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterPlacesByTopLevelCategory')


    def new_input_set(self):
        return FilterPlacesByTopLevelCategoryInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByTopLevelCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByTopLevelCategoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByTopLevelCategory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FilterPlacesByTopLevelCategoryInputSet(InputSet):
        """
        Set the value of the Category input for this choreography. ((required, string) Enter a Factual top-level category to narrow the search results. See Choreo doc for a list of Factual top-level categories.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

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
A ResultSet with methods tailored to the values returned by the FilterPlacesByTopLevelCategory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FilterPlacesByTopLevelCategoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Factual.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FilterPlacesByTopLevelCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterPlacesByTopLevelCategoryResultSet(response, path)
