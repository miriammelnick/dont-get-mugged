
###############################################################################
#
# TrendingVenues
# Returns a list of venues near the current location with the most people currently checked in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TrendingVenues(Choreography):

    """
    Create a new instance of the TrendingVenues Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/TrendingVenues')


    def new_input_set(self):
        return TrendingVenuesInputSet()

    def _make_result_set(self, result, path):
        return TrendingVenuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrendingVenuesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TrendingVenues
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TrendingVenuesInputSet(InputSet):
        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to retun, up to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude point of the user's location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Radius input for this choreography. ((optional, integer) Radius in meters, up to approximately 2000 meters.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the TrendingVenues choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TrendingVenuesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TrendingVenuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrendingVenuesResultSet(response, path)
